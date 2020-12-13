"""This module is for all data_entrypoint related queries
"""
import datetime
from typing import List
from typing import Tuple
from typing import Optional

from sqlalchemy import and_

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

    async def get_list(self,
                       batch_id: int,
                       page_size: int,
                       page: int,
                       from_dt: Optional[datetime.datetime]
                       ) -> Tuple[List[Model], int]:

        clause = self.__from_clause(batch_id=batch_id, from_dt=from_dt)
        data_over_time: List[Model] = await Model.query.where(clause).order_by(
            Model.measurement_ts.asc()
        ).offset(
            page_size * (page - 1)
        ).limit(
            page_size
        ).gino.all()

        count = await DB.select(
            [DB.func.count(Model.measurement_ts)]
        ).where(
            clause
        ).gino.scalar()

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

    def __from_clause(self, batch_id: int, from_dt: datetime.datetime = None):
        if from_dt:
            return and_(Model.batch_id == batch_id,
                        Model.measurement_ts > from_dt)
        return and_(Model.batch_id == batch_id)
