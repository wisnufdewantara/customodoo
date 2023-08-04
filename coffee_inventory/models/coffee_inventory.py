from odoo import models, api, fields, _
 
class Coffees(models.Model):
    _name = 'coffees.inventory'
 
    name = fields.Char("ID",required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
 
    coffee_name = fields.Char('Name',required=1)
    beans_to_coffee_conversionfactor = fields.Float(
       "Beans To Coffee Conversion Factor", required=1
    )
    short_description = fields.Char('Short Description')
    active = fields.Boolean('Active', help="If the active field is set to False, it will allow you to hide the account without removing it.", default=True)
    include_in_mix_bag = fields.Boolean('Include In Mix Bag' )
    roastery_id = fields.One2many('minimum.stock.levels.line', 'roastery', string='Roastery')
    created_date = fields.Datetime(string='Created Date', required=True, default=fields.Datetime.now)
    show_on_customer_dashboard = fields.Boolean('On Customer DashBoard')
#     @api.model
#     def create(self, vals):
#         if vals:
#             vals.update({
#                 'name': self.env['ir.sequence'].get('coffees.inventory')
#             })
#             print "dddddddddddddddddsdsdsdsdsd",vals['name']
#         
 
 
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('coffees.inventory') or _('New')
        return super(Coffees, self).create(vals)
class MinimumStockLevels(models.Model):
    _name = 'minimum.stock.levels.line'
     
     
     
    roastery = fields.Many2one('stock.warehouse',string="Roastery")
    quantity_in_gms = fields.Float("Quantity in gms")
    coffees_order_id = fields.Many2one('coffees.inventory', required=True)
     





     
# from odoo import models, api, fields, _
#  
#  
# class Coffees(models.Model):
#     _name = 'coffees.inventory'
#  
#  
#     name = fields.Char("ID",required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
#  
#     coffee_name = fields.Char('Name',required=1)
#     beans_to_coffee_conversionfactor = fields.Float(
#        "Beans To Coffee Conversion Factor", required=1
#     )
#     short_description = fields.Char('Short Description')
#     active = fields.Boolean('Active', help="If the active field is set to False, it will allow you to hide the account without removing it.", default=True)
#     include_in_mix_bag = fields.Boolean('Include In Mix Bag' )
#     msl_line_id = fields.One2many('minimum.stock.levels.line', 'roasteryId', string='Roastery Lines')
#     created_date = fields.Datetime(string='Created Date', required=True, default=fields.Datetime.now)
#     show_on_customer_dashboard = fields.Boolean('On Customer DashBoard')
# #     @api.model
# #     def create(self, vals):
# #         if vals:
# #             vals.update({
# #                 'name': self.env['ir.sequence'].get('coffees.inventory')
# #             })
# #             print "dddddddddddddddddsdsdsdsdsd",vals['name']
# #         
#  
#  
#     @api.model
#     def create(self, vals):
#         if vals.get('name', _('New')) == _('New'):
#             vals['name'] = self.env['ir.sequence'].next_by_code('coffees.inventory') or _('New')
#         return super(Coffees, self).create(vals)
# class MinimumStockLevels(models.Model):
#     _name = 'minimum.stock.levels.line'
#      
#      
# #     roasteryId = fields.Selection([(1,'Delhi Roastery'),
# #                                   (2,'Mumbai Roastery')], string="Roastery") 
#     roasteryId = fields.Many2one('stock.warehouse',string="Roastery")
#     quantity_in_gms = fields.Float("Quantity in gms")
#     coffees_order_id = fields.Many2one('coffees.inventory', required=True)
#     
#     
#     
#     
