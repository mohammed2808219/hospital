from odoo import api, fields, models, _

class Medik(models.Model):
    _name = "subjektif"
    
    
    perawat_id =fields.Many2one(comodel_name='hospital.perawat' ,string='name')
    subjektif = fields.Text(string='Subjektif')
    subjektif_dokter = fields.Text()
    riwayat_penyakit = fields.Text(string="Riwayat Penyakit Dahulu dan Pengobatan")
    riwayat_personal = fields.Text(string="Riwayat Personal Sosial dan Linkungan")
    riwayat_keluarga = fields.Text(string='keluarga')
    alergi = fields.Text(string='Alergen')
    
    
    @api.onchange('perawat_id')
    def _onchange_subjektif(self):
        string_subjektif = ''
        perawat_obj = self.env['hospital.perawat'].sudo().browse(self.perawat_id.id)
        if perawat_obj:
            import ipdb; ipdb.set_trace()
            string_subjektif += 'Nama : ' + str(perawat_obj.nama_kk.name) + ', '
            string_subjektif += 'Umur : ' + str(perawat_obj.age) + ', '
            string_subjektif += 'BB : ' + str(perawat_obj.berat_badan) + ' kg,'
            string_subjektif += 'keadaan sakit : ' + str(perawat_obj.keadaan_sakit) + ', '
            string_subjektif += 'kesadaran : ' + str(perawat_obj.kesadaran) + ', '
            if perawat_obj.keluhan_ids:
                string_subjektif += 'datang dengan : ' + str(perawat_obj.kesadaran) + ', '
                for keluhan in perawat_obj.keluhan_ids:
                    string_subjektif += str(keluhan.name + ', ')
        self.subjektif = string_subjektif
            
            
            
        
  