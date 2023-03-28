from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from calculator.adapters.unit_of_works.calculation import (
    CalculationSqlAlchemyUnitOfWork,
)
from calculator.configurator.settings import get_database_uri

db_uri = get_database_uri()
ENGINE = create_engine(db_uri)


class Container(containers.DeclarativeContainer):
    DEFAULT_SESSION_FACTORY = lambda: sessionmaker(bind=ENGINE, autocommit=False)

    calculation_uow = providers.Factory(
        CalculationSqlAlchemyUnitOfWork, session_factory=DEFAULT_SESSION_FACTORY
    )
