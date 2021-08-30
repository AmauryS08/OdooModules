import random

from odoo import fields, models, api, _


class facture(models.Model):
    _name = 'customsales.facture'
    _description = 'model facture'

    name = fields.Char(String = "Facture", readonly="1")
    client = fields.Many2one('res.partner', String = "Client", Requiered=True)
    reference_paiement = fields.Char(String = "Référence paiement", Requiered=True)
    date_facturation = fields.Date(String = "Date facturation", Requiered=True)
    data_echeance = fields.Date(String = "Date d'échéance")

    prix_total_ht = fields.Float("Prix total HT", compute='_compute_total', readonly="1")
    prix_total_ttc = fields.Float("Prix total TTC", compute='_compute_total', readonly="1")
    prix_tax = fields.Float("Taxes", compute='_compute_total', readonly='1')

    reference_facture = fields.Char(string="Id facture", compute="_reference_facture")

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

    state = fields.Selection([
        ('paye', 'Payée'),
        ('enattentepaye', 'En attente de paiement'),
    ], string="Etat de la facture:", invisible=True, default="enattentepaye")

    facture_article_id = fields.One2many('customsales.facture.article', 'facture_parent_id', string="Child ID")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            vals['name'] = self.env['ir.sequence'].next_by_code('facture.name.seq', sequence_date=seq_date) or _('Facture')
        result = super(facture, self).create(vals)
        return result

    def state_paye(self):
        self.write({'state': 'paye'})

    def state_enattentepaye(self):
        self.write({'state': 'enattentepaye'})

    def _reference_facture(self):
        for record in self:
            record.reference_facture = str(random.randint(1,99999))

    @api.depends('facture_article_id.prix_soustotal', 'facture_article_id.tax')
    def _compute_total(self):
        for order in self:
            totalht = 0
            totalttc = 0
            totaltax = 0
            for line in order.facture_article_id:
                totalht += line.prix_soustotal
                totalttc += line.prix_soustotal + line.prix_soustotal * (line.tax.amount / 100)
                totaltax += line.prix_soustotal * (line.tax.amount / 100)
            order.update({
                'prix_total_ht': totalht,
                'prix_total_ttc': totalttc,
                'prix_tax': totaltax,
            })



class factureArticles(models.Model):
    _name = 'customsales.facture.article'
    _description = "Sous menu facture pour article"

    article = fields.Many2one('product.product', String = "Article")
    label = fields.Char(String = "Label")
    quantity = fields.Float(String = "Quantité")
    prix_unite = fields.Float(String = "Prix")
    tax = fields.Many2many('account.tax',String = "Tax")
    prix_soustotal = fields.Float(String = "Prix Total HT", readonly=True, compute='_computeVar_final')


    @api.depends('prix_soustotal', 'prix_unite', 'quantity')
    def _computeVar_final(self):
        for order in self:
            for line in order:
                line.prix_soustotal = line.prix_unite * line.quantity


    facture_parent_id = fields.Many2one('customsales.facture', String="Informations Personnelles")



