import decimal
from decimal import Decimal

import marshmallow
import pytest

from calculator.domain.model.model import (
    Operands,
    calculation_factory,
    operands_factory,
)
from calculator.domain.model.schemas import CalculationCreateDTO, OperandsCreateDTO


def test_if_operands_is_created():
    schema_ = OperandsCreateDTO()
    result = schema_.load({"left": 4, "right": 5})
    model_ = Operands(**result)
    assert model_.left == 4 and model_.right == 5


def test_if_operands_is_created_with_factory():
    schema_ = OperandsCreateDTO()
    result = schema_.load({"left": 4, "right": 5})
    model_ = operands_factory(**result)
    assert model_.left == 4 and model_.right == 5


def test_if_operands_is_created_with_factory_and_with_wrong_types():
    with pytest.raises(decimal.InvalidOperation):
        operands_factory(**{"left": [], "right": 5.5})


def test_if_operands_create_dto_created():
    schema_ = OperandsCreateDTO()
    result = schema_.load({"left": 4, "right": 5})
    assert {"right": Decimal("5"), "left": Decimal("4")} == result


def test_if_operands_create_dto_can_be_created_with_wrong_types():
    schema_ = OperandsCreateDTO()
    result = schema_.load({"left": 4.5, "right": 5.0})
    assert {"left": Decimal("4.5"), "right": Decimal("5.0")} == result
    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema_.load({"left": [], "right": 5.0})

    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema_.load({"left": 5.5, "right": "fake"})


def test_if_operands_create_dto_can_be_created_with_extra_fields():
    schema_ = OperandsCreateDTO()
    result = schema_.load({"left": 4.5, "right": 5.0, "fake": 55})
    # So the "fake" data should be excluded
    assert {"left": Decimal("4.5"), "right": Decimal("5.0")} == result


def test_if_operands_create_dto_can_be_created_with_wrong_field_names():
    schema_ = OperandsCreateDTO()
    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema_.load({"lft": 4.5, "right": 5.0})


def test_if_operands_create_dto_can_be_created_with_missing_field_names():
    schema_ = OperandsCreateDTO()
    with pytest.raises(marshmallow.exceptions.ValidationError):
        schema_.load({"left": 4.5})


def test_if_calculation_model_created_with_factory():
    schema_ = CalculationCreateDTO()
    result_ = schema_.load({"left": 4.0, "right": 5.0, "action": "add", "result": 9.0})
    result = calculation_factory(**result_)
    assert result.action == "add"
    assert result.result == 9.0


def test_if_calculation_model_created_with_factory_with_wrong_action():
    schema_ = CalculationCreateDTO()
    # This should fail at schema level
    with pytest.raises(marshmallow.exceptions.ValidationError):
        _ = schema_.load({"left": 2.0, "right": 2.3, "action": "fake", "result": 4.6})

    with pytest.raises(ValueError):
        result = schema_.load(
            {"left": 2.0, "right": 2.3, "action": "add", "result": 4.6}
        )
        # If somebody changes the action and tries to inject fake data; it will fail at model level
        result["action"] = "fake"
        calculation_factory(**result)
