from odoo import fields, models, api


class sale_edit(models.Model):
    _name = 'sale_edit.sale_edit'
    _description = 'Modification module sale'
    _inherit = 'account.move'

    name = fields.Char()
