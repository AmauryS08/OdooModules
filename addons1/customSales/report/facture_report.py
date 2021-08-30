from odoo import fields, models, api


# class factureReport(models.Model):
#     _name = 'customsales.facture.report'
#     _description = 'Description'
#
#     name = fields.Char("Référence d'ordre", readonly = True)
#     date = fields.Datetime("Date de facture", readonly = True)
#     client = fields.Many2one('res.partner', String = "Client", readonly = True)
#     reference_paiement = fields.Char(String = "Référence paiement", readonly = True)
#     date_facturation = fields.Date(String = "Date facturation", readonly = True)
#     data_echeance = fields.Date(String = "Date d'échéance", readonly = True)
#     reference_client = fields.Char(String="Référence client", readonly = True)
#     vendeur = fields.Many2one('res.users', String="Vendeur", readonly = True)
#     equipe_commerciale = fields.Many2one('crm.team', String="Equipe commerciale", readonly = True)
#     compte_bank_ref = fields.Many2one('res.partner.bank', String="Compte bancaire destinataire", readonly = True)
#     societe = fields.Many2one('res.company', String="Société", readonly = True)
#     incoterm = fields.Many2one('account.incoterms', String="Incoterm", readonly = True)
#     pos_fiscal = fields.Many2one('account.fiscal.position', String="Position fiscale", readonly = True)
#     campagne = fields.Many2one('utm.campaign', String="Campagne", readonly = True)
#     moyen = fields.Many2one('utm.medium', String="Moyen", readonly = True)
#     source = fields.Many2one('utm.source', String="Source", readonly = True)
#
#     def print_report(self):
#         data = {
#             'from_date': self.from_date,
#             'to_date': self.to_date
#         }
#         return self.env.ref('customSales.facture').report_action(None, data=data)

class print(models.AbstractModel):
    _name = 'facture.print'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['customsales.facture'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'customsales.facture',
            'docs': docs,
            'data': data,
            'get_something': self.get_something,
        }

    def get_something(self):
        return 5
