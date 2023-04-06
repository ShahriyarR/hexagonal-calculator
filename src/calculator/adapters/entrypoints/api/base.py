from fastapi import APIRouter

from calculator.adapters.entrypoints.api.v1 import route_calculate

api_router = APIRouter()

api_router.include_router(
    route_calculate.router, prefix="/calculate", tags=["calculate"]
)
