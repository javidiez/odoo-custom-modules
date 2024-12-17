from odoo import models, api, fields

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    document_ids = fields.One2many('partner.document','partner_id', string="Documents")