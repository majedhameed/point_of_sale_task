# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ponint_of_sale_tax(models.Model):
#     _name = 'ponint_of_sale_tax.ponint_of_sale_tax'
#     _description = 'ponint_of_sale_tax.ponint_of_sale_tax'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
