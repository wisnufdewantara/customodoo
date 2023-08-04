from odoo import models, api, fields, _

class Coffees(models.Model):
    _name = 'blends.inventory'
    
    blends_id = fields.Char("ID",readonly=True)
    name = fields.Char("NAME",required=True)
    pre_mix = fields.Boolean("Pre-Mix")
    
    
