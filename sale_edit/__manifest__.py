{
    'name': 'sale_edit',
    'version': '0.2',
    'description': 'Modifications module vente et service sur site',
    'category': 'Uncategorized',
    'author': 'OCI',
    'depends': ['base','account','sale','industry_fsm'],
    'data': [
        'views/inherited_invoice_view.xml',
        'views/inherited_sale_view.xml',
        'views/inherited_portal_view.xml',
        'views/inherited_fsm_view.xml',
        'data/numerobi_sequence_data.xml'
    ],
    'installable': True,
    'application': True,
}
