# -*- coding: utf-8 -*-
{
    'name': "ab-travel-umroh",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ammarzakiy Faris",
    'website': "https://www.amrzakiy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sequence_data.xml',
        'views/views.xml',
        'views/package_views.xml',
        'views/menuitem_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}
