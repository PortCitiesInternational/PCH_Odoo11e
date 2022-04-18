{
    'name': 'PCH Sale',
    'version': '15.0.1.0.0',
    'author': 'Portcities',
    'license': 'LGPL-3',
    'website': 'portcities.net',
    'category': 'Sales/Sales',
    'summary' : 'Customization on Sale Order',
    'description' : """
        - Customize Report Sale Order \n
        - Customize Report Customer Invoice\n
        - Adjust report format\n
        - Remove Tax from sales and invoice report\n
        - Add Bank Account information to sales and invoice report\n
    """,
    'depends': ['sale_management'],
    'data':[
        'report/pch_sale_paperformat.xml',
        'report/invoice_report.xml',
        'report/invoice_report_template.xml',
        'report/sale_report.xml',
        'report/sale_report_template.xml',
        'views/account_move_view.xml',
        'views/sale_order_view.xml'],
    'active': False,
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.report_assets_common': [
            '/pch_sale/static/src/less/layout_background.less',
        ],
    }
}
