from odoo import api, fields, models, _

class PK21(models.Model):
    _name = "pk21"
    _description = "kode pk21"
    
    name=fields.Char(string="nama")
    name_Pertanyaan =fields.Char(string="Pertanyaan")
    kode=fields.Integer(string="kode")
    value= fields.Char(string="value")
    
    
    
    
    

            
    
    
    
    

