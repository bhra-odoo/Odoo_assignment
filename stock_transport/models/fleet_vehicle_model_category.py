#-*- coding: utf-8 -*-

from odoo import api, fields, models

class FleetVehicleModelCategory(models.Model):
    _name = 'fleet.vehicle.model.category'
    _inherit = 'fleet.vehicle.model.category'
    _description = 'Category of the model'
    _order = 'sequence asc, id asc'

    max_weight = fields.Float(string='Max weight(Kg)') 
    max_volume = fields.Float(string='Max volume(m\u00b3)')

    _sql_constraints = [
        ('check_max_weight_positive', 'CHECK(max_weight > 0)', 'Max Weight should be Greater than 0'),
        ('check_max_volume_positive', 'CHECK(max_volume > 0)', 'Max Volume should be Greater than 0')
    ]

    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight} Kg, {record.max_volume} m\u00b3)" 
