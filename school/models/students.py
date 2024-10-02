# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "school.student"
    _description = "Tabla de estudiantes"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order ="name asc"

    partner_id = fields.Many2one('res.partner', string="Nombre", required=True)
    name = fields.Char(related='partner_id.name', string="Nombre", store=True)
    alias = fields.Char(related='partner_id.alias', string="Apodo", store=True, readonly=False)
    image = fields.Binary(related='partner_id.image_1920', string="Imagen", store=True)
    phone = fields.Char(related='partner_id.phone', string="Teléfono", store=True)
    mobile = fields.Char(related='partner_id.mobile', string="Móvil", store=True)
    street = fields.Char(related='partner_id.street', string="Dirección", store=True)
    city = fields.Char(related='partner_id.city', string="Ciudad", store=True)
    country_id= fields.Many2one(related='partner_id.country_id', string="País", store=True)
    state_id= fields.Many2one(related='partner_id.state_id', string="Provincia", store=True)
    email = fields.Char(related='partner_id.email', string="Email", store=True)
    zip = fields.Char(related='partner_id.zip', string="C.P.", store=True)
    tuition = fields.Char(string="Matrícula", copy=False, tracking=20, required=True)
    birthdate = fields.Date(string="Fecha de nacimiento")
    inscription_date = fields.Date(string="Fecha de inscripción")
    carreers = fields.Many2one('school.carreers',string="Carrera", required=True)
    subjects = fields.Many2many('school.subjects')
    course = fields.Char(string="Curso")
    tag = fields.Many2many('school.tag', string="Etiquetas")
    teacher = fields.Many2one('res.partner', string="Profesor")
    teacher_assistant = fields.Many2one('res.partner', string="Teacher assistant")
    modality = fields.Selection([
                                        ('virtual', 'Virtual'),
                                        ('insitu', 'Presencial'),
                                        ], string="Modalidad", default="virtual")
    estimated_graduate_date = fields.Date(string="Fecha estimada de gradución")
    beca = fields.Char(string="Beca")
    final_project = fields.Char(string="Proyecto final")
    active = fields.Boolean(string="Activo", default=True)

    state = fields.Selection([
        ('draft', 'No iniciado'),
        ('ongoing', 'Cursando'),
        ('done', 'Finalizado'),
        ('abandoned', 'Abandonado'),
        ('expelled', 'Expulsado'),
    ], string='Status', default='draft', tracking=20)

    def action_ongoing(self):
        self.state = "ongoing"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_abandoned(self):
        self.state = "abandoned"

    def action_expelled(self):
        self.state = "expelled"

    # @api.depends('alias')
    # def _inverse_alias(self):
    #     for student in self:
    #         if student.partner_id:
    #             student.partner_id.alias = student.alias

    # @api.onchange('alias')
    # def _onchange_alias(self):
    #     for record in self:
    #         if record.alias and len(record.alias) > 7:
    #             return {
    #                 'warning': {
    #                     'title': _("Mensaje"),
    #                     'message': _('Se recomienda que el apodo sea corto')
    #                 }
    #             }
                
    @api.constrains('tuition')
    def _check_unique_tuition(self):
        for record in self:
            if self.search_count([('tuition','=', record.tuition), ('id', '!=', record.id)]) > 0:
                raise ValidationError('La matrícula debe ser única')
