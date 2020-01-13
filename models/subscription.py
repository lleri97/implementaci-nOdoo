# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'Abstract Recurring Contract'
    
    name = fields.Char(
                       required=True,
                       compute="subscription_name_definition"
                       )
    customer = fields.Many2one(
                               'res.partner',
                               string='Customer'
                               )
    agent = fields.Many2one(
                            'res.users',
                            string='Commercial Agent'
                            )
    active = fields.Boolean(
                            default=True,
                            string='Activo'
                            )
    plan = fields.Selection(
                            string="Plan",
                            selection=[
                            ('mensual', 'Mensual'),
                            ('semestral', 'Semestral'),
                            ('anual', 'Anual'),
                            ],
                            default='anual'
                            )
    products = fields.Many2many(
                                'product.product',
                                String='Product'
                                )
    
    automatic_price = fields.Boolean(
                                     string="Auto-price?",
                                     default=True,
                                     help="If this is marked, the price will be obtained automatically. If not, you will be "
                                     "able to introduce a manual price"
                                     )
    price = fields.Float(
                         string='Price',
                         compute="_compute_price"
                         )
    
    specific_price = fields.Float(
                                    string="Price s"
                                   )
    
    date_start = fields.Date(
                             default=fields.Date.today,
                             string='Date Start'
                             )
    date_end = fields.Date(
                           compute="calculate_date_end",
                           string="Date End",
                           index=True
                           )

    @api.depends('customer', 'date_start')
    def subscription_name_definition(self):
        self.name = ''
        self.name = self.customer + self.date_start
        
    @api.depends('plan')
    def calculate_date_end(self):
        if(self.plan == mensual):
            return (date_start + relativedelta(days=30))
        if(self.plan == semestral):
            return (date_start + relativedelta(months=6))
        if(self.plan == anual):
            return (date_start + relativedelta(months=12))
     
    @api.depends('automatic_price', 'product_id')
    def _compute_price(self):
        if automatic_price:
            product = product_id
            price = product.price
        else:
            price = specific_price
        
        
    
        