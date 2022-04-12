""" Sale Order """
from odoo import models, fields


class SaleOrder(models.Model):
    """ Inherit Sale Order """

    _inherit = 'sale.order'

    bank_account = fields.Many2one('account.journal', string="Bank Account")
