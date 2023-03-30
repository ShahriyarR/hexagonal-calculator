import pytest


@pytest.mark.integration
def test_uow_add_calculation(get_fake_container, get_calculation_model_object):
    uow = get_fake_container.calculation_uow()
    with uow:
        uow.calculation.add(get_calculation_model_object)
        uow.commit()
        all_ = uow.calculation.get_all()
        assert len(all_) == 1


@pytest.mark.integration
def test_uow_get_calculation_by_uuid(get_fake_container, get_calculation_model_object_with_subtract):
    uow = get_fake_container.calculation_uow()
    with uow:
        uow.calculation.add(get_calculation_model_object_with_subtract)
        uow.commit()
        all_ = uow.calculation.get_all()
        # get the dictionary values
        uuid = all_[1].uuid
        result = uow.calculation.get_by_uuid(uuid)
        assert result.uuid == uuid


@pytest.mark.integration
def test_uow_get_calculation_by_action(get_fake_container, get_calculation_model_object_with_subtract):
    uow = get_fake_container.calculation_uow()
    with uow:
        uow.calculation.add(get_calculation_model_object_with_subtract)
        uow.commit()
        result = uow.calculation.get_by_action("subtract")
        assert result.action == "subtract"


@pytest.mark.integration
def test_uow_get_all_calculations(get_fake_container, get_calculation_model_object):
    uow = get_fake_container.calculation_uow()
    with uow:
        uow.calculation.add(get_calculation_model_object)
        uow.commit()
        all_ = uow.calculation.get_all()
        assert len(all_) == 2