from odoo.exceptions import Warning, ValidationError
from odoo import api, fields, models, _

class kartu_keluarga(models.Model):
    _name = "kartu.keluarga"
    _description = "Kartu Keluarga"
    
    name = fields.Char(string="Order Reference", required=True, copy=False, 
                            readonly=True, default=lambda self: _('New'))
    name_id = fields.Many2one(comodel_name='partner',string='Name')
    nik_kepala_keluarga = fields.Char(related="name_id.nik",string='NIK', readonly=True)
    no_kartu_keluarga = fields.Char(related="name_id.no_kartu_keluarga",string='Nomor Kartu Keluarga', readonly=True)
    no_kartu_keluarga_db = fields.Char(string='Nomor Kartu Keluarga', readonly=True)
    alamat = fields.Char(related="name_id.alamat",string='Alamat', readonly=True)
    kode_pos = fields.Char(related="name_id.kode_pos",string='Kode Pos', readonly=True)
    desa_id = fields.Many2one('kelurahan',related="name_id.kelurahan_id",string='Desa/Kelurahan', readonly=True)
    kecamatan_id = fields.Many2one('kecamatan',related="name_id.kecamatan_id",string='Kecamatan', readonly=True)
    kota_id = fields.Many2one('city',related="name_id.kota_id",string='Kabupatan/Kota', readonly=True)
    provinsi_id = fields.Many2one('country.state',related="name_id.provinsi_id",string='Provinsi', readonly=True)
    kepala_keluarga = fields.Boolean(related="name_id.kepala_keluarga", string='Kepala Keluarga')
    partner_ids = fields.One2many('partner','kartu_keluarga_id',string='Partner_ids')
    
    _sql_constraints = [
        ('no_kartu_keluarga_db_uniq', 'unique(no_kartu_keluarga_db)', 'Nomor Kartu Keluarga sudah ada !'),
    ]
    
    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name']= self.env['ir.sequence'].next_by_code('kartu.keluarga') or _('New')
        id_partner = self.env['partner'].search([('id','=',vals['name_id'])])
        vals['no_kartu_keluarga_db'] = id_partner.no_kartu_keluarga
        return super(kartu_keluarga,self).create(vals)
    
    def write(self,vals):
        id_partner = self.env['partner'].search([('id','=',vals['name_id'])])
        vals['no_kartu_keluarga_db'] = id_partner.no_kartu_keluarga
        return super(kartu_keluarga,self).write(vals)
    
    @api.onchange('name_id')
    def onchange_partner_id(self):
            nomor_kartu_keluarga = self.env['partner'].search([('no_kartu_keluarga','=',self.no_kartu_keluarga)])
            if nomor_kartu_keluarga:
                if self.kepala_keluarga:
                    for id in nomor_kartu_keluarga:
                        self.partner_ids = [[4, id.id]]
                else:
                    self.partner_ids = [[5]]
            else:
                pass
                
        