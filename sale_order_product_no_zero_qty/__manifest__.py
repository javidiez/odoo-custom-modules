# -*- coding: utf-8 -*-
{
    'name': "Sale order product no zero quantity",

    'summary': "This module restricts the confirmation of sales orders with products that have zero quantities.",

    'description': """
This module restricts the confirmation of sales orders with products that have zero quantities. Additionally, it adds a button to remove products with zero quantities.
    """,

    'author': "Javier Diez",
    'website': "https://javierdiez.netlify.app/",
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '18.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images": ['static/images/banner.png', 'static/description/icon.png'],
}
