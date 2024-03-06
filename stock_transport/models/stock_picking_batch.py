#-*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('batch.transfer.docks', string='Dock')
    vehical_id = fields.Many2one('fleet.vehicle', string='Vehical')
    vehical_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehical Category')
    weight_progressbar = fields.Float(compute='_compute_weight_progressbar', store=True)
    volume_progressbar = fields.Float(compute='_compute_volume_progressbar', store=True)
    weight = fields.Char(string='Weight', compute='_compute_weight_and_volume', store=True)
    volume = fields.Char(string='Volume', compute='_compute_weight_and_volume', store=True)
    transfer_count = fields.Integer(string = 'Transfer', compute='_compute_transfer_and_lines', store=True)
    move_line_count = fields.Integer(string = 'Lines', compute='_compute_transfer_and_lines', store=True)
    
    @api.depends('picking_ids', 'vehical_category_id')
    def _compute_volume_progressbar(self):
        for record in self:
            total_volume = sum(record.picking_ids.mapped('shipping_volume'))
            max_volume = record.vehical_category_id.max_volume
            record.volume_progressbar = total_volume * 100 / max_volume if record.vehical_category_id and total_volume > 0 else 0

    @api.depends('picking_ids', 'vehical_category_id')
    def _compute_weight_progressbar(self):
        for record in self:
            total_weight = sum(record.picking_ids.mapped('shipping_weight'))
            max_weight = record.vehical_category_id.max_weight
            record.weight_progressbar = total_weight * 100 / max_weight if record.vehical_category_id and total_weight > 0 else 0

    @api.depends('weight_progressbar', 'volume_progressbar', 'vehical_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"({record.weight} Kg, {record.volume} m\u00b3), {record.vehical_id.driver_id.name}" 

    @api.depends('picking_ids', 'move_line_ids')
    def _compute_transfer_and_lines(self):
        self.write(
            {
                'transfer_count': len(self.picking_ids) if self.picking_ids else 0,
                'move_line_count': len(self.move_line_ids) if self.picking_ids else 0
            }
        )

    @api.depends('weight_progressbar', 'volume_progressbar')
    def _compute_weight_and_volume(self):
        for record in self:    
            record.weight = f"{str(round(record.weight_progressbar / 100, 2))} Kg"
            record.volume = f"{str(round(record.volume_progressbar / 100, 2))} m\u00b3"
