import contextlib

import pytest
import pytest_asyncio
import sqlalchemy
from httpx import AsyncClient

from calculator.adapters.db.orm import start_mappers
from calculator.adapters.entrypoints.api.app import app, create_app
from calculator.adapters.services.operands import OperandsService
from calculator.adapters.use_cases.calculate import CalculateUseCase
from calculator.domain.model.model import calculation_factory
from calculator.domain.model.schemas import CalculationCreateDTO
from tests.fake_container import FakeContainer
from tests.fake_repository import FakeCalculationRepository
from tests.fake_uow import FakeCalculationUnitOfWork


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


@pytest.fixture(scope="module")
def get_calculation_model_object_with_subtract():
    schema_ = CalculationCreateDTO()
    result_ = schema_.load(
        {"left": 4.0, "right": 5.0, "action": "subtract", "result": 9.0}
    )
    return calculation_factory(**result_)


@pytest.fixture(scope="module")
def get_fake_uow():
    return FakeCalculationUnitOfWork()


@pytest.fixture(scope="module")
def get_fake_container():
    # Start ORM mapper
    with contextlib.suppress(sqlalchemy.exc.ArgumentError):
        start_mappers()

    # Truncate table
    uow = FakeContainer.calculation_uow()
    with uow:
        uow.session.execute(sqlalchemy.text("DELETE FROM calculation"))
        uow.commit()

    return FakeContainer()


@pytest.fixture(scope="module")
def get_calculate_use_case():
    return CalculateUseCase()


@pytest_asyncio.fixture()
async def client():
    async with AsyncClient(
        app=app, base_url="http://0.0.0.0:8000/calculate/"
    ) as client:
        yield client


@pytest.fixture(scope="module")
def get_flask_app():
    app_ = create_app()
    yield app_
    app_.container.unwire()


@pytest.fixture(scope="module")
def get_flask_client(get_flask_app):
    return get_flask_app.test_client()
