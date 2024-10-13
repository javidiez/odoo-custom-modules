from odoo import models, fields

class Subjects(models.Model):
    _name = 'school.subjects'
    _description = "School subjects"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    active = fields.Boolean(string="Activo", default=True)
    carreer = fields.Many2many("school.carreers", string="Carrera")
