# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyecto2(models.Model):
#     _name = 'proyecto2.proyecto2'
#     _description = 'proyecto2.proyecto2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
