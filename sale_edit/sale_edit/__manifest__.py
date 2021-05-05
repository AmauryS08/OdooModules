{
    'name': 'sale_edit',
    'version': '0.1',
    'description': 'Modifications module sale',
    'category': 'Uncategorized',
    'author': 'Author',
    'depends': ['base','account','sale'],
    'data': [
        'views/inherited_invoice_view.xml',
        'views/inherited_sale_view.xml',
        'views/inherited_portal_view.xml'
    ],
    'installable': True,
    'application': True,
}
