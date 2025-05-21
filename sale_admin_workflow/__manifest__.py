{
    'name': 'Sale Admin Workflow',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage Sale Admin role, order limits, and automated workflows',
    'depends': ['sale_management', 'stock', 'account'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
