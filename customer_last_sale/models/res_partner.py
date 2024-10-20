# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    last_sale_order_date = fields.Datetime(string="Last sale order date", readonly=True)
    sale_order_id = fields.Many2one('sale.order', string="Sale order", readonly=True)
