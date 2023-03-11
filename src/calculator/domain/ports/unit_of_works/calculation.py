from abc import ABC, abstractmethod

from calculator.domain.ports.repositories.calculation import (
    CalculationRepositoryInterface,
)


class CalculationUnitOfWorkInterface(ABC):
    calculation: CalculationRepositoryInterface

    def __enter__(self) -> "CalculationUnitOfWorkInterface":
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            self.rollback()

    def commit(self):
        self._commit()

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError
