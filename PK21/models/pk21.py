import string
from unicodedata import name
from traitlets import default
from odoo.exceptions import Warning, ValidationError
from odoo import api, fields, models, _

class PK21(models.Model):
    _name = "pk21"
    _description = "kode pk21"
    
    #                         # KEPENDUDUKAN #
                            
    # name=fields.Char(related='nama_anggotakel',string="nama_anggotakel")
    # nama_anggotakel=fields.Char(string="nama_anggotakel")
    # no_kk=fields.Char(string="Kode Keluarga Indonesia KKI", required=True)
    # jenis_kelamin=fields.Integer(string="Jenis Kelamin")
    # sts_hubungan=fields.Integer(string="Hubungan dengan kepala keluarga")
    # tgl_lahir=fields.Char(string="Tanggal Lahir")
    # sts_kawin=fields.Integer(string="Status Perkawinan")
    # usia_kawin=fields.Integer(string="Usia Perkawinan")
    # id_pekerjaan=fields.Integer(string="Status pekerjaan")
    # jns_pendidikan=fields.Integer(string="Pendidikan")
    # kd_ibukandung=fields.Integer(string="Kode Ibu Kandung")
    
    #                         # KELUARGA BERENCANA #
                            
    # kb1=fields.Integer(string="Sudah berapa kali Ibu melahirkan")
    # # Berapa jumlah anak lahir hidup 
    # kba1=fields.Integer(string="- Laki - Laki")
    # kba2=fields.Integer(string="- Perempuan")
    # # Berapa jumlah anak masih hidup 
    # kbb1=fields.Integer(string="- Laki - Laki")
    # kbb2=fields.Integer(string="- Perempuan")
    # kb3=fields.Selection([('1','ya'),('2','tidak')],string="Apakah ibu sedang hamil?")
    # # kalau ya
    # kb3a1_usiahamil=fields.Integer(string="Usia Kehamilan")
    # kb4=fields.Selection([('1','ya'),('2','tidak')],string="Apakah saat ini IBU atau SUAMI menggunakan alat/obat/cara KB (kontrasepsi)")
    # kb7=fields.Integer(string="Jenis alat/obat/cara KB (kontrasepsi) yang dipakai saat ini atau terakhir dipakai")
    
    
    #                                 # PEMBANGUNGAN KELUARGA #
                                    
    # pk4=fields.Selection([('1','ya'),('2','tidak')])
    # pk5=fields.Selection([('1','ya'),('2','tidak')],string="Selama 6 (enam) bulan terakhir, setiap anggota keluarga makan “makanan beragam” (makanan pokok, sayur/buah dan lauk) paling sedikit 2 (dua) kali sehari")
    # pk6=fields.Selection([('1','ya'),('2','tidak')],string="Keluarga memiliki tabungan/simpanan (uang kontan, perhiasan, hewan ternak, hasil kebun, dll) yang dapat digunakan sewaktu-waktu untuk memenuhi kebutuhan pokok dalam 3 (tiga) bulan ke depan")
    # pk19=fields.Integer(string="Jenis atap rumah terluas")
    # pk20=fields.Integer(string="Jenis dinding rumah terluas")
    # pk21=fields.Integer(string="Jenis lantai rumah terluas")
    # pk22=fields.Integer(string="Sumber penerangan utama")
    # pk23=fields.Integer(string="Sumber air minum utama")
    # pk24=fields.Integer(string="Memiliki fasilitas tempat buang air besar")
    # pk25=fields.Integer(string="Luas rumah/bangunan keseluruhan m2")
    # pk26=fields.Integer(string="Orang yang tinggal dan menetap di rumah/bangunan ini")
    # pk27=fields.Integer(string="Bahan bakar utama untuk memasak")
    # pk28=fields.Integer(string="Kepemilikan rumah/bangunan tempat tinggal")
    
    
    name=fields.Char(string="nama")
    name_Pertanyaan =fields.Char(string="Pertanyaan")
    kode=fields.Integer(string="kode")
    value= fields.Char(string="value")
    
    
    
    
    

            
    
    
    
    

