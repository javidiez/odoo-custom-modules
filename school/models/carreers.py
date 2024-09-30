from odoo import models, fields

class Carreers(models.Model):
    _name = 'school.carreers'
    _description = "School carreers"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    active = fields.Boolean(string="Activo", default=True)
    subjects = fields.Many2many('school.subjects')
