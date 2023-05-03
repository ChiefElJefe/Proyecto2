from odoo import models, fields, api, _

STATE_TYPE = [
    ('start', 'Start'),
    ('in_progress', 'In progress'),
    ('completed', 'Completed')
]

CATEGORY_TYPE = [
    ('programming', 'Programming'),
    ('design', 'Design'),
    ('art', 'Art')
]


class Developer(models.Model):
    _name = 'proyecto2.developer'
    _description = 'proyect2.developer'
    _sql_constraints = [
        ('check_deadline_after_start_date', 'CHECK (deadline >= start_date)', 'Deadline must be after start date!')
    ]

    def _default_stage(self):
        return self.env['proyecto2.stages'].search([], limit=1)

    @api.model
    def _expands_group_ids(self, stages, domain, order):
        return self.env['proyecto2.stages'].search([], order=order)

    name = fields.Char(string="Task", required=True)
    description = fields.Text(string="Description", required=True)
    user_id = fields.Many2one('res.users', string="Assigned to", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.context_today)
    kanban_state = fields.Selection(STATE_TYPE, string="Status", default='start')
    type = fields.Selection(CATEGORY_TYPE, string="Type", required=True)
    deadline = fields.Date(string="Deadline")
    stage_id = fields.Many2one('proyecto2.stages', default=_default_stage, group_expand='_expands_group_ids')
