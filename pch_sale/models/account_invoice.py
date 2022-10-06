# coding: utf-8
""" pch_sale """

from odoo import models, fields


class AccountInvoice(models.Model):
    """ Inherit account.invoice """
    _inherit = 'account.invoice'

    bank_account = fields.Many2one(comodel_name='account.journal', string="Bank Account")
