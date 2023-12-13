# -*- coding: utf-8 -*-
# from odoo import http


# class Ab-travel-umroh(http.Controller):
#     @http.route('/ab-travel-umroh/ab-travel-umroh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ab-travel-umroh/ab-travel-umroh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ab-travel-umroh.listing', {
#             'root': '/ab-travel-umroh/ab-travel-umroh',
#             'objects': http.request.env['ab-travel-umroh.ab-travel-umroh'].search([]),
#         })

#     @http.route('/ab-travel-umroh/ab-travel-umroh/objects/<model("ab-travel-umroh.ab-travel-umroh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ab-travel-umroh.object', {
#             'object': obj
#         })
