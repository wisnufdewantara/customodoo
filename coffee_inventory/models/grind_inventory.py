from odoo import models, api, fields, _

class Grind(models.Model):
    _name = 'grind.inventory'

    name = fields.Char("ID",readonly=True)
    grind_name = fields.Char("Name",required=1)
    active = fields.Boolean('Active', default=True)
    created_date = fields.Datetime(string='Created Date', required=True, default=fields.Datetime.now)
    
