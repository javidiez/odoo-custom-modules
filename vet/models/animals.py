from odoo import models, fields, api

class Animal(models.Model):
    _name = "animal"
    _description = "Animals table"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    identification = fields.Char(string="ID")
    name = fields.Char(string="Name", required=True)
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Sex", default="male")
    birthdate = fields.Date(string="Birthdate")
    photo = fields.Binary(string="Photo")
    breed = fields.Many2one("animal.breed", string="Breed")
    species = fields.Many2one("animal.specie", string="Specie", required=True)
    owner = fields.Many2one('res.partner', string="Owner", required=True)
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ], string="Size", default='small')
    medicines = fields.Many2many("animal.medicine", string="Medicines", relation="animal_medicine_rel")
    vaccines = fields.Many2many("animal.vaccine", string="Vaccines", relation="animal_vaccine_rel")
    diseases = fields.Many2many("animal.disease", string="Diseases", relation="animal_disease_rel")
    allergies = fields.Many2many("animal.allergy", string="Allergies", relation="animal_allergy_rel")
    surgeries = fields.Many2many("animal.surgery", string="Surgeries", relation="animal_surgery_rel")
    visits = fields.Many2many("animal.visit", string="Visits")
    visit_date = fields.Date(related="visits.date", string="Visits")
    visit_reference = fields.Char(related="visits.sequence", string="Visits")
    active = fields.Boolean(string="Active", default=True)
    tags = fields.Many2many("animal.tag", string="Tags", relation="animal_tag_rel")
    insurance = fields.Many2one("animal.insurance", string="Insurance", relation="animal_insurance_rel")
