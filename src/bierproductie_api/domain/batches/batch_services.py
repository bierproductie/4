"""This module is for implementing batch services.

The Service class' job is to interface with the batch queries, and
transform the result provided by the Queries class into Schemas. When
creating an instance of Service() you shouldn't call
`service._queries()` directly, hence why it's declared as private (_).
"""

from typing import List

from bierproductie_api.domain.batches import batch_queries
from bierproductie_api.domain.batches import batch_schemas


class Service:
    """Service."""

    def __init__(self, queries: batch_queries.Queries):
        """__init__.

        Args:
            queries (batch_queries.Queries): queries
        """
        self._queries = queries

    async def create(self, batch: batch_schemas.Create) -> batch_schemas.DB:
        """create.

        Args:
            batch (batch_schemas.Create): batch
        Returns:
            batch_schemas.DB:
        """
        new_batch = await self._queries.create(batch=batch)
        return batch_schemas.DB.from_orm(new_batch)

    async def get_by_id(
            self, identifier: int) -> batch_schemas.DB:
        """Gets the batch that matches the provided identifier.

        Args:
            identifier (int): identifier
        Returns:
            batch_schemas.DB: If the batch is found, otherwise 404.
        """
        return await self._queries.get_by_id(identifier=identifier)

    async def get_list(self) -> List[batch_schemas.DB]:
        """Gets a paginated result list of batches.

        Returns:
            batch_schemas.Paginated:
        """
        batches = await self._queries.get_list()
        return [batch_schemas.DB.from_orm(batch) for batch in batches]

    async def update(
            self, identifier: int,
            new_batch: batch_schemas.Update) -> batch_schemas.DB:
        """Updates an existing batch.

        Args:
            identifier (int): identifier
            new_batch (batch_schemas.Update): new_batch
        Returns:
            batch_schemas.DB:
        """
        old_batch = await self._queries.get_by_id(
            identifier=identifier)

        updated_batch = await self._queries.update(old_batch=old_batch,
                                                   new_batch=new_batch)
        return batch_schemas.DB.from_orm(updated_batch)

    async def delete(self,
                     identifier: int) -> batch_schemas.DB:
        """Deletes a specific batch
        Args:
            identifier (int): identifier
        Returns:
            batch_schemas.DB:
        """
        deleted_batch = await self._queries.delete(
            identifier=identifier)
        return batch_schemas.DB.from_orm(deleted_batch)
