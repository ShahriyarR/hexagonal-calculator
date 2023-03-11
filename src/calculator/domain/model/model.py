import datetime
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

from ulid import ULID

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


class ActionType(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    DIVIDE = "divide"
    MULTIPLY = "multiply"


@dataclass
class Calculation:
    uuid: str
    left: Decimal
    right: Decimal
    action: str
    result: Decimal
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __hash__(self):
        return hash(self.uuid)


def calculation_factory(uuid, left, right, action, result, created_at, updated_at):
    return Calculation(
        uuid=uuid,
        left=left,
        right=right,
        action=ActionType[action].value,
        result=result,
        created_at=created_at,
        updated_at=updated_at,
    )


def operands_factory(**kwargs: dict[str]) -> Operands:
    schema_ = OperandsCreateDTO()
    model = Operands(**kwargs)
    schema_.dump(model)
    return model
