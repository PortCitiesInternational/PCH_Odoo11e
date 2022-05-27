# coding: utf-8
""" Account Move """

from odoo import models, fields


class AccountMove(models.Model):
    """ Inherit account.move """

    _inherit = 'account.move'

    bank_account = fields.Many2one('account.journal', string="Bank Account")
