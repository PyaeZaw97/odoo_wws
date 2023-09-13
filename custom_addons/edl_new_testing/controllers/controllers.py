# -*- coding: utf-8 -*-
# from odoo import http


# class EdlNewTesting(http.Controller):
#     @http.route('/edl_new_testing/edl_new_testing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edl_new_testing/edl_new_testing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edl_new_testing.listing', {
#             'root': '/edl_new_testing/edl_new_testing',
#             'objects': http.request.env['edl_new_testing.edl_new_testing'].search([]),
#         })

#     @http.route('/edl_new_testing/edl_new_testing/objects/<model("edl_new_testing.edl_new_testing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edl_new_testing.object', {
#             'object': obj
#         })
