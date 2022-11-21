from odoo import api, fields, models, _
class HospitalProfile(models.Model):
    _name = "hospital.manegement"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char(string="Hospital Name", tracking= True)
    email= fields.Char(string="email", tracking= True)
    age = fields.Integer(string="Age", tracking= True)
    phone= fields.Char("phone", tracking= True)
    note= fields.Text(string="Description", tracking= True)
    gender= fields.Selection([ ('male', 'Male'), ('female', 'Female'), ], required=True, default='male', tracking= True) 
    state = fields.Selection([ ('draft' , 'Draft'), ('confirm' , 'Confirmed'), ('done' , 'Done'), ('cancel' , 'Cancelled'), ], default='draft', string="Status")
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    reference= fields.Char(string="Order Reference", required=True, copy=False, 
                            readonly=True, default=lambda self: _('New'))
    appointmen_count = fields.Integer(string="Appointmen Count", compute="_compute_appointmen_count")

    def _compute_appointmen_count(self):
        for rec in self:
            appointmen_counts = self.env['hospital.appointmen'].search_count([('hospital_id', '=', rec.id)])
            rec.appointmen_count = appointmen_counts

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
        if vals.get('name'):
                vals['name'] = vals['name'].upper()
        if not vals.get('note'):
            vals['note'] = "new description"
        if vals.get('reference', _('New')) == _('New'):
            vals['reference']= self.env['ir.sequence'].next_by_code('hospital.manegement') or _('New')
        res = super(HospitalProfile, self).create(vals)
        return res