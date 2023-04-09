import json
from typing import Any

from dependency_injector.wiring import Provide, inject
from flask import Blueprint, Response

from calculator.domain.ports.use_cases.calculate import CalculateUseCaseInterface

blueprint = Blueprint("calculate", __name__)


@blueprint.get("/calculations")
@inject
def get_all_calculation(
    use_case: CalculateUseCaseInterface = Provide["calculate_use_case"],
) -> Response:
    data = use_case.get_all()
    return Response(json.dumps(data), content_type="application/json", status=200)


@blueprint.get("/calculation/<uuid>")
@inject
def get_calculation_by_uuid(
    uuid: str,
    use_case: CalculateUseCaseInterface = Provide["calculate_use_case"],
) -> dict[str, Any]:
    return use_case.get_by_uuid(uuid)
