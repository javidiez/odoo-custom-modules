# -*- coding: utf-8 -*-
# from odoo import http


# class CalendarMeetingRoom(http.Controller):
#     @http.route('/calendar_meeting_room/calendar_meeting_room', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calendar_meeting_room/calendar_meeting_room/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('calendar_meeting_room.listing', {
#             'root': '/calendar_meeting_room/calendar_meeting_room',
#             'objects': http.request.env['calendar_meeting_room.calendar_meeting_room'].search([]),
#         })

#     @http.route('/calendar_meeting_room/calendar_meeting_room/objects/<model("calendar_meeting_room.calendar_meeting_room"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calendar_meeting_room.object', {
#             'object': obj
#         })

