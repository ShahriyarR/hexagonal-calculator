def test_add_calculation(get_fake_repository, get_calculation_model_object):
    get_fake_repository.add(get_calculation_model_object)
    all_ = get_fake_repository.get_all()
    # get the dictionary values
    values = list(all_.values())
    assert len(values) == 1
    assert values[0].action == "add"


def test_get_calculation_by_uuid(get_fake_repository):
    all_ = get_fake_repository.get_all()
    # get the dictionary values
    values = list(all_.values())
    uuid = values[0].uuid
    result = get_fake_repository.get_by_uuid(uuid)
    assert result.action == "add"


def test_get_calculation_by_action(get_fake_repository):
    result = get_fake_repository.get_by_action("add")
    assert result.action == "add"


def test_get_all_calculations(get_fake_repository):
    all_ = get_fake_repository.get_all()
    values = list(all_.values())
    assert len(values) == 1
