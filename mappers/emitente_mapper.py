from models.pos_order import PosOrder
from satcfe.entidades import Emitente

class EmitenteMapper:

    def __init__(self, pos_order: PosOrder):
        self.pos_order = pos_order;
    
    def map(self) -> Emitente:
        Emitente(
            CNPJ=self.pos_order.get_company().l10n_br_cpf_code,
            IE=self.pos_order.get_company().l10n_br_ie_code
        )