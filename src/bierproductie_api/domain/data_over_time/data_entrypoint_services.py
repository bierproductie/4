"""This module is for implementing data_entrypoint services.

The Service class' job is to interface with the data_entrypoint queries, and
transform the result provided by the Quries class into Schemas. When
creating an instance of Service() you shouldn't call
`service._queries()` directly, hence why it's declared as private (_).
"""

import datetime

from bierproductie_api.core import exceptions
from bierproductie_api.domain import base_schemas
from bierproductie_api.domain.data_over_time import data_entrypoint_queries
from bierproductie_api.domain.data_over_time import data_entrypoint_schemas

from bierproductie_api.domain.batches import batch_queries
from bierproductie_api.domain.batches import batch_schemas
from bierproductie_api.domain.recipes import recipe_queries


class Service:
    """Service."""

    def __init__(self,
                 dot_queries: data_entrypoint_queries.Queries,
                 batch_queries: batch_queries.Queries,
                 recipe_queries: recipe_queries.Queries):
        """__init__.

        Args:
            queries (data_entrypoint_queries.Queries): queries
        """
        self._dot_queries = dot_queries
        self._batch_queries = batch_queries
        self._recipe_queries = recipe_queries

    async def create(self,
                     data_entrypoint: data_entrypoint_schemas.Create
                     ) -> data_entrypoint_schemas.DB:
        """create.

        Args:
            data_entrypoint (data_entrypoint_schemas.Create): data_entrypoint
        Returns:
            data_entrypoint_schemas.DB:
        """
        entry = await self._dot_queries.create(data_entrypoint=data_entrypoint)
        await self.update_batch(data_entrypoint=entry)
        return data_entrypoint_schemas.DB.from_orm(entry)

    async def get_by_id(self,
                        measurement_ts: datetime.datetime
                        ) -> data_entrypoint_schemas.DB:
        """Gets the data_entrypoint that matches the provided measurement_ts.

        Args:
            measurement_ts (datetime.datetime): measurement_ts
        Returns:
            data_entrypoint_schemas.DB: If found, otherwise 404.
        """
        data_entrypoint = await self._dot_queries.get_by_id(
            measurement_ts=measurement_ts)
        if data_entrypoint:
            return data_entrypoint_schemas.DB.from_orm(data_entrypoint)
        raise exceptions.NotFound()

    async def get_list(
        self,
        batch_id: int,
        page: int,
        page_size: int,
        from_dt: datetime.datetime = None
    ) -> data_entrypoint_schemas.Paginated:
        """Gets a paginated result list of data_over_time.

        Args:
            page (pydantic.conint(ge=1)): page
            page_size (pydantic.conint(ge=1, le=100)): page_size
        Returns:
            data_entrypoint_schemas.Paginated:
        """
        data_over_time, total = await self._dot_queries.get_list(
            batch_id=batch_id,
            page=page,
            page_size=page_size,
            from_dt=from_dt)
        more = ((total / page_size) - page) > 0
        number_of_pages = max(total / page_size, 1)
        results = [data_entrypoint_schemas.DB.from_orm(
            data_entrypoint) for data_entrypoint in data_over_time]
        pagination = base_schemas.Pagination(total=total,
                                             more=more,
                                             number_of_pages=number_of_pages)
        return data_entrypoint_schemas.Paginated(results=results,
                                                 pagination=pagination)

    async def update(self, data_entrypoint: data_entrypoint_schemas.Update
                     ) -> data_entrypoint_schemas.DB:
        """Updates an existing data_entrypoint.

        Args:
            data_entrypoint (data_entrypoint_schemas.Update): data_entrypoint
        Returns:
            data_entrypoint_schemas.DB:
        """
        old_data_entrypoint = await self._dot_queries.get_by_id(
            measurement_ts=data_entrypoint.measurement_ts)
        if old_data_entrypoint is None:
            raise exceptions.NotFound()

        updated = await self._dot_queries.update(
            old_data_entrypoint=old_data_entrypoint,
            new_data_entrypoint=data_entrypoint)
        await self.update_batch(data_entrypoint=updated)
        return data_entrypoint_schemas.DB.from_orm(updated)

    async def delete(self, measurement_ts: datetime.datetime
                     ) -> data_entrypoint_schemas.DB:
        """Deletes a specific data_entrypoint
        Args:
            measurement_ts (datetime.datetime): measurement_ts
        Returns:
            data_entrypoint_schemas.DB:
        """
        deleted_data_entrypoint = await self._dot_queries.delete(
            measurement_ts=measurement_ts)
        return data_entrypoint_schemas.DB.from_orm(deleted_data_entrypoint)

    async def update_batch(self, data_entrypoint):
        state = data_entrypoint.state
        if state != 17 and state != 9:
            return

        batch_id = data_entrypoint.batch_id
        batch = await self._batch_queries.get_by_id(identifier=batch_id)
        recipe_name = batch.recipe_id
        recipe = await self._recipe_queries.get_by_id(name=recipe_name)
        max_speed = recipe.max_speed
        ideal_cycle_time = self.calculate_ideal_cycle_time(max_speed=max_speed)

        speed = batch.speed
        amount_to_produce = batch.amount_to_produce
        planned_production_time = self.calculate_planned_production_time(
            amount_to_produce=amount_to_produce,
            speed=speed)
        produced = data_entrypoint.produced
        rejected = data_entrypoint.rejected
        accepted = produced - rejected
        oee = self.calculate_oee(
            accepted=accepted,
            planned_production_time=planned_production_time,
            ideal_cycle_time=ideal_cycle_time)
        updated_schema = batch_schemas.Update(
            speed=speed,
            started_dt=batch.started_dt,
            amount_to_produce=amount_to_produce,
            recipe_id=recipe_name,
            finished_dt=data_entrypoint.measurement_ts,
            oee=oee)
        await self._batch_queries.update(old_batch=batch,
                                         new_batch=updated_schema)

    def calculate_ideal_cycle_time(self, max_speed: float) -> float:
        return (1 / max_speed) * 60

    def calculate_planned_production_time(self,
                                          amount_to_produce: int,
                                          speed: float) -> float:
        return (amount_to_produce / speed) * 60

    def calculate_oee(self,
                      accepted: int,
                      planned_production_time: float,
                      ideal_cycle_time: float) -> float:
        return ((accepted * ideal_cycle_time) / planned_production_time) * 100
