"""This module is for implementing inventory_status services.

The Service class' job is to interface with the inventory_status queries, and
transform the result provided by the Quries class into Schemas. When
creating an instance of Service() you shouldn't call
`service._queries()` directly, hence why it's declared as private (_).
"""

import pydantic

from bierproductie_api.core import exceptions
from bierproductie_api.domain import base_schemas
from bierproductie_api.domain.inventory_statuses import \
    inventory_status_queries
from bierproductie_api.domain.inventory_statuses import \
    inventory_status_schemas


class Service:
    """Service."""

    def __init__(self, queries: inventory_status_queries.Queries):
        """__init__.

        Args:
            queries (inventory_status_queries.Queries): queries
        """
        self._queries = queries

    async def create(self,
                     inventory_status: inventory_status_schemas.Create
                     ) -> inventory_status_schemas.DB:
        """create.

        Args:
            inventory_status (inventory_status_schemas.Create):
                inventory_status
        Returns:
            inventory_status_schemas.DB:
        """
        new_inventory_status = await self._queries.create(
            inventory_status=inventory_status)
        return inventory_status_schemas.DB.from_orm(new_inventory_status)

    async def get_by_id(
            self, name: str) -> inventory_status_schemas.DB:
        """Gets the inventory_status that matches the provided name.

        Args:
            name (str): name
        Returns:
            inventory_status_schemas.DB: If the inventory_status is found,
            otherwise 404.
        """
        inventory_status = await self._queries.get_by_id(
            name=name)
        if inventory_status:
            return inventory_status_schemas.DB.from_orm(inventory_status)
        raise exceptions.NotFound()

    async def get_list(
        self,
        page: pydantic.conint(ge=1),
        page_size: pydantic.conint(ge=1, le=100),
    ) -> inventory_status_schemas.Paginated:
        """Gets a paginated result list of inventory_statuses.

        Args:
            page (pydantic.conint(ge=1)): page
            page_size (pydantic.conint(ge=1, le=100)): page_size
        Returns:
            inventory_status_schemas.Paginated:
        """
        inventory_statuses, total = await self._queries.get_list(
            page=page,
            page_size=page_size)
        more = ((total / page_size) - page) > 0
        results = [inventory_status_schemas.DB.from_orm(
            inventory_status) for inventory_status in inventory_statuses]
        number_of_pages = int(total / page_size)
        pagination = base_schemas.Pagination(
            total=total, more=more, number_of_pages=number_of_pages)
        return inventory_status_schemas.Paginated(results=results,
                                                  pagination=pagination)

    async def update(
            self, name: str,
            new_inventory_status: inventory_status_schemas.Update
    ) -> inventory_status_schemas.DB:
        """Updates an existing inventory_status.

        Args:
            name (str): name
            new_inventory_status (inventory_status_schemas.Update):
                new_inventory_status
        Returns:
            inventory_status_schemas.DB:
        """
        old_inventory_status = await self._queries.get_by_id(
            name=name)

        updated_inventory_status = await self._queries.update(
            old_inventory_status=old_inventory_status,
            new_inventory_status=new_inventory_status)
        return inventory_status_schemas.DB.from_orm(updated_inventory_status)

    async def delete(self,
                     name: str) -> inventory_status_schemas.DB:
        """Deletes a specific inventory_status
        Args:
            name (str): name
        Returns:
            inventory_status_schemas.DB:
        """
        deleted_inventory_status = await self._queries.delete(
            name=name)
        return inventory_status_schemas.DB.from_orm(deleted_inventory_status)
