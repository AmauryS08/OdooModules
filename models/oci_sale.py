from odoo import fields, models, api


class oci_sale(models.Model):
    _inherit = "sale.order"
