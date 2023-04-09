from fastapi import FastAPI
from flask import Flask
from flask_bootstrap import Bootstrap

from calculator.adapters.db.orm import start_mappers
from calculator.adapters.entrypoints.api.base import api_router
from calculator.adapters.entrypoints.api.v2 import route_calculate
from calculator.configurator.containers import Container


def include_router(app_):
    app_.include_router(api_router)


def start_application():
    container = Container()
    app_ = FastAPI()
    app_.container = container
    include_router(app_)
    # start ORM mappers
    try:
        start_mappers()
    except Exception as err:
        # Checking if the mapper was already started
        if "already has a primary mapper defined" not in str(err):
            raise RuntimeError(err) from err
    return app_


def create_app() -> Flask:
    container = Container()
    app_ = Flask(__name__)
    app_.container = container
    app_.register_blueprint(
        blueprint=route_calculate.blueprint, url_prefix="/v2/calculate"
    )

    bootstrap = Bootstrap()
    bootstrap.init_app(app_)

    # start ORM mappers
    try:
        start_mappers()
    except Exception as err:
        # Checking if the mapper was already started
        if "already has a primary mapper defined" not in str(err):
            raise RuntimeError(err) from err

    return app_


app = start_application()

flask_app = create_app()
