from odoo import models, fields, api

class Editorial(models.Model):
    _name = "book.editorial"
    _description = "Book editorial table"
    
    name = fields.Many2one("res.partner", string="Name")
    street = fields.Char(related="name.street", string="Street")
    city = fields.Char(related="name.city", string="City")
    state = fields.Many2one(related="name.state_id", string="State")
    zip = fields.Char(related="name.zip", string="ZIP")
    country = fields.Many2one(related="name.country_id", string="Country")
    phone = fields.Char(related="name.phone", string="Phone")
    mobile = fields.Char(related="name.mobile", string="Mobile")
    book_id = fields.One2many("book","editorial", string="Book")
    description = fields.Text(string="Description")
