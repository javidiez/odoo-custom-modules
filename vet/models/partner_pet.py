from odoo import fields, models, api

class Pet(models.Model):
    _inherit = "res.partner"

    pet = fields.Many2many("animal", string="Pet")
