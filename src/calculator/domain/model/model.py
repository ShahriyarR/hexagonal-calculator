from dataclasses import dataclass
from decimal import Decimal


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


def operands_factory(left: int, right: int) -> Operands:
    return Operands(left=left, right=right)
