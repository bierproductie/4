"""Endpoints starting with /inventory_statuses/ are defined here.

This module contains all API endpoints which path contains
'/inventory_statuses/'. Not that no "business-logic" is defined in here, we
simply pass in onto the inventory_status service from the `service_factory`, by
doing it this way the controller only knows which methods it can call in
inventory_status Service but nothing about the database.
"""

import fastapi
import pydantic
from starlette import status

from bierproductie_api.core import service_factory
from bierproductie_api.domain.inventory_statuses import \
    inventory_status_schemas

router = fastapi.APIRouter()


@router.get('/', response_model=inventory_status_schemas.Paginated)
async def get_inventory_statuses(page_size: pydantic.conint(ge=1, le=100) = 20,
                                 page: pydantic.conint(ge=1) = 1,
                                 service=fastapi.Depends(
        service_factory.get_inventory_status_services)):
    """Get a paginated list of inventory_statuses.

    TODO(Add Doc)
    Args:
        page_size (pydantic.conint(ge=1, le=100)): page_size
        page (pydantic.conint(ge=1)): page
        service:
    """
    return await service.get_list(page=page, page_size=page_size)


@router.post('/',
             response_model=inventory_status_schemas.DB,
             status_code=status.HTTP_201_CREATED)
async def add_inventory_status(
    inventory_status: inventory_status_schemas.Create,
    service=fastapi.Depends(
        service_factory.get_inventory_status_services)):
    """Create a new inventory_status.

    TODO(Add Doc)
    Args:
        inventory_status (inventory_status_schemas.Create): inventory_status
    """
    return await service.create(inventory_status=inventory_status)


@router.put('/{name}', response_model=inventory_status_schemas.DB)
async def update_inventory_status(
    name: str,
    inventory_status: inventory_status_schemas.Update,
    service=fastapi.Depends(
        service_factory.get_inventory_status_services)):
    """Updates an existing inventory_status.

    TODO(Add Doc and fix exception text)
    Args:
        name (str): name
        inventory_status (inventory_status_schemas.Update): inventory_status
    """
    inventory_status = await service.update(
        name=name,
        new_inventory_status=inventory_status)
    if inventory_status:
        return inventory_status
    raise fastapi.HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A inventory_status with ID: '{name} was not found.",
    )


@router.get('/{name}', response_model=inventory_status_schemas.DB)
async def get_inventory_status(
    name: str,
    service=fastapi.Depends(
        service_factory.get_inventory_status_services)):
    """Get a inventory_status with the provided name.

    TODO(Add Doc)
    Args:
        name (str): name
    """
    inventory_status = await service.get_by_id(name=name)
    if inventory_status:
        return inventory_status
    raise fastapi.HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A inventory_status with id: '{name} was not found.",
    )


@router.delete('/{name}', response_model=inventory_status_schemas.DB)
async def delete_inventory_status(
    name: str,
    service=fastapi.Depends(
        service_factory.get_inventory_status_services)):
    """Deletes the inventory_status that belongs to the provided name.

    TODO(Add Doc)
    Args:
        name (str): name
    """
    return await service.delete(name=name)
