
# -*- coding: utf-8 -*-
{
    'name': "Partner documents",

    'summary': """Module to attach files to Contacts. Each file can have a name and be downloaded from the form view of each contact.""",

    'description': """
        
        Module to attach files to Contacts. Each file can have a name and be downloaded from the form view of each contact.
        
    """,

    'author': "Javier Diez",
    'website': "https://javierdiez.netlify.app/",
    'license': 'AGPL-3',
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
    "images": ['static/src/img/banner.jpg', 'static/description/icon.png'],
}
