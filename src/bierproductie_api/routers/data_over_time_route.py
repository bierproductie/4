"""Endpoints starting with /data_over_time/ are defined here.

This module contains all API endpoints which path contains '/data_over_time/'.
Not that no "business-logic" is defined in here, we simply pass in onto
the data_entrypoint service from the `service_factory`, by doing it this way
the controller only knows which methods it can call in data_entrypoint Service
but nothing about the database.
"""
import datetime

import fastapi
import pydantic
from starlette import status

from bierproductie_api.core import service_factory
from bierproductie_api.domain.data_over_time import data_entrypoint_schemas

router = fastapi.APIRouter()


@router.get('/', response_model=data_entrypoint_schemas.Paginated)
async def get_data_over_time(page_size: pydantic.conint(ge=1, le=100) = 20,
                             page: pydantic.conint(ge=1) = 1,
                             service=fastapi.Depends(
        service_factory.get_data_entrypoint_services)):
    """Get a paginated list of data_over_time.

    TODO(Add Doc)
    Args:
        page_size (pydantic.conint(ge=1, le=100)): page_size
        page (pydantic.conint(ge=1)): page
        service:
    """
    return await service.get_list(page=page, page_size=page_size)


@router.post('/',
             response_model=data_entrypoint_schemas.DB,
             status_code=status.HTTP_201_CREATED)
async def add_data_entrypoint(data_entrypoint: data_entrypoint_schemas.Create,
                              service=fastapi.Depends(
                                  service_factory.get_data_entrypoint_services)
                              ):
    """Create a new data_entrypoint.

    TODO(Add Doc)
    Args:
        data_entrypoint (data_entrypoint_schemas.Create): data_entrypoint
    """
    return await service.create(data_entrypoint=data_entrypoint)


@router.put('/{measurement_ts}', response_model=data_entrypoint_schemas.DB)
async def update_data_entrypoint(
    measurement_ts: datetime.datetime,
    data_entrypoint: data_entrypoint_schemas.Update,
    service=fastapi.Depends(
        service_factory.get_data_entrypoint_services)):
    """Updates an existing data_entrypoint.

    TODO(Add Doc and fix exception text)
    Args:
        measurement_ts (datetime.datetime): measurement_ts
        data_entrypoint (data_entrypoint_schemas.Update): data_entrypoint
    """
    data_entrypoint = await service.update(measurement_ts=measurement_ts,
                                           new_data_entrypoint=data_entrypoint)
    if data_entrypoint:
        return data_entrypoint
    raise fastapi.HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A data_entrypoint with ID: '{measurement_ts} was not found.",
    )


@router.get('/{measurement_ts}', response_model=data_entrypoint_schemas.DB)
async def get_data_entrypoint(
    measurement_ts: datetime.datetime,
    service=fastapi.Depends(
        service_factory.get_data_entrypoint_services)):
    """Get a data_entrypoint with the provided measurement_ts.

    TODO(Add Doc)
    Args:
        measurement_ts (datetime.datetime): measurement_ts
    """
    data_entrypoint = await service.get_by_id(measurement_ts=measurement_ts)
    if data_entrypoint:
        return data_entrypoint
    raise fastapi.HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A data_entrypoint with id: '{measurement_ts} was not found.",
    )


@router.delete('/{measurement_ts}', response_model=data_entrypoint_schemas.DB)
async def delete_data_entrypoint(
    measurement_ts: datetime.datetime,
    service=fastapi.Depends(
        service_factory.get_data_entrypoint_services)):
    """Deletes the data_entrypoint that belongs to the provided measurement_ts.

    TODO(Add Doc)
    Args:
        measurement_ts (datetime.datetime): measurement_ts
    """
    return await service.delete(measurement_ts=measurement_ts)
