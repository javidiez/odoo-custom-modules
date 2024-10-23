from odoo import fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    note = fields.Text(string="Notes")
