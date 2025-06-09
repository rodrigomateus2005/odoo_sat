from mappers.destinatario_mapper import DestinatarioMapper
from mappers.detalhamentos_mapper import DetalhamentosMapper
from mappers.emitente_mapper import EmitenteMapper
from models.pos_order import PosOrder
from satcomum import constantes
from satcfe.entidades import CFeVenda

class CFeVendaMapper:

    def __init__(self, pos_order: PosOrder):
        self.pos_order = pos_order;
    
    def map(self) -> CFeVenda:
        CFeVenda(
            CNPJ=self.pos_order.get_cnpj(),
            signAC=constantes.ASSINATURA_AC_TESTE,
            numeroCaixa=2,
            emitente=EmitenteMapper(self.pos_order).map(),
            destinatario=DestinatarioMapper(self.pos_order).map(),
            detalhamentos=DetalhamentosMapper(self.pos_order).map()
        )