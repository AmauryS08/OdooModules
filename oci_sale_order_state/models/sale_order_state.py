from odoo import fields, models, api
from odoo.osv import expression



class sale_state_edit(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Draft Quotation'),
        ('sent', 'Quotation Sent'),
        ('commande_confirmee', 'Commande confirmée'),
        ('sale', 'Sales Order'),
        ('done', 'Sales Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True)

    def actioncommande_confirmee(self):
        self.state = 'commande_confirmee'