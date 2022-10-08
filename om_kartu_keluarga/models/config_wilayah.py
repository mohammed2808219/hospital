import code
from unicodedata import name
from odoo.exceptions import Warning, ValidationError
from odoo import api, fields, models, _

    
class country_state(models.Model):
    _name="country.state"
    _description="Provinsi Table"
    
    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    
class city(models.Model):
    _name="city"
    _description="Kota kabupaten Table"
    
    name=fields.Char(string="Name")
    code=fields.Char(string="Code")
    active= fields.Boolean(string="Active")
    state_id=fields.Many2one('country.state',string="Provinsi")
    
class kecamatan(models.Model):
    _name="kecamatan"
    _description="Kecamatan Table"
    
    name=fields.Char(string="Name")
    code=fields.Char(string="Code")
    active= fields.Boolean(string="Active")
    city_id=fields.Many2one('city',string="Kota Kabupaten")
    
class kelurahan(models.Model):
    _name="kelurahan"
    _description="Kelurahan Table"
    
    name=fields.Char(string="Name")
    code=fields.Char(string="Code")
    kecamatan_id = fields.Many2one('kecamatan',string='Kecamatan')
    zip = fields.Char(string='Kode Pos')
    active= fields.Boolean(string="Active")
    