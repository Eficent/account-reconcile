# © 2018 Eficent Business and IT Consulting Services S.L. (www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    reconcile_account_ids = fields.Many2many(
        string='Accounts to consider in the reconciliation',
        comodel_name='account.account',
        relation='account_reconcile_account_journal_rel',
        domain=[('reconcile', '=', True)],
        help="If you enter accounts here they will be the only ones"
             "to be considered during the reconciliation")
