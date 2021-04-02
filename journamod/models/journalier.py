from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class journalier(models.Model):
    _name = 'journamod.journalier'
    _description = 'Menu model'
#    _rec_name = 'sequence_id'

#    sequence_id = fields.Char(string='sequence', readonly=True)
    nom = fields.Char(string='Nom', Requiered=True)
    prenom = fields.Char(string='Prenom', Requiered=True)
    date_naissance = fields.Date(string='Date de naissance', Requiered = True)
    user_id = fields.Integer(string='Identification Utilisateur', Requiered = True)
    genre = fields.Selection([
        ('man', 'Homme'),
        ('woman', 'Femme'),
        ('other', 'Autre')
    ], string="Genre", default='man')
    state = fields.Selection([
        ('available','Disponible'),
        ('busy','Occupe'),
        ('secret', 'Non renseigne')
    ], string="Etat", default='available')

    # @api.model
    # def create(self, vals):
    #     seq = self.env['ir.sequence'].next_by_code('journamod') or '/'
    #     vals['sequence_id'] = seq
    #     return super(Journalier, self).create(vals)
    #
    # @api.one
    # def occupeProgressbar(self):
    #     self.write({'state': 'busy',})
    #
    # @api.one
    # def libreProgressbar(self):
    #     self.write({'state': 'available'})
    #
    # _sql_constraints = [('id_unique', 'UNIQUE(user_id)', 'Numero deja existant.')]
