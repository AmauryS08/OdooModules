from odoo import fields, models, api, _


class sale_edit(models.Model):
    _name = 'sale_edit.sale_edit'
    _description = 'Modification module sale'
    _inherit = 'account.move'

    name = fields.Char()

    def create(self, vals):
        if vals.get('oci_so_numerobi', _('New')) == _('New'):
            seq_date = None
            vals['oci_so_numerobi'] = self.env['ir.sequence'].next_by_code('sale_edit.numerobi.seq', sequence_date=seq_date) or _('N°BI')
        result = super(sale_edit, self).create(vals)
        return result
