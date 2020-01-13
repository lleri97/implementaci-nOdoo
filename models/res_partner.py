# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
     _inherit = 'res.partner'
     
     subscription_ids_customer = fields.One2many(
        'subscription.subscription',
        'customer',
        string="Contracts"
    )

    