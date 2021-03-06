from odoo import fields, models, api
class invoice_edit(models.Model):
    _inherit = 'account.move'
    # fields.Datetime(string="date paiement", related='order_date_id.date_order')
    oci_ac_numerobi = fields.Char(string="N° BI")
    oci_ac_techniciens = fields.Many2many('hr.employee', string="Technicien(s)")
    oci_ac_dateintervention = fields.Date(string="Date d'Intervention")
    oci_ac_typeintervention = fields.Selection([('DEPANNAGE', 'DEPANNAGE'), ('SOUS GARANTIE', 'SOUS GARANTIE'), ('INSTALLATION NEUVE', 'INSTALLATION NEUVE'), ('INSTALLATION OCCASION', 'INSTALLATION OCCASION'), ('LIVRAISON', 'LIVRAISON'), ('MAINTENANCE', 'MAINTENANCE'), ('MISE EN SERVICE', 'MISE EN SERVICE'), ('SAV', 'SAV')],string="Type Intervention")

class invoice_create(models.TransientModel):
    _inherit = "sale.advance.payment.inv"
    def _prepare_invoice_values(self, order, name, amount, so_line):
        res = super()._prepare_invoice_values(order, name, amount, so_line)
        res['oci_ac_numerobi'] = order.x_studio_oci_so_numerobi
        res['oci_ac_techniciens'] = order.x_studio_techniciens
        res['oci_ac_dateintervention'] = order.x_studio_oci_so_dateintervention
        res['oci_ac_typeintervention'] = order.x_studio_oci_so_typeintervention
        return res

class invoice_add(models.Model):
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

    # def _prepare_invoice_values(self, order, name, amount, so_line):
    #     invoice_vals = {
    #         'ref': order.client_order_ref,
    #         'move_type': 'out_invoice',
    #         'invoice_origin': order.name,
    #         'invoice_user_id': order.user_id.id,
    #         'narration': order.note,
    #         'partner_id': order.partner_invoice_id.id,
    #         'fiscal_position_id': (order.fiscal_position_id or order.fiscal_position_id.get_fiscal_position(order.partner_id.id)).id,
    #         'partner_shipping_id': order.partner_shipping_id.id,
    #         'currency_id': order.pricelist_id.currency_id.id,
    #         'payment_reference': order.reference,
    #         'invoice_payment_term_id': order.payment_term_id.id,
    #         'partner_bank_id': order.company_id.partner_id.bank_ids[:1].id,
    #         'team_id': order.team_id.id,
    #         'campaign_id': order.campaign_id.id,
    #         'medium_id': order.medium_id.id,
    #         'source_id': order.source_id.id,
    #         'invoice_line_ids': [(0, 0, {
    #             'name': name,
    #             'price_unit': amount,
    #             'quantity': 1.0,
    #             'product_id': self.product_id.id,
    #             'product_uom_id': so_line.product_uom.id,
    #             'tax_ids': [(6, 0, so_line.tax_id.ids)],
    #             'sale_line_ids': [(6, 0, [so_line.id])],
    #             'analytic_tag_ids': [(6, 0, so_line.analytic_tag_ids.ids)],
    #             'analytic_account_id': order.analytic_account_id.id or False,
    #         })],
    #     }
    #
    #     return invoice_vals


