# -*- coding: utf-8 -*-
# © 2016 Eficent Business and IT Consulting Services S.L.
# - Jordi Ballester Alomar
# © 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models
from openerp.tools import misc
from openerp.exceptions import Warning
from openerp.tools.translate import _


class SummaryReport(models.TransientModel):
    _name = 'wiz.bank.unreconcile'

    @api.model
    def _get_unreconcile_entries(self):
        cr, uid, context = self.env.args
        context = dict(context)
        bank_id = context.get('active_id')
        self.env.args = cr, uid, misc.frozendict(context)
        bank = self.env['account.bank.statement'].browse(bank_id)
        clearing_account_id = bank.journal_id and\
            bank.journal_id.default_credit_account_id and\
            bank.journal_id.default_credit_account_id.clearing_account_id and\
            bank.journal_id.default_credit_account_id.clearing_account_id.id
        if clearing_account_id:
            account_move_line_records = self.env['account.move.line'].search([
                ('account_id', '=', clearing_account_id),
                ('account_id.reconcile', '=', True),
                '|',
                ('reconcile_id', '=', False),
                ('reconcile_partial_id', '!=', False)
            ], order='date')
        else:
            raise Warning(_("Create an Clearing Account to get "
                            "the Unreconciled Journal Items."))
        return account_move_line_records

    line_ids = fields.Many2many('account.move.line',
                                'wiz_unreconciles_move_line_rel',
                                'reconciles_id', 'accounts_id',
                                'Journal Items to Reconcile',
                                default=_get_unreconcile_entries)

    @api.multi
    def process_wiz(self):
        context = dict(self._context)
        bank_stmt_obj = self.env['account.bank.statement']
        currency_obj = self.env['res.currency']
        statement = bank_stmt_obj.browse(context.get('active_ids'))
        lines = []
        for line in self.line_ids:
            amount = 0.0
            if line.debit > 0:
                amount = line.debit
            elif line.credit > 0:
                amount = -line.credit
            if line.amount_currency:
                if line.company_id.currency_id.id != statement.currency.id:
                    amount = currency_obj.compute(line.currency_id.id,
                                                  statement.currency.id,
                                                  line.amount_currency)
            elif (line.invoice and line.invoice.currency_id.id !=
                statement.currency.id):
                amount = currency_obj.compute(line.invoice.currency_id.id,
                                              statement.currency.id, amount)
            lines.append((0, 0, {
                'name': line.name or '?',
                'ref': line.ref,
                'partner_id': line.partner_id.id,
                'amount': amount,
                'date': line.date,
                'amount_currency': line.amount_currency,
                'currency_id': line.currency_id.id,
            }))
        statement.write({'line_ids': lines})
        return True
