from decimal import Decimal

import marshmallow
import pytest
from calculator.domain.model.model import Operands, operands_factory
from calculator.domain.model.schemas import OperandsCreateDTO


def test_if_operands_is_created():
    model_ = Operands(4, 5)
    assert model_.left == 4 and model_.right == 5


def test_if_operands_is_created_with_factory():
    model_ = operands_factory(4, 5)
    assert model_.left == 4 and model_.right == 5


def test_if_operands_is_created_with_wrong_types():
    model_ = operands_factory("boom", 5.5)
    assert model_.left == "boom" and model_.right == 5.5


def test_if_operands_create_dto_created():
    schema_ = OperandsCreateDTO()
    result = schema_.load({"left": 4, "right": 5})
    assert {'right': Decimal('5'), 'left': Decimal('4')} == result


def test_if_operands_create_dto_can_be_created_with_wrong_types():
    schema_ = OperandsCreateDTO()
    result = schema_.load({"left": 4.5, "right": 5.0})
    assert {"left": Decimal("4.5"), "right": Decimal("5.0")} == result
    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema_.load({"left": [], "right": 5.0})

    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema_.load({"left": 5.5, "right": "fake"})

