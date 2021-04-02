from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class journalier(models.Model):
    _name = 'journamod.journalier'
    _description = 'Menu model'

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

