from odoo import fields, models, api


class activite(models.Model):
    _name = 'customsales.activite'
    _description = 'Creer des activite dans un agenda'

    name = fields.Char()
    participants = fields.Many2many('res.partner')

    time_start = fields.Date()
    time_end = fields.Date()

    time_reel_start = fields.Date()
    time_reel_end = fields.Date()

    duree = fields.Datetime()

    #tag = fields.Many2many('categ_ids')
    lieu = fields.Char()

    responsable = fields.Many2one('res.users')

    state = fields.Selection([('planifie', 'Planifiée'),
                              ('encours', 'En cours'),
                              ('termine', 'Terminée'),
                              ('annule', 'Annulée')])


