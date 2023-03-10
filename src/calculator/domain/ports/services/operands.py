from abc import ABC, abstractmethod
from decimal import Decimal


class OperandsServiceInterface(ABC):
    def add(self, left: Decimal, right: Decimal) -> Decimal:
        return self._add(left, right)

    def subtract(self, left: Decimal, right: Decimal) -> Decimal:
        return self._subtract(left, right)

    def multiply(self, left: Decimal, right: Decimal) -> Decimal:
        return self._multiply(left, right)

    def divide(self, left: Decimal, right: Decimal) -> Decimal:
        return self._divide(left, right)

    @abstractmethod
    def _add(self, left: Decimal, right: Decimal) -> Decimal:
        raise NotImplementedError

    @abstractmethod
    def _subtract(self, left: Decimal, right: Decimal) -> Decimal:
        raise NotImplementedError

    @abstractmethod
    def _multiply(self, left: Decimal, right: Decimal) -> Decimal:
        raise NotImplementedError

    @abstractmethod
    def _divide(self, left: Decimal, right: Decimal) -> Decimal:
        raise NotImplementedError
