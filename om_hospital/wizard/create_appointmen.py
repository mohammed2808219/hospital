from odoo import api, fields, models, _

class CreatelAppointmen(models.Model):
    _name = "create.appointmen.wizard"
    _description = "Create Appointmen Wizard"
    
    name = fields.Char(string="Name", required=True)
    hospital_id = fields.Many2one('hospital.manegement', string="Patient", required=True)