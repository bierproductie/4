"""Endpoints starting with /batches/ are defined here.

This module contains all API endpoints which path contains '/batches/'.
Not that no "business-logic" is defined in here, we simply pass in onto
the batch service from the `service_factory`, by doing it this way
the controller only knows which methods it can call in batch Service
but nothing about the database.
"""
from typing import List

import fastapi
from starlette import status

from bierproductie_api.core import service_factory
from bierproductie_api.domain.batches import batch_schemas

router = fastapi.APIRouter()


@router.get('/', response_model=List[batch_schemas.DB])
async def get_batches(service=fastapi.Depends(
        service_factory.get_batch_services)):
    """Get a list of batches.

    Args:
        service:
    """
    return await service.get_list()


@router.post('/',
             response_model=batch_schemas.DB,
             status_code=status.HTTP_201_CREATED)
async def add_batch(batch: batch_schemas.Create,
                    service=fastapi.Depends(
                        service_factory.get_batch_services)):
    """Create a new batch.

    Args:
        batch (batch_schemas.Create): batch
    """
    return await service.create(batch=batch)


@router.put('/{identifier}', response_model=batch_schemas.DB)
async def update_batch(identifier: int,
                       batch: batch_schemas.Update,
                       service=fastapi.Depends(
                           service_factory.get_batch_services)):
    """Updates an existing batch.

    Args:
        identifier (int): identifier
        batch (batch_schemas.Update): batch
    """
    return await service.update(identifier=identifier,
                                new_batch=batch)


@router.get('/{identifier}', response_model=batch_schemas.DB)
async def get_batch(identifier: int,
                    service=fastapi.Depends(
                        service_factory.get_batch_services)):
    """Get a batch with the provided identifier.

    Args:
        identifier (int): identifier
    """
    return await service.get_by_id(identifier=identifier)


@router.delete('/{identifier}', response_model=batch_schemas.DB)
async def delete_batch(identifier: int,
                       service=fastapi.Depends(
                           service_factory.get_batch_services)):
    """Deletes the batch that belongs to the provided identifier.

    Args:
        identifier (int): identifier
    """
    return await service.delete(identifier=identifier)
