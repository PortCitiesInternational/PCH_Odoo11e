# -*- coding: utf-8 -*-
{
    'name': 'PCH Sale',
    'version': '1.0',
    'author': 'Portcities',
    'website': 'portcities.net',
    'category': 'Sales',
    'summary' : 'Customize on Sale Order',
    'description' : """
    v 1.0
    Customize Report Sale Order \n
    by AK.\n
    v 2.0\n
    - Customize Report Customer Invoice\n
    - Adjust report format\n
    - Remove Tax from sales and invoice report\n
    - Add Bank Account information to sales and invoice report\n
    """,
    'depends': [
        'sale','web'
    ],
    'data':[
        'report/pch_sale_paperformat.xml',
        'report/invoice_report.xml',
        'report/invoice_report_template.xml',
        'report/sale_report.xml',
        'report/sale_report_template.xml',
        'views/account_invoice_view.xml',
        'views/sale_view.xml',
        'views/web.xml',
    ],
    'active': False,
    'installable': True,
    'application': False,
    'auto_install': False,
}
