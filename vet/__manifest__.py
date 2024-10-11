# -*- coding: utf-8 -*-
{
    'name': "Gestión veterinaria",

    'summary': "Administrar los animales que visitan nuestra veterinaria",

    'description': """
Administrar los animales que visitan nuestra veterinaria
    """,

    'author': "Javier Diez",
    'website': "https://www.javierdiez.netlify.app",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Animals',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/animals_views.xml',
        'views/medicines_views.xml',
        'views/allergies_views.xml',
        'views/surgeries_views.xml',
        'views/vaccines_views.xml',
        'views/insurances_views.xml',
        'views/visits_views.xml',
        'views/species_views.xml',
        'views/breeds_views.xml',
        'views/tags_views.xml',
        'views/animal_partner_views.xml',
        'views/animals_menus.xml',
        'views/visit_sequence.xml',
        'views/animals_identification.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

