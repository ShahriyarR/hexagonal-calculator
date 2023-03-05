from decimal import Decimal

from calculator.domain.model.model import operands_factory
from calculator.domain.model.schemas import OperandsCreateDTO
from calculator.domain.ports.services.operands import OperandsServiceInterface


class OperandsService(OperandsServiceInterface):
    def _add(self, left: Decimal, right: Decimal) -> Decimal:
        data_ = {"left": left, "right": right}
        result = OperandsCreateDTO().load(data_)
        operands = operands_factory(**result)
        return operands.left + operands.right
