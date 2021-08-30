from odoo import fields, models, api


class colorchanger(models.TransientModel):
    _inherit = 'res.config.settings'

    colorbar = fields.Char(string="Couleur du menu", config_parameter="customcolors.colorbar")
    colorbutton = fields.Char(string="Couleur des boutons", config_parameter="customcolors.colorbutton")

    def set_values(self):
        res = super(colorchanger, self).set_values()
        self.env['ir.config_parameter'].set_param('colorchanger.colorbar', self.colorbar)
        return res


@api.model
def get_values(self):
    res = super(colorchanger, self).get_values()
    ICPstudio = self.env['ir.config_parameter'].sudo()
    colorbar = ICPstudio.get_param('colorchanger.colorbar')
    res.update(
        colorbar=colorbar
    )
    return res
