{
    'name': 'CustomSales',
    'version': '0.1',
    'summary': 'custom sales module',
    'description': 'Module de vente personnalisé',
    'category': 'Uncategorized',
    'author': 'Author',
    'depends': ['base','sale'],
    'data': [
        'views/facture_view.xml',
        'report/facture_report.xml',
        'report/facture_report_template.xml',
    ],
    'installable': True,
}
