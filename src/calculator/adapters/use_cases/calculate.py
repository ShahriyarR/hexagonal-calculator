from decimal import Decimal

from calculator.domain.ports.services.operands import OperandsServiceInterface
from calculator.domain.ports.unit_of_works.calculation import (
    CalculationUnitOfWorkInterface,
)
from calculator.domain.ports.use_cases.calculate import CalculateUseCaseInterface


class CalculateUseCase(CalculateUseCaseInterface):
    def __init__(
        self, uow: CalculationUnitOfWorkInterface, service: OperandsServiceInterface
    ):
        self.uow = uow
        self.service = service

    def _add(self, left: Decimal, right: Decimal):
        ...
