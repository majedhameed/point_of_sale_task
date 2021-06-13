# -*- coding: utf-8 -*-
# from odoo import http


# class PonintOfSaleTax(http.Controller):
#     @http.route('/ponint_of_sale_tax/ponint_of_sale_tax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ponint_of_sale_tax/ponint_of_sale_tax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ponint_of_sale_tax.listing', {
#             'root': '/ponint_of_sale_tax/ponint_of_sale_tax',
#             'objects': http.request.env['ponint_of_sale_tax.ponint_of_sale_tax'].search([]),
#         })

#     @http.route('/ponint_of_sale_tax/ponint_of_sale_tax/objects/<model("ponint_of_sale_tax.ponint_of_sale_tax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ponint_of_sale_tax.object', {
#             'object': obj
#         })
