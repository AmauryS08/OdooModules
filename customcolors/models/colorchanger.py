from odoo import fields, models, api


class colorchanger(models.Model):
    _name = 'customcolors.colorchanger'
    _description = 'Changement couleurs menu'

    name = fields.Char()