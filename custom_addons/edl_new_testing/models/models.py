# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class edl_new_testing(models.Model):
#     _name = 'edl_new_testing.edl_new_testing'
#     _description = 'edl_new_testing.edl_new_testing'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
