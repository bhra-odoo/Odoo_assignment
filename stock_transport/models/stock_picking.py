#-*- coding: utf-8 -*-

from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    shipping_volume = fields.Float(string='Volume',compute='_compute_shipping_volume_weight', default=0.0)
    shipping_weight = fields.Float(string='Shipping Weight', compute='_compute_shipping_volume_weight', default=0.0)

    @api.depends('move_ids')
    def _compute_shipping_volume_weight(self):
        for record in self:
            for volume in record.move_ids:
                    record.shipping_volume += volume.product_id.volume * volume.quantity
                    record.shipping_weight += volume.product_id.weight * volume.quantity
