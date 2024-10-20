from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            order.partner_id.write({
                'last_sale_order_date': fields.Datetime.now(),  # Cambiado a Datetime para guardar fecha y hora
                'sale_order_id': order.id
        })
        return res
