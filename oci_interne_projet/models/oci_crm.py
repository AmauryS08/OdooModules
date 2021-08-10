from odoo import fields, models, api


class oci_crm(models.Model):
    _inherit = "crm.lead"

    oci_crm_demonstrateur = fields.Many2one('res.users', string="Démonstrateur")
    oci_crm_chefprojet = fields.Many2one('res.users', string="Chef de projet")
    oci_crm_consultant = fields.Many2many('res.users', string="Consultant(s)")

    oci_crm_logiciel = fields.Many2many('crm.tag', 'crm_tag_rel', 'lead_id', 'tag_id', string="Logiciel(s)")
