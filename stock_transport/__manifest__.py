#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'stock_transport',
    'description': '',
    'category': '',
    'summary': 'Transport Management System',
    'installable': True,
    'application': True,
    'depends': ['base', 'stock_picking_batch', 'fleet'],
    'license': 'OEEL-1',
    'version': '1.0',
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_view.xml',
        'views/stock_picking_batch_view.xml',
        'views/stock_picking_view.xml',
    ],
}
