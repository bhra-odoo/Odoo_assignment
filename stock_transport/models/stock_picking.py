#-*- coding: utf-8 -*-

from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    shipping_volume = fields.Float(string='Volume',compute='_compute_shipping_volume_weight', default=0.0)
    shipping_weight = fields.Float(string='Shipping Weight', compute='_compute_shipping_volume_weight', default=0.0)

    @api.depends('move_ids')
    def _compute_shipping_volume_weight(self):
        for record in self:
            for info in record.move_ids:
                record.shipping_volume += info.product_id.volume * info.quantity
                record.shipping_weight += info.product_id.weight * info.quantity
