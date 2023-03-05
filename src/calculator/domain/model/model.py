from dataclasses import dataclass
from decimal import Decimal

from calculator.domain.model.schemas import OperandsCreateDTO


@dataclass
class Operands:
    left: Decimal
    right: Decimal

    def __hash__(self):
        return hash(self.left + self.right)

    def __eq__(self, other):
        if not isinstance(other, Operands):
            return False
        return self.left == other.left and self.right == other.right


def operands_factory(**kwargs: dict[str]) -> Operands:
    schema_ = OperandsCreateDTO()
    model = Operands(**kwargs)
    schema_.dump(model)
    return model
