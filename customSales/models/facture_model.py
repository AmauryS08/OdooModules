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
    create_date = fields.Date(String = "Date de création")
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


class factureArticles(models.Model):
    _name = 'customsales.facture.article'
    _description = "Sous menu facture pour article"

    article = fields.Many2one('product.product', String = "Article")
    label = fields.Char(String = "Label")
    quantity = fields.Float(String = "Quantité")
    prix = fields.Float(String = "Prix")
    tax = fields.Many2many('account.tax',String = "Tax")
    prixtot_ht = fields.Float(String = "Prix Total HT", readonly=True, compute='_computeVar_final')
    prixtot_ttc = fields.Float(string="Prix Total TTC", readonly=True, compute='_computeVar_final')
    prixtot_bill = fields.Float(string="Prix TOTAL", readonly=True, compute='_computeVar_final')

    @api.depends('prixtot_ttc', 'prix', 'quantity', 'prixtot_ht', 'tax')
    def _computeVar_final(self):
        for order in self:
            prixtot = 0.0
            for line in order:
                line.prixtot_ht = line.prix * line.quantity
                line.prixtot_ttc = line.prixtot_ht + (line.prixtot_ht * (line.tax.amount / 100))
                prixtot += line.prixtot_ttc
            order.update({
                'prixtot_bill': prixtot,
            })

    facture_parent_id = fields.Many2one('customsales.facture', String="Informations Personnelles")



