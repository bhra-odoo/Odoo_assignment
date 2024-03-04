#-*- coding: utf-8 -*-

from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    shipping_volume = fields.Float(string='Volume',compute='_compute_shipping_volume')
    shipping_weight = fields.Float(string='Sheeping Weight', compute='_compute_shipping_weight')

    @api.depends('move_line_ids_without_package')
    def _compute_shipping_volume(self):
        for record in self:
            record.shipping_volume = 0
            for volume in record.move_line_ids_without_package:
                    record.shipping_volume += volume.product_id.volume * volume.quantity

    @api.depends('move_line_ids_without_package')
    def _compute_shipping_weight(self):
        for record in self:
            record.shipping_weight = 0
            for volume in record.move_line_ids_without_package:
                    record.shipping_weight += volume.product_id.weight * volume.quantity
