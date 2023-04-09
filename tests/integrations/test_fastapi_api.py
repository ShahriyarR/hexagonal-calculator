import pytest

from calculator.adapters.entrypoints.api.app import app


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_all_calculation_api(get_fake_container, client):
    use_case = get_fake_container.calculate_use_case()
    with app.container.calculate_use_case.override(use_case):
        response = await client.get("/calculations")
        assert response.status_code == 200
        with app.container.calculation_uow.override(get_fake_container.calculation_uow):
            with app.container.operands_service.override(
                get_fake_container.operands_service
            ):
                use_case.add(5, 6)
                uow_ = get_fake_container.calculation_uow()
                with uow_:
                    result = uow_.calculation.get_all()
                    assert len(result) == 1
                    assert result[0].action == "add"
                    assert result[0].result == 11
        response = await client.get("/calculations")
        assert response.status_code == 200
        data = response.json()
        assert len(data["results"]) == 1


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_by_uuid_api(get_fake_container, client):
    use_case = get_fake_container.calculate_use_case()
    with app.container.calculate_use_case.override(use_case):
        response = await client.get("/calculations")
        data = response.json()
        uuid = data["results"][0]
        response = await client.get(f"/calculation/{uuid}")
        assert response.status_code == 200
        data = response.json()
        assert data["result"]["uuid"] == uuid
        assert data["result"]["action"] == "add"
