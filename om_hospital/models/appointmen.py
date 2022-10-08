from odoo import api, fields, models, _

class HospitalAppointmen(models.Model):
    _name = "hospital.appointmen"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointmen"
    
    name = fields.Char(string="Order Reference", required=True, copy=False, 
                            readonly=True, default=lambda self: _('New'))
    hospital_id = fields.Many2one('hospital.manegement', string="Patient", required=True, tracking= True)
    age = fields.Integer(string="Age", related='hospital_id.age', tracking= True)
    gender= fields.Selection([ ('male', 'Male'), ('female', 'Female'), ], required=True, tracking= True) 
    note= fields.Text(string="Description", tracking= True)
    state = fields.Selection([ ('draft' , 'Draft'), ('confirm' , 'Confirmed'), ('done' , 'Done'), ('cancel' , 'Cancelled'), ], default='draft', string="Status")
    date_appointmen = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")


    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"
        
    def action_cancel(self):
        self.state = "cancel"

    @api.model
    def create(self,vals):
        if not vals.get('note'):
            vals['note'] = "new description"
        if vals.get('name', _('New')) == _('New'):
            vals['name']= self.env['ir.sequence'].next_by_code('hospital.appointmen') or _('New')
        res = super(HospitalAppointmen, self).create(vals)
        return res

    @api.onchange('hospital_id')
    def onchange_hospital_id(self):
        if self.hospital_id:
            if self.hospital_id.gender:
                self.gender = self.hospital_id.gender
            if self.hospital_id.note:
                self.note = self.hospital_id.note
        else:
            self.gender = ''
            self.note = ''