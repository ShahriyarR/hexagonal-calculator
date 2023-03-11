from typing import Callable, Any

from calculator.adapters.repositories.calculation import CalculationSqlAlchemyRepository
from calculator.domain.ports.unit_of_works.calculation import CalculationUnitOfWorkInterface
from sqlalchemy.orm import Session


class CalculationSqlAlchemyUnitOfWork(CalculationUnitOfWorkInterface):

    def __init__(self, session_factory: Callable[[], Any]):
        self.session_factory = session_factory()

    def __enter__(self):
        self.session: Session = self.session_factory()
        self.calculation = CalculationSqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()