from odoo import api, fields, models, _

class PartnerInherit(models.Model):
    _inherit = 'partner'
    
    subjektif_id = fields.Many2one(comodel_name='medik', string='subjektif')
    