from odoo import fields, models, api, _


class facture(models.Model):
    _name = 'customsales.facture'
    _description = 'model facture'


    name = fields.Char(String = "Nom", Requiered=True)
    client = fields.Many2one('res.partner', String = "Client", Requiered=True)
    reference_paiement = fields.Char(String = "Référence paiement", Requiered=True)
    date_facturation = fields.Date(String = "Date facturation", Requiered=True)
    data_echeance = fields.Date(String = "Date d'échéance")

    # Sous menu Autres informations
    reference_client = fields.Char(String="Référence client")
    vendeur = fields.Many2one('res.users', String="Vendeur")
    equipe_commerciale = fields.Many2one('crm.team', String="Equipe commerciale")
    compte_bank_ref = fields.Many2one('res.partner.bank', String="Compte bancaire destinataire")

    societe = fields.Many2one('res.company', String="Société")
    incoterm = fields.Many2one('account.incoterms', String="Incoterm")
    pos_fiscal = fields.Many2one('account.fiscal.position', String="Position fiscale")

    campagne = fields.Many2one('utm.campaign', String="Campagne")
    moyen = fields.Many2one('utm.medium', String="Moyen")
    source = fields.Many2one('utm.source', String="Source")

    facture_article_id = fields.One2many('customsales.facture.article', 'facture_parent_id', string="Child ID")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')
        result = super(facture, self).create(vals)
        return result


class factureArticles(models.Model):
    _name = 'customsales.facture.article'
    _description = "Sous menu facture pour article"

    article = fields.Many2one('product.product', String = "Article")
    label = fields.Char(String = "Label")
    quantity = fields.Float(String = "Quantité")
    prix = fields.Float(String = "Prix")
    tax = fields.Many2many('account.tax',String = "Tax")
    # prixtot = fields.Monetary(String = "Prix Total", type="mon")

    facture_parent_id = fields.Many2one('customsales.facture', String="Informations Personnelles")



