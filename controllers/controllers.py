# -*- coding: utf-8 -*-
# from odoo import http


# class Proyecto2(http.Controller):
#     @http.route('/proyecto2/proyecto2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto2/proyecto2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto2.listing', {
#             'root': '/proyecto2/proyecto2',
#             'objects': http.request.env['proyecto2.proyecto2'].search([]),
#         })

#     @http.route('/proyecto2/proyecto2/objects/<model("proyecto2.proyecto2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto2.object', {
#             'object': obj
#         })
