
# -*- coding: utf-8 -*-
{
    'name': "Partner documents",

    'summary': """Add documents to partners""",

    'description': """
        
        Add documents to partners
        
    """,

    'author': "Javier Diez",
    'category': 'Contacts',
    'version': '18.0',
    'depends': ['base','mail','contacts'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/documents_views.xml',
    ],
    "images": ['static/images/banner.png', 'static/description/icon.png'],
}
