from models.pos_order import PosOrder
from satcfe.entidades import Destinatario

class DestinatarioMapper:

    def __init__(self, pos_order: PosOrder):
        self.pos_order = pos_order;
    
    def map(self) -> Destinatario:
        Destinatario(
            CPF=self.pos_order.get_customer().l10n_br_cpf_code,
            xNome=self.pos_order.get_customer().name
        )