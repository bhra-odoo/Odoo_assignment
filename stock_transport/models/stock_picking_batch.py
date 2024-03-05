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
    transfer_count = fields.Integer(string = "Transfer", compute='_compute_transfer_and_lines', store=True)
    move_line_count = fields.Integer(string = "Lines", compute='_compute_transfer_and_lines', store=True)
    
    @api.depends('picking_ids', 'vehical_category_id')
    def _compute_batch_volume(self):
        total_volume = sum(self.picking_ids.mapped('shipping_volume'))
        max_volume = self.vehical_category_id.max_volume
        self.batch_volume = total_volume * 100 / max_volume if self.vehical_category_id and total_volume > 0 else 0

    @api.depends('picking_ids', 'vehical_category_id')
    def _compute_batch_weight(self):
        total_weight = sum(self.picking_ids.mapped('shipping_weight'))
        max_weight = self.vehical_category_id.max_weight
        self.batch_weight = total_weight * 100 / max_weight if self.vehical_category_id and total_weight > 0 else 0

    @api.depends('batch_weight', 'batch_volume', 'vehical_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"({record.batch_weight} Kg, {record.batch_volume} m\u00b3), {record.vehical_id.driver_id.name}" 

    @api.depends('picking_ids', 'move_line_ids')
    def _compute_transfer_and_lines(self):
        self.write(
            {
                'transfer_count': len(self.picking_ids) if self.picking_ids else 0,
                'move_line_count': len(self.move_line_ids) if self.picking_ids else 0
            }
        )
