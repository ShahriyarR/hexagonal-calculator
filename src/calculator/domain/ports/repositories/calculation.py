from abc import ABC, abstractmethod

from calculator.domain.model import model


class CalculationRepositoryInterface(ABC):
    def __init__(self):
        self.seen = set()

    def add(self, calculation: model.Calculation):
        self._add(calculation)
        self.seen.add(calculation)

    def get(self, id_) -> model.Calculation:
        calculation = self._get(id_)
        if calculation:
            self.seen.add(calculation)
        return calculation

    def get_by_action(self, action: str) -> model.Calculation:
        calculation = self._get_by_action(action)
        if calculation:
            self.seen.add(calculation)
        return calculation

    def get_by_uuid(self, uuid: str) -> model.Calculation:
        calculation = self._get_by_uuid(uuid)
        if calculation:
            self.seen.add(calculation)
        return calculation

    def get_all(self) -> list[model.Calculation]:
        return self._get_all()

    @abstractmethod
    def _add(self, calculation: model.Calculation):
        raise NotImplementedError

    @abstractmethod
    def _get(self, id_) -> model.Calculation:
        raise NotImplementedError

    @abstractmethod
    def _get_by_action(self, action: str) -> model.Calculation:
        raise NotImplementedError

    @abstractmethod
    def _get_by_uuid(self, uuid: str) -> model.Calculation:
        raise NotImplementedError

    @abstractmethod
    def _get_all(self) -> list[model.Calculation]:
        raise NotImplementedError
