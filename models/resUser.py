# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUser(models.Model):
     _inherit = 'res.users'
     
     subscription_ids_comercial = fields.One2many(
        'subscription.subscription',
        string="Contracts"
    )
    
    