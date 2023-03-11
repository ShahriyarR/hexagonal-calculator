import random

from calculator.domain.model import model
from calculator.domain.ports.repositories.calculation import (
    CalculationRepositoryInterface,
)


class FakeCalculationRepository(CalculationRepositoryInterface):
    def __init__(self):
        super().__init__()
        self.database = {}

    def _add(self, calculation: model.Calculation):
        id_ = random.randint(10, 100)
        self.database[id_] = calculation

    def _get(self, id_: int) -> model.Calculation:
        return self.database[id_]

    def _get_by_uuid(self, uuid: str) -> model.Calculation:
        for val in self.database.values():
            if val.uuid == uuid:
                return val

    def _get_by_action(self, action: str) -> model.Calculation:
        for val in self.database.values():
            if val.action == action:
                return val

    def _get_all(self) -> list[model.Calculation]:
        return self.database
