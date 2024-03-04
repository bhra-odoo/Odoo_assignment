#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'stock_transport_settings',
    'description': '',
    'category': '',
    'summary': 'Transport Management System settings',
    'installable': True,
    'application': True,
    'depends': ['base', 'stock'],
    'license': 'OEEL-1',
    'version': '1.0',
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_view.xml'
    ],
}
