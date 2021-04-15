from odoo import fields, models, api


class testrelationa(models.Model):
    _name = 'journamod.testrelationa'
    _description = 'test relation A'

    b_ids = fields.Many2many('journamod.testrelationb', 'a_b_relation', 'a_id', 'b_id', 'Nom A')
    name = fields.Char()

class testrelationb(models.Model):
    _name = 'journamod.testrelationb'
    _description = 'test relation B'

    a_ids = fields.Many2many('journamod.testrelationa', 'a_b_relation', 'b_id', 'a_id', 'Nom B')
    name = fields.Char()
