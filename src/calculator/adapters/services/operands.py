from contextlib import contextmanager
from decimal import Decimal

from calculator.domain.model.model import Operands, operands_factory
from calculator.domain.model.schemas import OperandsCreateDTO
from calculator.domain.ports.services.operands import OperandsServiceInterface


@contextmanager
def operands_factory_validation(left: Decimal, right: Decimal) -> Operands:
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

    def _divide(self, left: Decimal, right: Decimal) -> Decimal:
        with operands_factory_validation(left, right) as operands:
            return operands.left / operands.right
