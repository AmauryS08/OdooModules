from odoo import fields, models, api


class fsm_edit(models.Model):
    _inherit = "project.task"

    oci_fsm_numerobi = fields.Char(string="N° BI")
    oci_fsm_numerobiexterne = fields.Char(string="N° BI externe")
    oci_fsm_techniciens = fields.Many2many('hr.employee', string="Technicien(s)")
    oci_fsm_dateintervention = fields.Date(string="Date d'Intervention")
    oci_fsm_typeintervention = fields.Selection(string="Type Intervention")
    oci_fsm_representant = fields.Many2one(string="Représentant")

    def action_fsm_create_quotation(self):
        res = super().action_fsm_create_quotation()
        res.update({
            'oci_so_numerobi': self.oci_fsm_numerobi,
            'oci_so_numerobiexterne': self.oci_fsm_numerobiexterne,
            'oci_so_techniciens': self.oci_fsm_techniciens,
            'oci_so_dateintervention': self.oci_fsm_dateintervention,
            'oci_so_typeintervention': self.oci_fsm_typeintervention,
            'oci_so_representant': self.oci_fsm_representant,
            # 'context': {
            #     'default_numerobi': self.oci_fsm_numerobi
            # }
        })
        return res