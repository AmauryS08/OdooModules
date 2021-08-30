from odoo import fields, models, api


class oci_project(models.Model):
    _inherit = "project.task"

    oci_project_infodispo = fields.Char(string="Info")
