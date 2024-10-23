# -*- coding: utf-8 -*-
{
    'name': "Purchas line notes",

    'summary': "Add notes to the purchase order lines",

    'description': """
Add notes to the purchase order lines
    """,

    'author': "Javier Diez",
    'website': "https://javierdiez.netlify.app/",
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order_line_note_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images": ['static/images/banner.png', 'static/description/icon.png'],
}
