from odoo import api, fields, models, _


class AlasanDatang(models.Model):
    _name = "alasan.datang"
    _description = "Alasan Datang"

    name = fields.Char(string="Alasan Datang", required=True)
    code = fields.Char(string="Code", required=True)

    keluhan_ids = fields.Many2many(
        'hospital.perawat', 'form_perawat_rel', 'keluhan_id', 'hospital_perawat_id', 'Keluhan')

    @api.model
    def create(self, vals):
        if vals.get('name', 'code'):
            vals['name'] = '[{0}] {1}'.format(vals['code'], vals['name'])
            return super(AlasanDatang, self).create(vals)
