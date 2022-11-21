from odoo import api, fields, models, _

class Medik(models.Model):
    _name = "medik"
    
    name = fields.Char(string="Name")
    #subjektif
    perawat_id = fields.Many2one('hospital.perawat','name')
    perawat_ids = fields.One2many('hospital.perawat', 'subjektif_id' ,'perawat_ids')
    subjektif = fields.Text(string='Subjektif')
    subjektif_dokter = fields.Text()
    riwayat_penyakit = fields.Text(string="Riwayat Penyakit")
    riwayat_personal = fields.Text(string="Riwayat Personal")
    partner_ids = fields.One2many('partner', 'subjektif_id' , string='partner_ids')
    subjektif_partner_ids = fields.One2many('subjektif.partner', 'subjektif_id' , string='subjektif partner')
    
    
    #objektif
    objektif = fields.Text(string='Pemeriksaan Awal')
    kepala = fields.Boolean(string='Kepala')
    kepala_disc = fields.Text()
    leher = fields.Boolean(string='Leher')
    leher_disc = fields.Text()
    thorax = fields.Boolean(string='Thorax')
    thorax_disc = fields.Text()
    abdomen = fields.Boolean(string='Abdomen')
    abdomen_disc = fields.Text()
    ekstremitas = fields.Boolean(string='Ekstremitas')
    ekstremitas_disc = fields.Text()
    genitalia = fields.Boolean(string='Genitalia')
    genitalia_disc = fields.Text()
    lain_lain = fields.Boolean(string='Lain-lain')
    lain_lain_disc = fields.Text()
    
    
    #assesment
    kasus = fields.Selection([
        ('1', 'Kasus Baru'),
        ('2', 'Kasus Lama'),
        ])
    masalah = fields.Selection([
        ('1', 'Masalah Umum'),
        ('2', 'Masalah Spesifik'),
        ('3', 'Masalah Kompleks'),
        ('4', 'Masalah Promotif/Preventif'),
    ])
    icpc_2_id = fields.Many2one(comodel_name='icpc', string='ICPC-2')
    icp_icd = fields.Char(related='icpc_2_id.code_icd')
    icd10_id = fields.Many2one(comodel_name='icd', string="Diagnosis Kerja(ICD10)")
    aspik_personal = fields.Text(string='Aspik Personal')
    aspik_klinis = fields.Text(string='Aspik Klinis')
    aspik_risiko_internal = fields.Text(string='Aspik Risiko Internal')
    aspik_risiko_eksternal = fields.Text(string='Aspik Risiko Eksternal')
    derajat_fungsional = fields.Text(string='Derajat Fungsional')
    
    
    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name']= self.env['ir.sequence'].next_by_code('medik') or _('New')
        return super(Medik, self).create(vals)
    
      
    
    @api.onchange('perawat_id','icpc_2_id')
    def _onchange_subjektif(self):
        self.subjektif_partner_ids = False
        partner = self.env['partner'].search([
            '|', '|',
            ('nik_kepala_keluarga','=',self.perawat_id.nik),
            ('nik_kepala_keluarga','=',self.perawat_id.nomer_kk), 
            ('nik','=',self.perawat_id.nomer_kk)
            ])
        if partner:
            ids = []
            for id in partner:
                if id.nik_kepala_keluarga:
                    ids.append([0,0,{
                        'partner_id' : id.id,
                    }])
            self.subjektif_partner_ids = ids
            
        string_objektif = ''
        string_subjektif = ''
        if self.perawat_id:
            self.perawat_ids = False
            #subjektif
            self.perawat_ids  = self.perawat_id
            string_subjektif += 'Nama : ' + str(self.perawat_id.name.name) + ', '
            string_subjektif += 'Umur : ' + str(self.perawat_id.age) + ', '
            string_subjektif += 'BB : ' + str(self.perawat_id.berat_badan) + ' kg,'
            string_subjektif += 'keadaan sakit : ' + str(self.perawat_id.keadaan_sakit) + ', '
            string_subjektif += 'kesadaran : ' + str(self.perawat_id.kesadaran) + ', '
            if self.perawat_id.keluhan_ids:
                string_subjektif += 'datang dengan : ' + str(self.perawat_id.kesadaran) + ', '
                for keluhan in self.perawat_id.keluhan_ids:
                    string_subjektif += str(keluhan.name + ', ')
            self.subjektif = string_subjektif
            
            #objektif
            string_objektif += 'IMT : ' + str(self.perawat_id.imt) + ', '
            string_objektif += 'Nafas : ' + str(self.perawat_id.nafas) + ', '
            string_objektif += 'Suhu Badan : ' + str(self.perawat_id.suhu_badan) + ', '
            string_objektif += 'Saturasi O2 CSpO2 : ' + str(self.perawat_id.saturasi) + ', '
            string_objektif += 'Interpretasi : ' + str(self.perawat_id.peringatan_interpretasi_imt) + ', '
            self.objektif = string_objektif
            
        if self.icpc_2_id:
            self.aspik_klinis = 'Diagnosis : %s' %str(self.icpc_2_id.name)
        
     
            


class SubjektifPartner(models.Model):
    _name = "subjektif.partner"
    
    subjektif_id = fields.Many2one(comodel_name='medik', string='subjektif', readonly=True)
    partner_id = fields.Many2one(comodel_name='partner', string='partner' , readonly=True)
    name = fields.Char(related='partner_id.name', string='name')
    nik = fields.Char(related='partner_id.nik', string='nik')
    sts_hubungan = fields.Many2one(related='partner_id.sts_hubungan', string='Staus Hubungan')
    keluhan_utama = fields.Char(related='partner_id.keluhan_utama', string='Keluhan Utana')
    


    

class ICPC(models.Model):
    _name = "icpc"
    
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    code_icd = fields.Char(string='ICD')
    
    def name_get(self, context=None):
        if context is None:
            context = {}
        res = []
        for record in self:
            name_get = "[%s] - %s" % (record.code, record.name)
            res.append((record.id, name_get))
        return res

class ICD(models.Model):
    _name = "icd"
    
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    
    def name_get(self, context=None):
        if context is None:
            context = {}
        res = []
        for record in self:
            name_get = "[%s] - %s" % (record.code, record.name)
            res.append((record.id, name_get))
        return res
    
    @api.model
    def name_search(self,name,args=None,operator='ilike',limit=100):
        args =  args or []
        if name:
            args = ['|',('name',operator,name),('code',operator,name)]
        categorys = self.search(args, limit=limit)
        return categorys.name_get()

       