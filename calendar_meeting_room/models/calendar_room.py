# -*- coding: utf-8 -*-

from odoo import models, fields


class CalendarRoom(models.Model):
    _inherit = "calendar.event"

    room = fields.Many2one("calendar.meeting.room", string="Room")