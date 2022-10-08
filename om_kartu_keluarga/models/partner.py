from odoo.exceptions import Warning, ValidationError
from odoo import api, fields, models, _
from datetime import datetime

class Partner(models.Model):
    _name = "partner"
    _description = "Regestrasi Partner"
    
    
    name = fields.Char(string='Nama Pasien')
    no_kartu_keluarga = fields.Char(string='Nomor Kartu Keluarga')
    kepala_keluarga = fields.Boolean(string='Kepala Keluarga')
    alamat = fields.Char(string='Alamat')
    kode_pos = fields.Char(string='Kode Pos')
    provinsi_id = fields.Many2one('country.state',string="Provinsi")
    kota_id = fields.Many2one('city',string='Kota/Kabupaten',domain="[('state_id','=',provinsi_id)]")
    kecamatan_id = fields.Many2one('kecamatan',string='Kecamatan',domain="[('city_id','=',kota_id)]")
    kelurahan_id = fields.Many2one('kelurahan',string='Kelurahan/Desa', domain="[('kecamatan_id','=',kecamatan_id)]")
    nik = fields.Char(string='NIK')
    jenis_kelamin = fields.Selection([('1','laki-laki'),('2','perempuan')],string='Jenis Kelamin')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    agama = fields.Char(string='Agama')
    pendidikan = fields.Many2one(comodel_name="pk21",string='Pendidikan', domain="[('name','=','jns_pendidikan')]")
    jenis_pekerjaan = fields.Many2one(comodel_name="pk21",string='Jenis Pekerjaan', domain="[('name','=','id_pekerjaan')]")
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
    status_keluarga = fields.Many2one(comodel_name="pk21",string='Status di Keluarga', domain="[('name','=','sts_hubungan')]")
    status_perkawinan = fields.Many2one(comodel_name="pk21",string='Status Perkawinan', domain="[('name','=','sts_kawin')]")
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
    kb7=fields.Many2one(comodel_name="pk21",string="Jenis alat/obat/cara KB", domain="[('name','=','kb7')]")
    pk4=fields.Selection([('1','ya'),('2','tidak')],string="Selama 6 (enam) bulan terakhir, terdapat paling sedikit 1 (satu) anggota keluarga yang memiliki sumber penghasilan untuk memenuhi kebutuhan pokok per bulan")
    pk5=fields.Selection([('1','ya'),('2','tidak')],string="Selama 6 (enam) bulan terakhir, setiap anggota keluarga makan “makanan beragam” (makanan pokok, sayur/buah dan lauk) paling sedikit 2 (dua) kali sehari")
    pk6=fields.Selection([('1','ya'),('2','tidak')],string="Keluarga memiliki tabungan/simpanan (uang kontan, perhiasan, hewan ternak, hasil kebun, dll) yang dapat digunakan sewaktu-waktu untuk memenuhi kebutuhan pokok dalam 3 (tiga) bulan ke depan")
    pk19=fields.Many2one(comodel_name="pk21",string="Jenis atap rumah terluas", domain="[('name','=','pk19')]")
    pk20=fields.Many2one(comodel_name="pk21",string="Jenis dinding rumah terluas", domain="[('name','=','pk20')]")
    pk21=fields.Many2one(comodel_name="pk21",string="Jenis lantai rumah terluas", domain="[('name','=','pk21')]")
    pk22=fields.Many2one(comodel_name="pk21",string="Sumber penerangan utama", domain="[('name','=','pk22')]")
    pk23=fields.Many2one(comodel_name="pk21",string="Sumber air minum utama", domain="[('name','=','pk23')]")
    pk24=fields.Many2one(comodel_name="pk21",string="Memiliki fasilitas tempat buang air besar", domain="[('name','=','pk24')]")
    pk25=fields.Integer(string="Luas rumah/bangunan keseluruhan m2")
    pk26=fields.Integer(string="Luas rumah/bangunan keseluruhan m2")
    pk27=fields.Many2one(comodel_name="pk21",string="Bahan bakar utama untuk memasak", domain="[('name','=','pk27')]")
    pk28=fields.Many2one(comodel_name="pk21",string="Kepemilikan rumah/bangunan tempat tinggal", domain="[('name','=','pk28')]")
    # Berapa jumlah anak lahir hidup
    kba1=fields.Integer(string="-Laki - Laki")
    kba2=fields.Integer(string="-Perempuan")
    # Berapa jumlah anak masih hidup   
    kbb1=fields.Integer(string="-Laki - Laki")
    kbb2=fields.Integer(string="-Perempuan")
    
    kb1=fields.Integer(string="Sudah berapa kali Ibu melahirkan")
    kd_ibukandung=fields.Integer(string="Kode Ibu Kandung")
    # tgl_lahir=fields.Char(string="Tanggal Lahir")
    related_status_perkawinan = fields.Integer(related='status_perkawinan.kode', string='Status Perkawinan', store=True)
    
    
    _sql_constraints = [
        ('nik_uniq', 'unique(nik)', 'NIK sudah ada !'),
    ]
    
    @api.model
    def create(self,vals):
        if not vals.get('nik').isdigit() :
            raise ValidationError('Perhatian!\nNIK harus angkah.')
        elif not vals.get('no_kartu_keluarga').isdigit():
            raise ValidationError('Perhatian!\nNomor Kartu Keluarga harus angkah.')
        return super(Partner,self).create(vals)
    
    
    def write(self,vals):
        if vals.get('nik'):
            if not vals.get('nik').isdigit() :
                raise ValidationError('Perhatian!\nNIK harus angkah.')
        if vals.get('no_kartu_keluarga'):
            if not vals.get('no_kartu_keluarga').isdigit():
                raise ValidationError('Perhatian!\nNomor Kartu Keluarga harus angkah.')
        return super(Partner,self).write(vals)
    
    
    @api.model
    def name_search(self,name,args=None,operator='ilike',limit=100):
        args =  args or []
        if name:
            args = ['|','|',('name',operator,name),('no_kartu_keluarga',operator,name),('nik',operator,name)]
        categorys = self.search(args, limit=limit)
        return categorys.name_get()

            
            
    
    
    
    

