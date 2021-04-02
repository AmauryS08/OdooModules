# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'JournaMod',
    'version': '0.1',
    'author': "a",
    'description': "Premier module test",
    'category': 'Uncategorized',
    'depends': ['base', 'hr'],
    'data': [
        'views/journalier.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
