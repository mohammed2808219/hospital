from dataclasses import field
from odoo import api, fields, model, _


class HospitalPerawat(models.Model):
    _name = "hospital.perawat"
    _description = "Hospital Perawat"

    sup = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')

    alasan_keluhan = fields.Text(string="Alasan Keluhan")
    keadaan_sakit = fields.Selection([('tampak_sehat', 'Tampak Sehat'), ('sakit_ringan', 'Sakit Ringan'), (
        'sakit_sedang', 'Sakit Sedang'), ('sakit_berat', 'Sakit Berat')], required=True)
    kesadaran = fields.Selection([('compos_mentis', 'Compost Mentis'), (
        'somnolen', 'Somnolen'), ('apatis', 'Apatis'), ('delirium', 'Delirium')], required=True)
    sistole = fields.Float(string="Sistole")
    diastole = fields.Float(string="Diastole")
    detak_jantung = fields.Float(string="Detak Jantung")
    nafas = fields.Float(string="Nafas")
    suhu_badan = fields.Float(string="Suhu Badan")
    saturasi = fields.Float(string="Saturasi 02 CSpO2".translate(sup))
    alergi_makanan = fields.Char(string="Alergi Makanan")
    alergi_obat = fields.Char(string="Alergi Obat")
    tinggi_badan = fields.Float(string="Tinggi Badan")
    berat_badan = fields.Float(string="Berat Badan")
    imt = fields.Float(string="IMT")
    interpretasi = fields.Selection(
        [('kurang', 'Kurang'), ('normal', 'Normal'), ('ppe', 'PPE'), ('obesitas', 'Obesitas'), ('obesitas-1', 'Obesitas 1'), ('obesitas-2', 'Obesitas 2')], required=True)
    lingkar_perut = fields.Float(string="Lingkar Perut")
    lingkar_panggul = fields.Float(string="Lingkar Panggul")
    jenis_atap_rumah = fields.Selection([('beton', 'Beton'), ('genteng', 'Genteng'), ('asbes-seng', 'Asbes/Seng'), ('kayu-sirap', 'Kayu/Sirap'),
                                        ('bambu', 'Bambu'), ('jermai-ijuk-rumbia-daun', 'Jerami/Ijuk/Rumbia/Daun-daunan'), ('lainnya', 'Lainnya')], required=True)
    jenis_dinding_rumah = fields.Selection([('tembok', 'Tembok'), ('kayu-papan', 'Kayu/Papan'),
                                           ('seng', 'Seng'), ('bambu', 'Bambu'), ('lainnya', 'Lainnya')], required=True)
    jenis_lantai_rumah_terluas = fields.Selection([('keramik-granit-marmer-ubin-tegel-teraso', 'Keramik/Granit/Marmer/Ubin/Tegel/Teraso'), (
        'semen', 'Semen'), ('kayu-papan', 'Kayu/Papan'), ('bambu', 'Bambu'), ('tanah', 'Tanah'), ('lainnya', 'Lainnya')], required=True)
    sumber_penerangan_utama = fields.Selection([('900watt', 'Listrik Pribadi 900 Watt'), (
        '>900watt', 'Listrik Pribadi >900 Watt'), ('genset-solar_cell', 'Genset/ Solar Cell'), ('listrik_bersama', 'Listrik Bersama')])
    sumber_air_minum_utama = fields.Selection([('air_kemasan-isi_ulang', 'Air Kemasan/Isi Ulang'), ('ledeng-pam', 'Ledeng/PAM'), ('sumur_bor', 'Sumur Bor'), ('sumur_terlindung', 'Sumur Terlindung'),
                                              ('sumur_tidak_terlindung', 'Sumur Tidak Terlindung'), ('air_permukaan', 'Air Permukaan (Sungai, Danau, dll)'), ('air_hujan', 'Air Hujan'), ('lainnya', 'lainnya')], required=True)
    fasilitas_buang_air_besar = fields.Selection([('ya_dengan_septic_tank', 'Ya, dengan Septic'), (
        'ya_tanpa_septictank', 'Ya, Tanpa Septic Tank'), ('tidak_jamban_umum-bersama', 'Tidak, Jamban Umum/Bersama'), ('lainnya', 'Lainnya')])
    bangunan_keseluruhan = fields.Integer(
        string="Luas rumah/bangunan keseluruhan (m2)?", required=True)
    jumlah_orang_rumah = fields.Integer(
        string="Jumlah orang dalam satu rumah?", required=True)
    bahan_bakar_masak = fields.Selection([('listrik-gas', 'Listrik/Gas'), ('minyak_tanah',
                                         'Minyak Tanah'), ('arang-kayu', 'Arang/Kayu'), ('lainnya', 'Lainnya')], required=True)
    kepemilikan_rumah = fields.Selection([('milik_sendiri', 'Milik Sendiri'), ('kontrak-sewa', 'Kontrak/Sewa'), (
        'bebas_sewa', 'Bebas Sewa'), ('menumpang', 'Menumpang'), ('dinas', 'Dinas'), ('lainnya', 'Lainnya')], required=True)
    kb_pk = fields.Selection([('tidak', 'Tidak'), ('ya', 'Ya')], required=True)
    informasi_diperoleh = fields.Selection([('koran-majalah-tabloid', 'Koran/Majalah/Tabloid'), ('televisi-radio-videotron', 'Televisi/Radio/Videotron'), ('facebook-instagram-twitter-whatsapp-youtube-blog-website', 'Facebook/Instagram/Twitter/Whatsapp/Youtube/Blog/Website')('seminar-pengajian-ibadat-workshop-diseminasi-pertemuan_kelompok_kegiatan-konseling-pemeran',
                                           'Seminar/Pengajian/Ibadat/Workshop/Diseminasi/Pertemuan Kelompok Kegiatan/Konseling/Pemeran')('leaflet-lembar_balik-poster-spanduk-banner-umbul_umbul-billboard-baliho-mural_souvenir')('Leaflet/Lembar Balik/Poster/Spanduk/Banner/Umbul Umbul/Billboard/Baliho/Mural Souvenir')('wayang-tarian-pentas_budaya_lokal', 'Wayang/Tarian/Pentas Budaya Lokal')], required=True)
    kb_kp_petugas = fields.Selection(
        [('ya', 'Ya'), ('tidak', 'Tidak')], required=True)
    keluarga_informasi_diperoleh = fields.Selection([('pejabat_pemerintah', 'Pejabat Pemerintah'), ('petugas_keluarga_berencana-pkb-plkb-petugas-lapangan-kb-lainnya', 'Petugas Keluarga Berencana/PKB/PLKB/Petugas Lapangan KB/Lainnya'), ('guru-dosen', 'Guru/Dosen'), (
        'tokoh-agama', 'Tokoh Agama'), ('tokoh-masyarakat', 'Tokoh Masyarakat Masyarakat'), ('dokter', 'Dokter'), ('bidan-perawat', 'Bidan/Perawat'), ('perangkat-desa-kelurahan', 'Perangkat Desa/Kelurahan'), ('kader-imp', 'Kader/IMP')], required=True)
