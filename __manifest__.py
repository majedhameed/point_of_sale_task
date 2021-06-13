# -*- coding: utf-8 -*-
{
    'name': "point_of_sale_task",

    'summary': """
        This Module Perform the following task show tax amount in pos order screen:""",

    'description': """
        show tax amount in pos order screen:
    """,

    'author': "MajedShogaa",
    'website': "majedshogaa@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/pos_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/show_tax.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
