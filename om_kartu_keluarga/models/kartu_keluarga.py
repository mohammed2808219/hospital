from odoo.exceptions import Warning, ValidationError
from odoo import api, fields, models, _

class kartu_keluarga(models.Model):
    _name = "kartu.keluarga"
    _description = "Kartu Keluarga"
    
    name = fields.Char(string="Order Reference", required=True, copy=False, 
                            readonly=True, default=lambda self: _('New'))
    name_id = fields.Many2one(comodel_name='partner',string='Name', domain=[('kepala_keluarga', '=', True)])
    nik_kepala_keluarga = fields.Char(related="name_id.nik",string='NIK Kepala Keluarga', readonly=True, store=True)
    alamat = fields.Char(related="name_id.alamat",string='Alamat', readonly=True)
    kode_pos = fields.Char(related="name_id.kode_pos",string='Kode Pos', readonly=True)
    desa_id = fields.Many2one('kelurahan',related="name_id.kelurahan_id",string='Desa/Kelurahan', readonly=True)
    kecamatan_id = fields.Many2one('kecamatan',related="name_id.kecamatan_id",string='Kecamatan', readonly=True)
    kota_id = fields.Many2one('city',related="name_id.kota_id",string='Kabupatan/Kota', readonly=True)
    provinsi_id = fields.Many2one('country.state',related="name_id.provinsi_id",string='Provinsi', readonly=True)
    kepala_keluarga = fields.Boolean(related="name_id.kepala_keluarga", string='Kepala Keluarga', store=True)
    partner_ids = fields.One2many('partner','kartu_keluarga_id',string='Partner_ids')
    
    _sql_constraints = [
        ('nik_kepala_keluarga_uniq', 'unique(nik_kepala_keluarga)', 'NIK Kepala Keluarga sudah ada !'),
    ]
    
    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name']= self.env['ir.sequence'].next_by_code('kartu.keluarga') or _('New')
        return super(kartu_keluarga,self).create(vals)
    
    @api.onchange('name_id')
    def onchange_partner_id(self):
            nomor_kepala_keluarga = self.env['partner'].search([('nik_kepala_keluarga','=',self.nik_kepala_keluarga)])
            if nomor_kepala_keluarga:
                self.partner_ids = False
                ids = []
                if self.kepala_keluarga:
                    for id in nomor_kepala_keluarga:
                        ids.append(id.id)
                    self.partner_ids = ids
                else:
                   self.partner_ids = False
            else:
                self.partner_ids = False
                
        