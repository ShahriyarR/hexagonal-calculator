import pytest
from tests.fake_repository import FakeCalculationRepository

from calculator.adapters.services.operands import OperandsService
from calculator.domain.model.model import calculation_factory
from calculator.domain.model.schemas import CalculationCreateDTO


@pytest.fixture(scope="module")
def get_operands_service():
    return OperandsService()


@pytest.fixture(scope="module")
def get_fake_repository():
    return FakeCalculationRepository()


@pytest.fixture(scope="module")
def get_calculation_model_object():
    schema_ = CalculationCreateDTO()
    result_ = schema_.load({"left": 4.0, "right": 5.0, "action": "add", "result": 9.0})
    return calculation_factory(**result_)
