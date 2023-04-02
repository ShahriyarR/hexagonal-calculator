from decimal import Decimal

from dependency_injector.wiring import Provide

from calculator.domain.model.model import calculation_factory
from calculator.domain.model.schemas import CalculationCreateDTO
from calculator.domain.ports.services.operands import OperandsServiceInterface
from calculator.domain.ports.unit_of_works.calculation import (
    CalculationUnitOfWorkInterface,
)
from calculator.domain.ports.use_cases.calculate import CalculateUseCaseInterface


class CalculateUseCase(CalculateUseCaseInterface):
    def __init__(
        self,
        uow: CalculationUnitOfWorkInterface = Provide["calculation_uow"],
        service: OperandsServiceInterface = Provide["operands_service"],
    ):
        self.uow = uow
        self.service = service

    def _add(self, left: Decimal, right: Decimal):
        with self.uow:
            # calculate
            result = self.service.add(left, right)
            # save the information
            schema_ = CalculationCreateDTO()
            data_ = schema_.load(
                {"left": left, "right": right, "action": "add", "result": result}
            )
            model = calculation_factory(**data_)
            self.uow.calculation.add(model)
            self.uow.commit()

    def _subtract(self, left: Decimal, right: Decimal):
        with self.uow:
            # calculate
            result = self.service.subtract(left, right)
            # save the information
            schema_ = CalculationCreateDTO()
            data_ = schema_.load(
                {"left": left, "right": right, "action": "subtract", "result": result}
            )
            model = calculation_factory(**data_)
            self.uow.calculation.add(model)
            self.uow.commit()

    def _multiply(self, left: Decimal, right: Decimal):
        with self.uow:
            # calculate
            result = self.service.multiply(left, right)
            # save the information
            schema_ = CalculationCreateDTO()
            data_ = schema_.load(
                {"left": left, "right": right, "action": "multiply", "result": result}
            )
            model = calculation_factory(**data_)
            self.uow.calculation.add(model)
            self.uow.commit()

    def _divide(self, left: Decimal, right: Decimal):
        with self.uow:
            # calculate
            result = self.service.divide(left, right)
            # save the information
            schema_ = CalculationCreateDTO()
            data_ = schema_.load(
                {"left": left, "right": right, "action": "divide", "result": result}
            )
            model = calculation_factory(**data_)
            self.uow.calculation.add(model)
            self.uow.commit()
