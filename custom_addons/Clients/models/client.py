from odoo import api, fields, models
from datetime import date


class Student(models.Model):
    _name = "client"
    _description = "Company client"

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    course = fields.Selection([('1', '1'), ('2', '2'), ('3', '3')], string="Course")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")

