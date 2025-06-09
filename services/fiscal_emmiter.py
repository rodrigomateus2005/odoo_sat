from abc import ABC, abstractmethod
from models.pos_order import PosOrder

class FiscalEmmiter(ABC):

    @abstractmethod
    def emmit(self, posOrder: PosOrder):
        pass