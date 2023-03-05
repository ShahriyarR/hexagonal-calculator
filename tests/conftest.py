import pytest

from calculator.adapters.services.operands import OperandsService


@pytest.fixture(scope="module")
def get_operands_service():
    return OperandsService()
