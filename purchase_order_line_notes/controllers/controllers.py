# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderLineNotes(http.Controller):
#     @http.route('/purchase_order_line_notes/purchase_order_line_notes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_line_notes/purchase_order_line_notes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_line_notes.listing', {
#             'root': '/purchase_order_line_notes/purchase_order_line_notes',
#             'objects': http.request.env['purchase_order_line_notes.purchase_order_line_notes'].search([]),
#         })

#     @http.route('/purchase_order_line_notes/purchase_order_line_notes/objects/<model("purchase_order_line_notes.purchase_order_line_notes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_line_notes.object', {
#             'object': obj
#         })

