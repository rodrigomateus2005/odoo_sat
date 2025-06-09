from mappers.detalhamento_mapper import DetalhamentoMapper
from models.pos_order import PosOrder
from satcfe.entidades import Detalhamento

class DetalhamentosMapper:

    def __init__(self, pos_order: PosOrder):
        self.pos_order = pos_order;
    
    def map(self) -> list[Detalhamento]:
        return map(
            lambda item:
                DetalhamentoMapper(item).map()
            ,
            self.pos_order.get_itens()
        )