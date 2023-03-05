from contextlib import contextmanager
from decimal import Decimal
from typing import Generator

import icontract
from calculator.domain.model.model import operands_factory
from calculator.domain.model.schemas import OperandsCreateDTO
from calculator.domain.ports.services.operands import OperandsServiceInterface


@contextmanager
def operands_factory_validation(left: Decimal, right: Decimal) -> Generator:
    data_ = {"left": left, "right": right}
    result = OperandsCreateDTO().load(data_)
    yield operands_factory(**result)


class OperandsService(OperandsServiceInterface):
    def _add(self, left: Decimal, right: Decimal) -> Decimal:
        with operands_factory_validation(left, right) as operands:
            return operands.left + operands.right

    def _subtract(self, left: Decimal, right: Decimal) -> Decimal:
        with operands_factory_validation(left, right) as operands:
            return operands.left - operands.right

    def _multiply(self, left: Decimal, right: Decimal) -> Decimal:
        with operands_factory_validation(left, right) as operands:
            return operands.left * operands.right

    @icontract.require(lambda left, right: right != 0)
    def _divide(self, left: Decimal, right: Decimal) -> Decimal:
        with operands_factory_validation(left, right) as operands:
            return operands.left / operands.right
