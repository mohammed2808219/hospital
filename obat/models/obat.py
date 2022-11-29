from odoo import api, fields, models, _

class Obat(models.Model):
    _name = "obat"
    _description = "Configuration Obat"
    
    name=fields.Char(string="name")
    kode =fields.Char(string="Kode")
    nama_dagang =fields.Char(string="Nama Dagang")
    kdoe_pabrik=fields.Char(string="Kode Pabrik")
    harga_beli=fields.Float(string="Harga Beli")
    harga_jual= fields.Float(string="Harga Jual")
    
    
    
    
    

            
    
    
    
    

