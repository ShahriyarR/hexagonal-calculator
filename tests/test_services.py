from decimal import Decimal

import marshmallow
import pytest

from calculator.adapters.services.operands import OperandsService


def test_operands_service_add_result():
    operand = OperandsService()
    assert operand.add(Decimal("4.5"), Decimal("5")) == 9.5


def test_operands_service_add_with_wrong_data_types():
    operand = OperandsService()
    with pytest.raises(marshmallow.exceptions.ValidationError):
        operand.add([], Decimal("5")) == 9.5
