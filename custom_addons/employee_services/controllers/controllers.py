# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeServices(http.Controller):
#     @http.route('/employee_services/employee_services', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_services/employee_services/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_services.listing', {
#             'root': '/employee_services/employee_services',
#             'objects': http.request.env['employee_services.employee_services'].search([]),
#         })

#     @http.route('/employee_services/employee_services/objects/<model("employee_services.employee_services"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_services.object', {
#             'object': obj
#         })
