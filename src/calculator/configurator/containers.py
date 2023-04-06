from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from calculator.adapters.services.operands import OperandsService
from calculator.adapters.unit_of_works.calculation import (
    CalculationSqlAlchemyUnitOfWork,
)
from calculator.adapters.use_cases.calculate import CalculateUseCase
from calculator.configurator.settings import get_database_uri

db_uri = get_database_uri()
ENGINE = create_engine(db_uri)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "calculator.adapters.use_cases.calculate",
        ],
        packages=[
            "calculator.adapters.entrypoints.api",
        ]
    )

    DEFAULT_SESSION_FACTORY = lambda: sessionmaker(bind=ENGINE, autocommit=False)

    calculation_uow = providers.Factory(
        CalculationSqlAlchemyUnitOfWork, session_factory=DEFAULT_SESSION_FACTORY
    )

    operands_service = providers.Factory(OperandsService)

    calculate_use_case = providers.Factory(
        CalculateUseCase,
        uow=calculation_uow,
        service=operands_service,
    )
