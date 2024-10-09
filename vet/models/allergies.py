from odoo import models, fields, api

class Allergie(models.Model):
    _name = "animal.allergie"
    _description = "Animal allergies table"

    name = fields.Char(string="Allergies", required=True)
    description = fields.Text(string="Description")
