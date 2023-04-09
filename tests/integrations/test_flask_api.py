import pytest

BASE_URL = "/v2/calculate"


@pytest.mark.integration
def test_get_all_calculation_flask_api(
    get_fake_container, get_flask_client, get_flask_app
):
    use_case = get_fake_container.calculate_use_case()
    with get_flask_app.container.calculate_use_case.override(use_case):
        response = get_flask_client.get(f"{BASE_URL}/calculations")
        assert response.status_code == 200
        with get_flask_app.container.calculation_uow.override(
            get_fake_container.calculation_uow
        ):
            with get_flask_app.container.operands_service.override(
                get_fake_container.operands_service
            ):
                use_case.add(5, 6)
                uow_ = get_fake_container.calculation_uow()
                with uow_:
                    result = uow_.calculation.get_all()
                    assert len(result) == 1
                    assert result[0].action == "add"
                    assert result[0].result == 11
        response = get_flask_client.get(f"{BASE_URL}/calculations")
        assert response.status_code == 200
        assert response.json["results"][0] == result[0].uuid


@pytest.mark.integration
def test_get_by_uuid_flask_api(get_fake_container, get_flask_client, get_flask_app):
    use_case = get_fake_container.calculate_use_case()
    with get_flask_app.container.calculate_use_case.override(use_case):
        response = get_flask_client.get(f"{BASE_URL}/calculations")
        data = response.json
        uuid = data["results"][0]
        response = get_flask_client.get(f"{BASE_URL}/calculation/{uuid}")
        assert response.status_code == 200
        data = response.json
        assert data["result"]["uuid"] == uuid
        assert data["result"]["action"] == "add"
