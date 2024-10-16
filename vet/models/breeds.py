from odoo import models, fields, api

class Breed(models.Model):
    _name = "animal.breed"
    _description = "Animal breeds table"

    name = fields.Char(string="Breed", required=True)
    specie = fields.Many2one("animal.specie", string="Specie")
    description = fields.Text(string="Description")
