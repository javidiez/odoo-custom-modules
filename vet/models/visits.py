from odoo import fields, models, api

class Visit(models.Model):
    _name = "animal.visit"
    _description = "Animals visits table"

    date = fields.Date(string="Visit date", required=True)
    animal = fields.Many2one("animal", string="Patiente", required=True)
    owner = fields.Many2one("res.partner", string="Owner", required=True)
    reason = fields.Text(string="Reason")
    suggested_treatment = fields.Text(string="Suggested treatment")
    observations = fields.Text(string="Observations")
