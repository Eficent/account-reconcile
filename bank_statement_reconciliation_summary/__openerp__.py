# -*- coding: utf-8 -*-
# © 2016 Eficent Business and IT Consulting Services S.L.
# - Jordi Ballester Alomar
# © 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Bank Statement Reconciliation Summary',
    'category': 'Account',
    'summary': 'Bank Statement Reconciliation Summary',
    'version': '8.0.1.0.0',
    'author': 'Eficent Business and IT Consulting Services S.L., '
              'Serpent Consulting Services Pvt. Ltd.,'
              'Odoo Community Association (OCA)',
    'depends': ['account'],
    'data': [
        'report/summary_report.xml',
        'report/report.xml',
        'view/account_account_view.xml',
        'view/account_bank_statement.xml',
        'wizard/account_bank_unreconcile_view.xml',
    ],
    'installable': True,
}
