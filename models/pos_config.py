from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PosConfig(models.Model):
    _inherit = 'pos.config'

    sat_key = fields.Char(string='Sat Key', help='The sat number key.')