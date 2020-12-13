"""This module is for all batch related queries
"""
from typing import List

from bierproductie_api.domain.batches import batch_model
from bierproductie_api.domain.batches import batch_schemas

CreateSchema = batch_schemas.Create
UpdateSchema = batch_schemas.Update
Model = batch_model.Model


class Queries:
    """Queries
    """

    async def create(self, batch: CreateSchema) -> Model:
        return await Model.create(**batch.__dict__)

    async def get_list(self) -> List[Model]:
        batches: List[Model] = await Model.query.order_by(
            Model.started_dt.desc()).gino.all()

        return batches

    async def get_by_id(self, identifier: int) -> Model:
        return await Model.get(identifier)

    async def get_latest(self) -> Model:
        return await Model.query.order_by(Model.identifier.desc()).gino.first()

    async def delete(self, identifier: int) -> Model:
        batch = await self.get_by_id(identifier)
        await batch.delete()
        return batch

    async def update(self, old_batch: Model,
                     new_batch: UpdateSchema) -> Model:
        updated_batch = await old_batch.update(**new_batch.__dict__
                                               ).apply()
        return updated_batch._instance  # pylint: disable=protected-access
