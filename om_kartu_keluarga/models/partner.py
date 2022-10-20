from traitlets import Instance
from odoo.exceptions import Warning, ValidationError
from odoo import api, fields, models, _
from datetime import datetime

class Partner(models.Model):
    _name = "partner"
    _description = "Regestrasi Partner"
    
    
    name = fields.Char(string='Nama Pasien')
    rekam_medis = fields.Char(string='No. Rekam Medis', default=lambda self: _('New'), readonly=True)
    nik_kepala_keluarga = fields.Char(string='NIK Kepala Keluarga', required=True)
    kepala_keluarga = fields.Boolean(string='Kepala Keluarga')
    alamat = fields.Char(string='Alamat')
    kode_pos = fields.Char(string='Kode Pos')
    provinsi_id = fields.Many2one('country.state',string="Provinsi")
    kota_id = fields.Many2one('city',string='Kota/Kabupaten',domain="[('state_id','=',provinsi_id)]")
    kecamatan_id = fields.Many2one('kecamatan',string='Kecamatan',domain="[('city_id','=',kota_id)]")
    kelurahan_id = fields.Many2one('kelurahan',string='Kelurahan/Desa', domain="[('kecamatan_id','=',kecamatan_id)]")
    nik = fields.Char(string='NIK', required=True)
    jenis_kelamin = fields.Selection([('1','laki-laki'),('2','perempuan')],string='Jenis Kelamin')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    agama = fields.Char(string='Agama')
    pendidikan = fields.Many2one(comodel_name="pk21",string='Pendidikan', domain="[('value','=','jns_pendidikan')]")
    jenis_pekerjaan = fields.Many2one(comodel_name="pk21",string='Jenis Pekerjaan', domain="[('value','=','id_pekerjaan')]")
    no_hp = fields.Char(string='Nomor HP')
    email = fields.Char(string='Email')
    golongan_darah = fields.Selection([
        ('a','A'),
        ('b','B'),
        ('ab','AB'),
        ('o','O'),
        ('a+','A+'),
        ('b+','B+'),
        ('ab+','AB+'),
        ('o+','O+'),
        ('o-','O-'),
        ('a-','A-'),
        ('b-','B-'),
        ('ab-','AB-'),
        ], string='Golongan Darah')
    sts_hubungan = fields.Many2one(comodel_name="pk21",string='Status di Keluarga', domain="[('value','=','sts_hubungan')]")
    sts_kawin = fields.Many2one(comodel_name="pk21",string='Status Perkawinan', domain="[('value','=','sts_kawin')]")
    usia_kawin_pertama_tahun = fields.Integer(string='Usia Kawin Pertama')
    usia_kawin_pertama_bulan = fields.Selection([
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ], string='Usia Kawin Pertama')
    etnis = fields.Char(string='Etnis')
    kewarganegaraan = fields.Selection([
        ('wni','WNI'),
        ('wna','WNA'),],string='Kewarganegaraan')
    kartu_keluarga_id = fields.Many2one(comodel_name='kartu.keluarga', string='Kartu Keluarga')
    kb3=fields.Selection([('1','ya'),('2','tidak')],string="Apakah ibu sedang hamil?")
    # kalau ya
    kb3a1_usiahamil=fields.Integer(string="Usia Kehamilan")
    kb7=fields.Many2one(comodel_name="pk21",string="Jenis alat/obat/cara KB", domain="[('value','=','kb7')]")
    pk4=fields.Boolean()
    pk5=fields.Boolean()
    pk6=fields.Boolean()
    pk19=fields.Many2one(comodel_name="pk21",string="Jenis atap rumah terluas", domain="[('value','=','pk19')]")
    pk20=fields.Many2one(comodel_name="pk21",string="Jenis dinding rumah terluas", domain="[('value','=','pk20')]")
    pk21=fields.Many2one(comodel_name="pk21",string="Jenis lantai rumah terluas", domain="[('value','=','pk21')]")
    pk22=fields.Many2one(comodel_name="pk21",string="Sumber penerangan utama", domain="[('value','=','pk22')]")
    pk23=fields.Many2one(comodel_name="pk21",string="Sumber air minum utama", domain="[('value','=','pk23')]")
    pk24=fields.Many2one(comodel_name="pk21",string="Memiliki fasilitas tempat buang air besar", domain="[('value','=','pk24')]")
    pk25=fields.Integer(string="Luas rumah/bangunan keseluruhan m2")
    pk26=fields.Integer(string="Jumlah orang yang tinggal dan menetap di rumah/bangunan ini")
    pk27=fields.Many2one(comodel_name="pk21",string="Bahan bakar utama untuk memasak", domain="[('value','=','pk27')]")
    pk28=fields.Many2one(comodel_name="pk21",string="Kepemilikan rumah/bangunan tempat tinggal", domain="[('value','=','pk28')]")
    # Berapa jumlah anak lahir hidup
    kba1=fields.Integer(string="-Laki - Laki")
    kba2=fields.Integer(string="-Perempuan")
    # Berapa jumlah anak masih hidup   
    kbb1=fields.Integer(string="-Laki - Laki")
    kbb2=fields.Integer(string="-Perempuan")
    
    kb1=fields.Integer(string="Sudah berapa kali Ibu melahirkan")
    kd_ibukandung=fields.Integer(string="Kode Ibu Kandung")
    # tgl_lahir=fields.Char(string="Tanggal Lahir")
    related_sts_kawin = fields.Integer(related='sts_kawin.kode', string='Status Perkawinan', store=True)
    
    
    _sql_constraints = [
        ('nik_uniq', 'unique(nik)', 'NIK sudah ada !'),
    ]
    
    
    @api.model
    def create(self,vals):
        if vals.get('rekam_medis', _('New')) == _('New'):
            vals['rekam_medis']= self.env['ir.sequence'].next_by_code('partner') or _('New')
            
        if vals.get('nik'):
            if not vals.get('nik').isdigit() :
                raise ValidationError('Perhatian!\nNIK harus angkah.')
            if len(vals.get('nik')) != 16 :
                raise ValidationError('Perhatian!\nNIK harus 16 angkah.')
        if vals.get('nik_kepala_keluarga'):
            if not vals.get('nik_kepala_keluarga').isdigit():
                raise ValidationError('Perhatian!\nNomor Kartu Keluarga harus angkah.')
            elif len(vals.get('nik_kepala_keluarga')) != 16 :
                raise ValidationError('Perhatian!\nNomor Kartu Keluarga harus 16 angkah.')
            elif vals.get('kepala_keluarga') == True:
                nik_kepala_true = self.search([('nik_kepala_keluarga','=',vals.get('nik_kepala_keluarga')),('kepala_keluarga','=',True)])
                if nik_kepala_true:
                    raise ValidationError('Perhatian!\nkepala Keluarga untuk NIK ini sudah ada.')
            
        if not vals.get('provinsi_id'):
            vals['provinsi_id'] = 40 # 40 adalah id provinsi Lampung
        if vals.get('sts_hubungan') == '1':
            vals['kepala_keluarga'] = True
        return super(Partner,self).create(vals)
    
    
    def write(self,vals):
        if vals.get('nik'):
            if not vals.get('nik').isdigit() :
                raise ValidationError('Perhatian!\nNIK harus angkah.')
            if len(vals.get('nik')) != 16 :
                raise ValidationError('Perhatian!\nNIK harus 16 angkah.')
        if vals.get('nik_kepala_keluarga'):
            if not vals.get('nik_kepala_keluarga').isdigit():
                raise ValidationError('Perhatian!\nNomor Kartu Keluarga harus angkah.')
            elif len(vals.get('nik_kepala_keluarga')) != 16 :
                raise ValidationError('Perhatian!\nNomor Kartu Keluarga harus 16 angkah.')
        if vals.get('kepala_keluarga') == True:
            nik_kepala_true = self.search([('nik_kepala_keluarga','=',self.nik_kepala_keluarga),('kepala_keluarga','=',True)])
            if nik_kepala_true:
                raise ValidationError('Perhatian!\nkepala Keluarga untuk NIK ini sudah ada.')
        
        if vals.get('sts_hubungan') == '1':
            vals['kepala_keluarga'] = True
            
        return super(Partner,self).write(vals)
    
    
    @api.model
    def name_search(self,name,args=None,operator='ilike',limit=100):
        args =  args or []
        if name:
            args = ['|','|',('name',operator,name),('nik_kepala_keluarga',operator,name),('nik',operator,name),('kepala_keluarga','=',True)]
        categorys = self.search(args, limit=limit)
        return categorys.name_get()

            
            
    
    
    
    

