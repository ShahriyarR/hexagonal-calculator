def test_uow_add_calculation(get_fake_uow, get_calculation_model_object):
    with get_fake_uow:
        get_fake_uow.calculation.add(get_calculation_model_object)
        all_ = get_fake_uow.calculation.get_all()
        # get the dictionary values
        values = list(all_.values())
        assert len(values) == 1
        assert values[0].action == "add"


def test_uow_get_calculation_by_uuid(get_fake_uow, get_calculation_model_object):
    with get_fake_uow:
        get_fake_uow.calculation.add(get_calculation_model_object)
        all_ = get_fake_uow.calculation.get_all()
        # get the dictionary values
        values = list(all_.values())
        uuid = values[0].uuid
        result = get_fake_uow.calculation.get_by_uuid(uuid)
        assert result.action == "add"


def test_uow_get_calculation_by_action(get_fake_uow, get_calculation_model_object):
    with get_fake_uow:
        get_fake_uow.calculation.add(get_calculation_model_object)
        result = get_fake_uow.calculation.get_by_action("add")
        assert result.action == "add"


def test_uow_get_all_calculations(get_fake_uow, get_calculation_model_object):
    with get_fake_uow:
        get_fake_uow.calculation.add(get_calculation_model_object)
        all_ = get_fake_uow.calculation.get_all()
        values = list(all_.values())
        assert len(values) == 1
