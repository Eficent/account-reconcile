# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Bank Statement Default Rule",
    "summary": "Apply default values in bank statement lines depending "
               "on matched patterns",
    "version": "12.0.1.0.0",
    "depends": ["account"],
    "author": "Eficent, Odoo Community Association (OCA)",
    "website": "http://www.github.com/OCA/account-reconcile",
    "category": "Finance",
    "data": [
        "security/ir.model.access.csv",
        "views/bank_statement_default_rule_views.xml",
        "views/account_bank_statement_views.xml",
    ],
    'license': 'AGPL-3',
    "auto_install": False,
    'installable': True,
}
