from decimal import Decimal

import marshmallow
import pytest

from calculator.adapters.services.operands import OperandsService


def test_operands_service_add_result(get_operands_service):
    assert get_operands_service.add(Decimal("4.5"), Decimal("5")) == 9.5


def test_operands_service_add_with_wrong_data_types(get_operands_service):
    with pytest.raises(marshmallow.exceptions.ValidationError):
        get_operands_service.add([], Decimal("5")) == 9.5
