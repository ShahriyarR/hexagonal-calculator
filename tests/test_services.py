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


def test_operands_service_multiply_result(get_operands_service):
    assert get_operands_service.multiply(Decimal("2.0"), Decimal("2.5")) == Decimal("5")
    assert get_operands_service.multiply(Decimal("2.0"), Decimal("2.5")) == Decimal(
        "5.0"
    )

    assert get_operands_service.multiply(7, 8) == 56
    assert get_operands_service.multiply(7, 0) == 0


def test_operands_service_multiply_with_wrong_data_types(get_operands_service):
    with pytest.raises(marshmallow.exceptions.ValidationError):
        get_operands_service.multiply([], Decimal("5")) == 9.5

    with pytest.raises(marshmallow.exceptions.ValidationError):
        assert get_operands_service.multiply(5, "str") == 9.5


def test_operands_service_divide_result(get_operands_service):
    assert get_operands_service.divide(Decimal("4.0"), Decimal("2.0")) == Decimal("2.0")
    assert get_operands_service.divide(Decimal("4.0"), Decimal("2")) == Decimal("2")

    assert get_operands_service.divide(56, 7) == 8
    assert get_operands_service.divide(7, 0) == 0


def test_operands_service_multiply_with_wrong_data_types(get_operands_service):
    with pytest.raises(marshmallow.exceptions.ValidationError):
        get_operands_service.divide([], Decimal("5")) == 9.5

    with pytest.raises(marshmallow.exceptions.ValidationError):
        assert get_operands_service.divide(5, "str") == 9.5
