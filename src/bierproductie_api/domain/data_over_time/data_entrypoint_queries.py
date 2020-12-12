"""This module is for all data_entrypoint related queries
"""
import datetime
from typing import List
from typing import Tuple

from bierproductie_api.core.db import DB
from bierproductie_api.domain.data_over_time import data_entrypoint_model
from bierproductie_api.domain.data_over_time import data_entrypoint_schemas

CreateSchema = data_entrypoint_schemas.Create
UpdateSchema = data_entrypoint_schemas.Update
Model = data_entrypoint_model.Model


class Queries():
    """Queries
    """

    async def create(self, data_entrypoint: CreateSchema) -> Model:
        return await Model.create(**data_entrypoint.__dict__)

    async def get_list(self, page_size: int, page: int
                       ) -> Tuple[List[Model], int]:

        data_over_time: List[Model] = await Model.query.order_by(
            Model.measurement_ts.asc()
        ).offset(
            page_size * (page - 1)
        ).limit(
            page_size
        ).gino.all()
        count = await DB.func.count(Model.measurement_ts).gino.scalar()
        return data_over_time, count

    async def get_by_id(self, measurement_ts: datetime.datetime) -> Model:
        return await Model.get(measurement_ts)

    async def delete(self, measurement_ts: datetime.datetime) -> Model:
        data_entrypoint = await self.get_by_id(measurement_ts)
        await data_entrypoint.delete()
        return data_entrypoint

    async def update(self, old_data_entrypoint: Model,
                     new_data_entrypoint: UpdateSchema) -> Model:
        updated = await old_data_entrypoint.update(
            **new_data_entrypoint.__dict__).apply()
        return updated._instance  # pylint: disable=protected-access
