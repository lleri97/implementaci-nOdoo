# -*- coding: utf-8 -*-
{
    'name': "2dam2curious_subscription",

    'summary': """subscritkjasdfblajshbdflbdhj""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Grupo 5 Reto2",
    'website': "http://www.2dam2curious.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/subscription.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True
}