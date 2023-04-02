from abc import ABC, abstractmethod
from decimal import Decimal

from calculator.domain.ports.services.operands import OperandsServiceInterface
from calculator.domain.ports.unit_of_works.calculation import (
    CalculationUnitOfWorkInterface,
)


class CalculateUseCaseInterface(ABC):
    @abstractmethod
    def __init__(
        self, uow: CalculationUnitOfWorkInterface, service: OperandsServiceInterface
    ):
        raise NotImplementedError

    def add(self, left: Decimal, right: Decimal):
        return self._add(left, right)

    def subtract(self, left: Decimal, right: Decimal):
        return self._subtract(left, right)

    def multiply(self, left: Decimal, right: Decimal):
        return self._multiply(left, right)

    @abstractmethod
    def _add(self, left: Decimal, right: Decimal):
        raise NotImplementedError

    @abstractmethod
    def _subtract(self, left: Decimal, right: Decimal):
        raise NotImplementedError

    def _multiply(self, left: Decimal, right: Decimal):
        raise NotImplementedError
