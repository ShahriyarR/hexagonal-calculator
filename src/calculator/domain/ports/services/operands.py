from abc import ABC, abstractmethod
from decimal import Decimal


class OperandsServiceInterface(ABC):
    def add(self, left: Decimal, right: Decimal) -> Decimal:
        return self._add(left, right)

    def subtract(self, left: Decimal, right: Decimal) -> Decimal:
        return self._subtract(left, right)

    @abstractmethod
    def _add(self, left: Decimal, right: Decimal) -> Decimal:
        raise NotImplementedError

    @abstractmethod
    def _subtract(self, left: Decimal, right: Decimal) -> Decimal:
        raise NotImplementedError
