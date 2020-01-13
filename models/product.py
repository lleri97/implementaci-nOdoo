# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
     _inherit = 'product.product'
     
     subscription_ids = fields.Many2many(
        'subscription.subscription',
        string="Contracts"
    )

    