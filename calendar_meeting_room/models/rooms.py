# -*- coding: utf-8 -*-

from odoo import models, fields


class Room(models.Model):
    _name = 'calendar.meeting.room'
    _description = 'Calendar meeting room'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(string="Capacity")
    location= fields.Char(string="Location")
