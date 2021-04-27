from odoo import fields, models, api


class invoice_edit(models.Model):
    _inherit = 'account.move'

    oci_ac_numerobi = fields.Char(string="N° BI")
    oci_ac_techniciens = fields.Many2many(string="Technicien(s)")
    oci_ac_dateintervention = fields.Date(string="Date d'Intervention")
    oci_ac_typeintervention = fields.Selection(string="Type Intervention")


class invoice_create(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        res = super()._prepare_invoice_values(order, name, amount, so_line)
        if order.x_studio_oci_so_numerobi:
            res['oci_ac_numerobi'] = order.x_studio_oci_so_numerobi
        if order.x_studio_techniciens:
            res['oci_ac_techniciens'] = order.x_studio_techniciens
        if order.x_studio_oci_so_dateintervention:
            res['oci_ac_dateintervention'] = order.x_studio_oci_so_dateintervention
        if order.x_studio_oci_so_typeintervention:
            res['oci_ac_typeintervention'] = order.x_studio_oci_so_typeintervention
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


