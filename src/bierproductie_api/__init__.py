"""This module is where we initialize our App
"""

from fastapi import FastAPI
from fastapi.middleware import cors
import sentry_sdk
from sentry_sdk.integrations import sqlalchemy

from bierproductie_api.core import version
from bierproductie_api.core.db import DB
from bierproductie_api.routers import batches_route
from bierproductie_api.routers import data_over_time_route
from bierproductie_api.routers import recipes_route


def create_app() -> FastAPI:
    """create_app.

    Args:

    Returns:
        FastAPI:
    """
    app: FastAPI = FastAPI(
        title="Bierproductie API", version=version.__version__,
    )
    _initalize_extensions(app=app)
    _add_middleware(app=app)
    return _register_routes(app=app)


def _add_middleware(app: FastAPI) -> FastAPI:
    app.add_middleware(
        cors.CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def _register_routes(app: FastAPI) -> FastAPI:
    """_register_routes.

    Args:
        app (FastAPI): app

    Returns:
        FastAPI:
    """
    app.include_router(data_over_time_route.router, tags=[
                       "Data_Over_Time"], prefix="/data_over_time")
    app.include_router(batches_route.router, tags=[
                       "Batches"], prefix="/batches")
    app.include_router(recipes_route.router, tags=[
                       "Recipes"], prefix="/recipes")
    return app


def _initalize_extensions(app: FastAPI):
    """_initalize_extensions.

    Args:
        app (FastAPI): app
    """
    DB.init_app(app=app)
    sentry_sdk.init(integrations=[sqlalchemy.SqlalchemyIntegration()])
