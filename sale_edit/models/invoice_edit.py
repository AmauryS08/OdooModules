from odoo import fields, models, api

class invoice_edit(models.Model):
    _inherit = 'account.move'

    # fields.Datetime(string="date paiement", related='order_date_id.date_order')
    oci_ac_numerobi = fields.Char(string="N° BI")
    oci_ac_techniciens = fields.Many2many('hr.employee', string="Technicien(s)")
    oci_ac_dateintervention = fields.Date(string="Date d'Intervention")
    oci_ac_typeintervention = fields.Selection(string="Type Intervention")


class invoice_create(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        res = super()._prepare_invoice_values(order, name, amount, so_line)
        res['oci_ac_numerobi'] = order.x_studio_oci_so_numerobi
        res['oci_ac_techniciens'] = order.x_studio_techniciens
        res['oci_ac_dateintervention'] = order.x_studio_oci_so_dateintervention
        res['oci_ac_typeintervention'] = order.x_studio_oci_so_typeintervention
        return res


class invoice_add(models.TransientModel):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        if self.x_studio_oci_so_numerobi:
            res['oci_ac_numerobi'] = self.x_studio_oci_so_numerobi
        if self.x_studio_techniciens:
            res['oci_ac_techniciens'] = self.x_studio_techniciens
        if self.x_studio_oci_so_dateintervention:
            res['oci_ac_dateintervention'] = self.x_studio_oci_so_dateintervention
        if self.x_studio_oci_so_typeintervention:
            res['oci_ac_typeintervention'] = self.x_studio_oci_so_typeintervention
        return res

