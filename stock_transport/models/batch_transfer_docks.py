#-*- coding: utf-8 -*-

from odoo import api, fields, models

class BatchTransferDocks(models.Model):
    _name = 'batch.transfer.docks'
    _description = 'Batch Transfer Docks'

    name = fields.Char('Dock Name')