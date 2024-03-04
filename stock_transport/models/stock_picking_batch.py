#-*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('batch.transfer.docks', string='Dock')
    vehical_id = fields.Many2one('fleet.vehicle', string='Vehical')
    vehical_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehical Category')
    batch_weight = fields.Float(string='Weight', compute='_compute_batch_weight', store=True)
    batch_volume = fields.Float(string='Volume', compute='_compute_batch_volume', store=True)
    
    @api.depends('picking_ids', 'vehical_category_id')
    def _compute_batch_volume(self):
        total_volume = sum(self.picking_ids.mapped('shipping_volume'))
        max_volume = self.vehical_category_id.max_volume if self.vehical_category_id else 0
        if self.vehical_category_id:
            self.batch_volume = total_volume * 100 / max_volume
        else:
            self.batch_volume = 0

    @api.depends('picking_ids', 'vehical_category_id')
    def _compute_batch_weight(self):
        total_weight = sum(self.picking_ids.mapped('shipping_weight'))
        max_weight = self.vehical_category_id.max_weight if self.vehical_category_id else 0
        if self.vehical_category_id:
            max_weight = self.vehical_category_id.max_weight
            self.batch_weight = total_weight * 100 / max_weight
        else:
            self.batch_weight = 0
