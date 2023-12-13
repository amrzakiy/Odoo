from odoo import api, fields, models

class TravelPackage(models.Model):
    _name = 'travel.package'
    _description = 'Travel Package'

    ref = fields.Char(string='Referensi', readonly=True, default='-')
    berangkat = fields.Date(string='Tanggal Berangkat', required=True, readonly=True, states={'draft' : [('readonly', False)]})
    kembali = fields.Date(string='Tanggal Kembali', required=True, readonly=True, states={'draft' : [('readonly', False)]})
    product_sale_id = fields.Many2one('product.template', string='Sale', domain=['|', ('categ_id', '=', 'umroh'), ('categ_id.name', 'ilike', 'umroh')], required=True, readonly=True, states={'draft' : [('readonly', False)]})
    product_package_id = fields.Many2one('product.template', string='Package', domain=['|', ('categ_id', '=', 'umroh'), ('categ_id.name', 'ilike', 'umroh')], required=True, readonly=True, states={'draft' : [('readonly', False)]})
    quota = fields.Integer(string='Quota', default=20, readonly=True, states={'draft' : [('readonly', False)]})
    progress = fields.Float(string='Quota Progress') 
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done')], string='Status', default='draft')

    def package_draft(self):
        self.write({'state': 'draft'})
 
    def package_open(self):
        self.write({'state': 'confirm'})
 
    def package_done(self):
        self.write({'state': 'done'})
        
    progress = fields.Float(string='Quota Progress')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('travel.package')
        return super(TravelPackage, self).create(vals)
    
    hotels_line = fields.One2many('hotels.line', 'package_id', string='Hotel')

class HotelsLine(models.Model):
    _name = 'hotels.line'
    
    package_id = fields.Many2one('travel.package', string='Hotel')

    partner_id = fields.Many2one('res.partner', string='Nama Hotel', required=True, domain=[('hotel', '=', True)])
    check_in = fields.Date(string='Check In Hotel', required=True)
    check_out = fields.Date(string='Check Out Hotel', required=True)
    kota = fields.Char(string='Kota', related='partner_id.city', readonly=True)