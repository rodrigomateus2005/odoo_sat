from decimal import Decimal
from typing import List
from models.pos_order import PosOrder
from satcfe.entidades import Detalhamento, ProdutoServico, Imposto, ICMSSN102, PISSN, COFINSSN

from odoo.addons.stock.models.stock_picking import Picking
from odoo.addons.stock.models.product import Product
from odoo.addons.product.models.product_product import ProductProduct

class DetalhamentoMapper:

    def __init__(self, item: Picking):
        self.item = item;
    
    def map(self) -> List[Detalhamento]:
        Detalhamento(
            produto=ProdutoServico(
                    cProd=self.get_product().code,
                    xProd=self.get_product()._compute_display_name(),
                    CFOP='5102',
                    uCom='UN',
                    qCom=Decimal('1.0000'),
                    vUnCom=Decimal('5.75'),
                    indRegra='A'),
            imposto=Imposto(
                    icms=ICMSSN102(Orig='2', CSOSN='500'),
                    pis=PISSN(CST='49'),
                    cofins=COFINSSN(CST='49')))
        
    def get_product(self) -> ProductProduct | Product:
        return self.get_product()