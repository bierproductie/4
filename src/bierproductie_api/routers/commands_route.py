"""Endpoints starting with /data_over_time/ are defined here.

This module contains all API endpoints which path contains '/data_over_time/'.
Not that no "business-logic" is defined in here, we simply pass in onto
the data_entrypoint service from the `service_factory`, by doing it this way
the controller only knows which methods it can call in data_entrypoint Service
but nothing about the database.
"""
import fastapi

from bierproductie_api.core import service_factory

router = fastapi.APIRouter()


@router.post('/{method}')
async def get_data_over_time(method: str,
                             service=fastapi.Depends(
        service_factory.get_command_services)):
    """Send a start command to the OPC-UA client
    """
    return await service.send(method=method)
