"""Endpoints starting with /maintenance/ are defined here.

This module contains all API endpoints which path contains '/maintenance/'.
Not that no "business-logic" is defined in here, we simply pass in onto
the maintenance service from the `service_factory`, by doing it this way
the controller only knows which methods it can call in maintenance Service
but nothing about the database.
"""

import fastapi

from bierproductie_api.core import service_factory
from bierproductie_api.domain.maintenance import maintx_schemas

router = fastapi.APIRouter()


@router.get('/', response_model=maintx_schemas.DB)
async def get_maintenance(service=fastapi.Depends(
        service_factory.get_maintx_services)):
    """Get the latest maintenance
    """
    return await service.get()


@router.put('/', response_model=maintx_schemas.DB)
async def update_maintenance(maintenance: maintx_schemas.Update,
                             service=fastapi.Depends(
                                 service_factory.get_maintx_services)):
    """Updates the maintenance value

    Args:
        maintenance (maintx_schemas.Update): maintx
    """
    return await service.update(value=maintenance.value)
