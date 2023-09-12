# -*- coding: utf-8 -*-
# from odoo import http


# class HrTest(http.Controller):
#     @http.route('/hr_test/hr_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_test/hr_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_test.listing', {
#             'root': '/hr_test/hr_test',
#             'objects': http.request.env['hr_test.hr_test'].search([]),
#         })

#     @http.route('/hr_test/hr_test/objects/<model("hr_test.hr_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_test.object', {
#             'object': obj
#         })
