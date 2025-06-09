import logging
from odoo import api, fields, models, tools, _
from odoo.addons.point_of_sale.models import pos_order
from odoo.addons.point_of_sale.models.pos_session import PosSession
from odoo.addons.l10n_br.models.res_company import ResCompany
from odoo.addons.l10n_br.models.res_partner import ResPartner as BrResPartner
from odoo.addons.account.models.partner import ResPartner
from odoo.addons.base.models.res_partner import Partner
from odoo.addons.stock.models.stock_picking import Picking


_logger = logging.getLogger(__name__)

class PosOrder(pos_order.PosOrder):
    _name = 'pos.order'
    _inherit = 'pos.order'

    def write(self, vals):
        _logger.info('passou: write ')
        return super(PosOrder, self).write(vals)
    
    def get_session(self) -> PosSession:
        return self.session_id
    
    def get_company(self) -> ResCompany:
        return self.get_session().company_id
    
    def get_cnpj(self) -> str:
        return self.get_company().l10n_br_cpf_code
    
    def get_customer(self) -> Partner | ResPartner | BrResPartner:
        return self.partner_id
    
    def get_itens(self) -> list[Picking]:
        return self.picking_ids
    