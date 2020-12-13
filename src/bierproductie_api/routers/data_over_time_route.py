"""Endpoints starting with /data_over_time/ are defined here.

This module contains all API endpoints which path contains '/data_over_time/'.
Not that no "business-logic" is defined in here, we simply pass in onto
the data_entrypoint service from the `service_factory`, by doing it this way
the controller only knows which methods it can call in data_entrypoint Service
but nothing about the database.
"""
from typing import Optional
import datetime

import fastapi
import pydantic
from starlette import status

from bierproductie_api.core import service_factory
from bierproductie_api.domain.data_over_time import data_entrypoint_schemas

router = fastapi.APIRouter()


@router.get('/{batch_id}', response_model=data_entrypoint_schemas.Paginated)
async def get_data_over_time(batch_id: int,
                             from_dt: Optional[datetime.datetime] = None,
                             page_size: pydantic.conint(ge=1, le=100) = 20,
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
    return await service.get_list(batch_id=batch_id,
                                  page=page,
                                  page_size=page_size)


@router.put('/',
            response_model=data_entrypoint_schemas.DB,
            status_code=status.HTTP_201_CREATED)
async def update_data_entrypoint(
    data_entrypoint: data_entrypoint_schemas.Update,
    service=fastapi.Depends(
        service_factory.get_data_entrypoint_services)
):
    """Update an existing data_entrypoint.

    TODO(Add Doc)
    Args:
        data_entrypoint (data_entrypoint_schemas.Update): data_entrypoint
    """
    return await service.update(data_entrypoint=data_entrypoint)


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
