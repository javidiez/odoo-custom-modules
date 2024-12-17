# -*- coding: utf-8 -*-
{
    'name': "Calendar meeting room",

    'summary': "Add the room of the calendar event",

    'description': """
Add the room of the calendar event
    """,

    'author': "Javier Diez",
    'website': "https://javierdiez.netlify.app/",
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Calendar',
    'version': '18.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/calendar_meeting_room.xml',
        'views/rooms_configuration.xml',
        'views/room_menues.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images": ['static/images/banner.png', 'static/description/icon.png'],
}
