"""This module is for implementing maintx services.

The Service class' job is to interface with the maintx queries, and
transform the result provided by the Quries class into Schemas. When
creating an instance of Service() you shouldn't call
`service._queries()` directly, hence why it's declared as private (_).
"""
from bierproductie_api.core import exceptions
from bierproductie_api.domain.maintenance import maintx_queries
from bierproductie_api.domain.maintenance import maintx_schemas


class Service:
    """Service."""

    def __init__(self, queries: maintx_queries.Queries):
        """__init__.

        Args:
            queries (maintx_queries.Queries): queries
        """
        self._queries = queries

    async def create(self, value: float) -> maintx_schemas.DB:
        """create.

        Args:
            maintx (maintx_schemas.Create): maintx
        Returns:
            maintx_schemas.DB:
        """
        new_maintx = await self._queries.create(value=value)
        return maintx_schemas.DB.from_orm(new_maintx)

    async def get(self) -> maintx_schemas.DB:
        """Gets the maintx that matches the provided value.

        Args:
            value (float): value
        Returns:
            maintx_schemas.DB: If the maintx is found, otherwise 404.
        """
        maintx = await self._queries.get()
        if maintx:
            return maintx_schemas.DB.from_orm(maintx)
        raise exceptions.NotFound()

    async def update(self, value: float) -> maintx_schemas.DB:
        """Updates the maintenance

        Args:
            value (float): value
        Returns:
            maintx_schemas.DB:
        """
        old_maintx = await self._queries.get()
        if old_maintx is None:
            return await self.create(value=value)
        updated = await self._queries.update(value=value)
        return maintx_schemas.DB.from_orm(updated)
