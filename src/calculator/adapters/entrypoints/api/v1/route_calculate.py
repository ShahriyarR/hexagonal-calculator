import json
from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response

from calculator.domain.ports.use_cases.calculate import CalculateUseCaseInterface

router = APIRouter()


@router.get("/calculations", response_model=None)
@inject
async def get_all_calculation(
    use_case: CalculateUseCaseInterface = Depends(Provide["calculate_use_case"]),
) -> Response:
    data = use_case.get_all()
    return Response(
        content=json.dumps(data), media_type="application/json", status_code=200
    )


@router.get("/calculation/{uuid}", response_model=None)
@inject
async def get_calculation_by_uuid(
    uuid: str,
    use_case: CalculateUseCaseInterface = Depends(Provide["calculate_use_case"]),
) -> dict[str, Any]:
    return use_case.get_by_uuid(uuid)
