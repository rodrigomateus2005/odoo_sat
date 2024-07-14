import logging
from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _name = 'pos.order'
    _inherit = 'pos.order'

    def write(self, vals):
        _logger.info('passou: write ')
        return super(PosOrder, self).write(vals)