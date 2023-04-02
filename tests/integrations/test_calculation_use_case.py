import icontract
import pytest

from calculator.configurator.containers import Container


def test_calculate_use_case_add(get_fake_container, get_calculate_use_case):
    with Container.calculation_uow.override(get_fake_container.calculation_uow):
        with Container.operands_service.override(get_fake_container.operands_service):
            get_calculate_use_case.add(5, 6)
            uow_ = get_fake_container.calculation_uow()
            with uow_:
                result = uow_.calculation.get_all()
                assert len(result) == 1
                assert result[0].action == "add"
                assert result[0].result == 11


def test_calculate_use_case_subtract(get_fake_container, get_calculate_use_case):
    with Container.calculation_uow.override(get_fake_container.calculation_uow):
        with Container.operands_service.override(get_fake_container.operands_service):
            get_calculate_use_case.subtract(5, 6)
            uow_ = get_fake_container.calculation_uow()
            with uow_:
                result = uow_.calculation.get_all()
                assert len(result) == 2
                assert result[1].action == "subtract"
                assert result[1].result == -1


def test_calculate_use_case_multiply(get_fake_container, get_calculate_use_case):
    with Container.calculation_uow.override(get_fake_container.calculation_uow):
        with Container.operands_service.override(get_fake_container.operands_service):
            get_calculate_use_case.multiply(5, 6)
            uow_ = get_fake_container.calculation_uow()
            with uow_:
                result = uow_.calculation.get_all()
                assert len(result) == 3
                assert result[2].action == "multiply"
                assert result[2].result == 30


def test_calculate_use_case_divide(get_fake_container, get_calculate_use_case):
    with Container.calculation_uow.override(get_fake_container.calculation_uow):
        with Container.operands_service.override(get_fake_container.operands_service):
            get_calculate_use_case.divide(8, 2.0)
            uow_ = get_fake_container.calculation_uow()
            with uow_:
                result = uow_.calculation.get_all()
                assert len(result) == 4
                assert result[3].action == "divide"
                assert result[3].result == 4.0

            with pytest.raises(icontract.errors.ViolationError):
                get_calculate_use_case.divide(8, 0)


def test_calculate_use_case_get_all(get_fake_container, get_calculate_use_case):
    with Container.calculation_uow.override(get_fake_container.calculation_uow):
        with Container.operands_service.override(get_fake_container.operands_service):
            get_calculate_use_case.add(55, 65)
            get_calculate_use_case.subtract(55, 66)
            get_calculate_use_case.multiply(55, 66)
            result = get_calculate_use_case.get_all()
            # Because of the previous added 4 values
            assert len(result["results"]) == 7
