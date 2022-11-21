from odoo import api, fields, models, _


class HospitalPerawat(models.Model):
    _name = "hospital.perawat"
    _description = "Hospital Perawat"

    sup = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')

    keadaan_sakit = fields.Selection([('tampak_sehat', 'Tampak Sehat'), ('sakit_ringan', 'Sakit Ringan'), (
        'sakit_sedang', 'Sakit Sedang'), ('sakit_berat', 'Sakit Berat')])
    kesadaran = fields.Selection([('compos_mentis', 'Compost Mentis'), (
        'somnolen', 'Somnolen'), ('apatis', 'Apatis'), ('delirium', 'Delirium')])
    sistole = fields.Float(string="Sistole")
    diastole = fields.Float(string="Diastole")
    detak_jantung = fields.Float(string="Detak Jantung")
    nafas = fields.Float(string="Nafas")
    suhu_badan = fields.Float(string="Suhu Badan")
    saturasi = fields.Float(string="Saturasi O2 CSpO2".translate(sup))
    alergi = fields.Boolean(string="Alergi")
    alergi_makanan = fields.Char(string="Alergi Makanan")
    alergi_obat = fields.Char(string="Alergi Obat")
    tinggi_badan = fields.Float(string="Tinggi Badan")
    berat_badan = fields.Float(string="Berat Badan")
    imt = fields.Float(string="IMT", readonly=True)
    interpretasi = fields.Selection(
        [('kurang', 'Kurang'), ('normal', 'Normal'), ('ppe', 'PPE'), ('obesitas', 'Obesitas'), ('obesitas-1', 'Obesitas 1'), ('obesitas-2', 'Obesitas 2')])
    lingkar_perut = fields.Float(string="Lingkar Perut")
    lingkar_panggul = fields.Float(string="Lingkar Panggul")
    jenis_atap_rumah = fields.Selection([('beton', 'Beton'), ('genteng', 'Genteng'), ('asbes-seng', 'Asbes/Seng'), ('kayu-sirap', 'Kayu/Sirap'),
                                        ('bambu', 'Bambu'), ('jermai-ijuk-rumbia-daun', 'Jerami/Ijuk/Rumbia/Daun-daunan'), ('lainnya', 'Lainnya')])
    jenis_dinding_rumah = fields.Selection([('tembok', 'Tembok'), ('kayu-papan', 'Kayu/Papan'),
                                           ('seng', 'Seng'), ('bambu', 'Bambu'), ('lainnya', 'Lainnya')])
    jenis_lantai_rumah_terluas = fields.Selection([('keramik-granit-marmer-ubin-tegel-teraso', 'Keramik/Granit/Marmer/Ubin/Tegel/Teraso'), (
        'semen', 'Semen'), ('kayu-papan', 'Kayu/Papan'), ('bambu', 'Bambu'), ('tanah', 'Tanah'), ('lainnya', 'Lainnya')])
    sumber_penerangan_utama = fields.Selection([('900watt', 'Listrik Pribadi 900 Watt'), (
        '>900watt', 'Listrik Pribadi >900 Watt'), ('genset-solar_cell', 'Genset/ Solar Cell'), ('listrik_bersama', 'Listrik Bersama')])
    sumber_air_minum_utama = fields.Selection([('air_kemasan-isi_ulang', 'Air Kemasan/Isi Ulang'), ('ledeng-pam', 'Ledeng/PAM'), ('sumur_bor', 'Sumur Bor'), ('sumur_terlindung', 'Sumur Terlindung'),
                                              ('sumur_tidak_terlindung', 'Sumur Tidak Terlindung'), ('air_permukaan', 'Air Permukaan (Sungai, Danau, dll)'), ('air_hujan', 'Air Hujan'), ('lainnya', 'lainnya')])
    fasilitas_buang_air_besar = fields.Selection([('ya_dengan_septic_tank', 'Ya, dengan Septic'), (
        'ya_tanpa_septictank', 'Ya, Tanpa Septic Tank'), ('tidak_jamban_umum-bersama', 'Tidak, Jamban Umum/Bersama'), ('lainnya', 'Lainnya')])
    bangunan_keseluruhan = fields.Integer(
        string="Luas bangunan keseluruhan (m2)?")
    jumlah_orang_rumah = fields.Integer(
        string="Jumlah orang dalam satu rumah?")
    bahan_bakar_masak = fields.Selection([('listrik-gas', 'Listrik/Gas'), ('minyak_tanah',
                                         'Minyak Tanah'), ('arang-kayu', 'Arang/Kayu'), ('lainnya', 'Lainnya')])
    kepemilikan_rumah = fields.Selection([('milik_sendiri', 'Milik Sendiri'), ('kontrak-sewa', 'Kontrak/Sewa'), (
        'bebas_sewa', 'Bebas Sewa'), ('menumpang', 'Menumpang'), ('dinas', 'Dinas'), ('lainnya', 'Lainnya')])
    kb_pk = fields.Boolean(default=False)
    informasi_diperoleh = fields.Selection([('koran-majalah-tabloid', 'Koran/Majalah/Tabloid'), ('televisi-radio-videotron', 'Televisi/Radio/Videotron'), ('facebook-instagram-twitter-whatsapp-youtube-blog-website', 'Facebook/Instagram/Twitter/Whatsapp/Youtube/Blog/Website'),('seminar-pengajian-ibadat-workshop-diseminasi-pertemuan_kelompok_kegiatan-konseling-pemeran',
                                           'Seminar/Pengajian/Ibadat/Workshop/Diseminasi/Pertemuan Kelompok Kegiatan/Konseling/Pemeran'),('leaflet-lembar_balik-poster-spanduk-banner-umbul_umbul-billboard-baliho-mural_souvenir', 'Leaflet/Lembar Balik/Poster/Spanduk/Banner/Umbul Umbul/Billboard/Baliho/Mural Souvenir'),('wayang-tarian-pentas_budaya_lokal', 'Wayang/Tarian/Pentas Budaya Lokal')])
    kb_kp_petugas = fields.Boolean(default=False)
    keluarga_informasi_diperoleh = fields.Selection([('pejabat_pemerintah', 'Pejabat Pemerintah'), ('petugas_keluarga_berencana-pkb-plkb-petugas-lapangan-kb-lainnya', 'Petugas Keluarga Berencana/PKB/PLKB/Petugas Lapangan KB/Lainnya'), ('guru-dosen', 'Guru/Dosen'), (
        'tokoh-agama', 'Tokoh Agama'), ('tokoh-masyarakat', 'Tokoh Masyarakat Masyarakat'), ('dokter', 'Dokter'), ('bidan-perawat', 'Bidan/Perawat'), ('perangkat-desa-kelurahan', 'Perangkat Desa/Kelurahan'), ('kader-imp', 'Kader/IMP')])
    peringatan_interpretasi_imt = fields.Selection([('kurang','Kurang'),('normal','Normal'),('pre-obesitas','Pre-Obesitas'),('obesitas','Obesitas'),('obesitas-1','Obesitas 1'),('obesitas-2','Obesitas 2')]) 
    peringatan_alergi = fields.Text('Alergi')  
    ghk_merokok = fields.Selection([('tidak', 'Tidak'), ('ya', 'Ya')], string="Merokok ?")
    ghk_alkohol = fields.Selection([('tidak', 'Tidak'), ('ya', 'Ya')], string="Konsumsi Alkohol ?")
    ghk_olahraga = fields.Selection([('tidak', 'Tidak'), ('ya', 'Ya')], string="Olahraga 3 x 30 Menit per-Minggu ?")
    ghk_makan_sayur = fields.Selection([('tidak', 'Tidak'), ('ya', 'Ya')], string="Makan Sayur (Tinggi Serat) 3 Porsi Setiap Hari ?")


    name = fields.Many2one(comodel_name="partner", string="Nama Pasien")
    nama_kk = fields.Many2one(comodel_name="partner", string="Nama KK", domain=[('kepala_keluarga', '=', True)])
    alamat_kk = fields.Char(related="nama_kk.alamat", string="Alamat", readonly=True)
    nomer_kk = fields.Char(related="nama_kk.nik_kepala_keluarga", string="Nomer KK", readonly=True)
    no_hp_kk = fields.Char(related="nama_kk.no_hp", string="No HP", readonly=True)
    email_kk = fields.Char(related="nama_kk.email", string="Email", readonly=True)
    nik = fields.Char(related="nama_kk.nik", string="nik")
    age = fields.Integer()

    keluhan_ids = fields.Many2many('alasan.datang', string="Alasan Datang")
    subjektif_id = fields.Many2one('medik')


    @api.onchange('tinggi_badan', 'berat_badan')
    def _onchange_imt(self):
        if self.tinggi_badan and self.berat_badan :
            imt = self.berat_badan / (self.tinggi_badan / 100)
            self.imt = imt
            if imt < 18.5:
                self.peringatan_interpretasi_imt = 'kurang'
            elif imt >= 18.5 and imt <= 22.9:
                self.peringatan_interpretasi_imt = 'normal'
            elif imt >= 23 and imt <= 24.9:
                self.peringatan_interpretasi_imt = 'pre-obesitas'
            elif imt >= 25 and imt <= 29.9:
                self.peringatan_interpretasi_imt = 'obesitas-1'
            elif imt >= 30 and imt < 35:
                self.peringatan_interpretasi_imt = 'obesitas-2'
            else:
                self.peringatan_interpretasi_imt = 'obesitas-2'
        else :
            self.imt = 0
            self.peringatan_interpretasi_imt = ''

    @api.onchange('alergi_makanan', 'alergi_obat')
    def _onchange_alergi(self):
        if self.alergi:
            alergi_str = ''
            if self.alergi_makanan or self.alergi_obat:
                alergi_str += 'Makanan : ' + str(self.alergi_makanan) + "\n" + 'Obat : ' + str(self.alergi_obat)
                self.peringatan_alergi = alergi_str


    @api.model
    def create(self, vals):
        if vals.get('tinggi_badan') and vals.get('berat_badan'):
            imt = vals.get('berat_badan') / (vals.get('tinggi_badan') / 100)
            vals['imt'] = imt
            if imt < 18.5:
                vals['peringatan_interpretasi_imt'] = 'kurang'
            elif imt >= 18.5 and imt <= 22.9:
                vals['peringatan_interpretasi_imt'] = 'normal'
            elif imt >= 23 and imt <= 24.9:
                vals['peringatan_interpretasi_imt'] = 'pre-obesitas'
            elif imt >= 25 and imt <= 29.9:
                vals['peringatan_interpretasi_imt'] = 'obesitas-1'
            elif imt >= 30 and imt < 35:
                vals['peringatan_interpretasi_imt'] = 'obesitas-2'
            else:
                vals['peringatan_interpretasi_imt'] = 'obesitas-2'
        else :
            self.imt = 0
            self.peringatan_interpretasi_imt = ''
         
        alergi = vals.get('alergi') or self.alergi   
        if alergi:
            alergi_str = ''
            if  vals.get('alergi_makanan') or  vals.get('alergi_obat'):
                alergi_str += 'Makanan : ' +  str(vals.get('alergi_makanan')) + "\n" + 'Obat : ' +  str(vals.get('alergi_obat'))
                vals['peringatan_alergi'] = alergi_str
                
        return super(HospitalPerawat, self).create(vals)
    
    def write(self,vals):
        
        tinggi = vals.get('tinggi_badan') or self.tinggi_badan
        berat = vals.get('berat_badan') or self.berat_badan
        if tinggi or berat:
            imt = berat / (tinggi / 100)
            vals['imt'] = imt
            if imt < 18.5:
                vals['peringatan_interpretasi_imt'] = 'kurang'
            elif imt >= 18.5 and imt <= 22.9:
                vals['peringatan_interpretasi_imt'] = 'normal'
            elif imt >= 23 and imt <= 24.9:
                vals['peringatan_interpretasi_imt'] = 'pre-obesitas'
            elif imt >= 25 and imt <= 29.9:
                vals['peringatan_interpretasi_imt'] = 'obesitas-1'
            elif imt >= 30 and imt < 35:
                vals['peringatan_interpretasi_imt'] = 'obesitas-2'
            else:
                vals['peringatan_interpretasi_imt'] = 'obesitas-2'
        # import ipdb; ipdb.set_trace()    
        alergi = vals.get('alergi') or self.alergi 
        if alergi:
            alergi_str = ''
            if  vals.get('alergi_makanan') or  vals.get('alergi_obat'):
                alergi_str += 'Makanan : ' +  str(vals.get('alergi_makanan')) + "\n" + 'Obat : ' +  str(vals.get('alergi_obat'))
                vals['peringatan_alergi'] = alergi_str
                
        return super(HospitalPerawat,self).write(vals)
            
        