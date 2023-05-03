from odoo import models, fields, api, _


class Developer(models.Model):
    _name = 'proyecto2.stages'
    _description = 'proyect2.stages'

    name = fields.Char(string="Stage", required=True)
    developer_ids = fields.One2many('proyecto2.developer', 'stage_id')
