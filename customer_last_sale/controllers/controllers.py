# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerLastSale(http.Controller):
#     @http.route('/customer_last_sale/customer_last_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_last_sale/customer_last_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_last_sale.listing', {
#             'root': '/customer_last_sale/customer_last_sale',
#             'objects': http.request.env['customer_last_sale.customer_last_sale'].search([]),
#         })

#     @http.route('/customer_last_sale/customer_last_sale/objects/<model("customer_last_sale.customer_last_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_last_sale.object', {
#             'object': obj
#         })

