from odoo import fields, models, api


class invoice_edit(models.Model):
    _inherit = 'account.move'

    name_test = fields.Char(string="TEST:")
    oci_facture_informations = fields.Many2one('sale.order', 'OCI facture information')
    #fields.Datetime(string="date paiement", related='order_date_id.date_order')
    oci_ac_numerobi = fields.Char(string="N° BI", related='oci_facture_informations.x_studio_oci_so_numerobi')
    oci_ac_techniciens = fields.Many2many(string="Technicien(s)", related='oci_facture_informations.x_studio_techniciens')
    oci_ac_dateintervention = fields.Date(string="Date d'Intervention", related='oci_facture_informations.x_studio_oci_so_dateintervention')
    oci_ac_typeintervention = fields.Selection(string="Type Intervention", related='oci_facture_informations.x_studio_oci_so_typeintervention')
