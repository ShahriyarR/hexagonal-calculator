from calculator.domain.ports.unit_of_works.calculation import (
    CalculationUnitOfWorkInterface,
)
from tests.fake_repository import FakeCalculationRepository


class FakeCalculationUnitOfWork(CalculationUnitOfWorkInterface):
    def __init__(self):
        self.committed = False

    def __enter__(self):
        self.calculation = FakeCalculationRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        self.committed = True

    def rollback(self):
        # because we don't care
        pass
