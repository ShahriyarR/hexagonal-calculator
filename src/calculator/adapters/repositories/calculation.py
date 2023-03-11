from calculator.domain.ports.repositories.calculation import CalculationRepositoryInterface
from calculator.domain.model import model


class CalculationSqlAlchemyRepository(CalculationRepositoryInterface):

    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, calculation: model.Calculation):
        self.session.add(calculation)

    def _get(self, id_: int) -> model.Calculation:
        return self.session.query(model.Calculation).filter_by(id=id_).first()

    def _get_by_uuid(self, uuid: str) -> model.Calculation:
        return self.session.query(model.Calculation).filter_by(uuid=uuid).first()

    def _get_by_action(self, action: str) -> model.Calculation:
        return self.session.query(model.Calculation).filter_by(action=action).first()

    def _get_all(self) -> list[model.Calculation]:
        return self.session.query(model.Calculation).all()

