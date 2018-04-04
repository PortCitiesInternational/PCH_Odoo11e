# coding: utf-8
""" pch_sale """

from odoo import models, fields


class SaleOrder(models.Model):
    """ Inherit sale.order """
    _inherit = 'sale.order'

    bank_account = fields.Many2one(comodel_name='account.journal', string="Bank Account")
