from odoo import models, fields, api

class Surgerie(models.Model):
    _name = "animal.surgerie"
    _description = "Animal surgeries table"

    surgeries = fields.Char(string="Surgerie", required=True)
    observations = fields.Text(string="Observations")
