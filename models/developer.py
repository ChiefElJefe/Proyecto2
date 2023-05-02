from odoo import models, fields, api, _
from datetime import date


class Developer(models.Model):
    _name = 'proyecto2.developer'
    _description = 'proyect2.developer'
    _sql_constraints = [
        ('check_deadline_after_start_date', 'CHECK (deadline >= start_date)', 'Deadline must be after start date!')
    ]

    name = fields.Char(string="Task", required=True)
    description = fields.Text(string="Description", required=True)
    user_id = fields.Many2one('res.users', string="Assigned to", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.context_today)
    deadline = fields.Date(string="Deadline")
