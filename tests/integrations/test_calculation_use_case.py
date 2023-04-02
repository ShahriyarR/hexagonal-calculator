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
