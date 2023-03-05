from abc import ABC, abstractmethod
from decimal import Decimal


class OperandsServiceInterface(ABC):
    def add(self, left: Decimal, right: Decimal) -> Decimal:
        return self._add(left, right)

    @abstractmethod
    def _add(self, left: Decimal, right: Decimal) -> Decimal:
        raise NotImplementedError
