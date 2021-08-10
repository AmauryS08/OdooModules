from odoo import fields, models, api


class oci_crm(models.Model):
    _inherit = "crm.lead"

    name = fields.Char()
