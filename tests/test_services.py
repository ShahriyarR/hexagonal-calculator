from decimal import Decimal

import marshmallow
import pytest


def test_operands_service_add_result(get_operands_service):
    assert get_operands_service.add(Decimal("4.5"), Decimal("5.5")) == Decimal("10")
    assert get_operands_service.add(Decimal("4.5"), Decimal("6.1")) == Decimal("10.6")
    assert get_operands_service.add(7, 8) == 15
    assert get_operands_service.add(7.5, 8) == 15.5


def test_operands_service_add_with_wrong_data_types(get_operands_service):
    with pytest.raises(marshmallow.exceptions.ValidationError):
        get_operands_service.add([], Decimal("5")) == 9.5

    with pytest.raises(marshmallow.exceptions.ValidationError):
        assert get_operands_service.add(5, "str") == 9.5


def test_operands_service_subtract_result(get_operands_service):
    assert get_operands_service.subtract(Decimal("4.5"), Decimal("5.5")) == Decimal(
        "-1"
    )
    assert get_operands_service.subtract(Decimal("4.5"), Decimal("6.1")) == Decimal(
        "-1.6"
    )
    assert get_operands_service.subtract(7, 8) == -1
    assert get_operands_service.subtract(7.5, 8) == -0.5


def test_operands_service_subtract_with_wrong_data_types(get_operands_service):
    with pytest.raises(marshmallow.exceptions.ValidationError):
        get_operands_service.subtract([], Decimal("5")) == 9.5

    with pytest.raises(marshmallow.exceptions.ValidationError):
        assert get_operands_service.subtract(5, "str") == 9.5
