# -*- coding: utf-8 -*-
# from odoo import http


# class PerritosCalientes(http.Controller):
#     @http.route('/perritos_calientes/perritos_calientes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/perritos_calientes/perritos_calientes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('perritos_calientes.listing', {
#             'root': '/perritos_calientes/perritos_calientes',
#             'objects': http.request.env['perritos_calientes.perritos_calientes'].search([]),
#         })

#     @http.route('/perritos_calientes/perritos_calientes/objects/<model("perritos_calientes.perritos_calientes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('perritos_calientes.object', {
#             'object': obj
#         })

