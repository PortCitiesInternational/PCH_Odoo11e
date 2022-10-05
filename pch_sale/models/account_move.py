""" Account Move """
from odoo import models, fields


class AccountMove(models.Model):
    """ Inherit Account Move """

    _inherit = 'account.move'

    bank_account = fields.Many2one('account.journal', string="Bank Account")
