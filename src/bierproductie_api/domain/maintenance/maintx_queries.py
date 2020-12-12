"""This module is for all maintx related queries
"""
from bierproductie_api.domain.maintenance import maintx_model

Model = maintx_model.Model


class Queries():
    """Queries
    """

    async def create(self, value: float) -> Model:
        return await Model.create(value=value)

    async def get(self) -> Model:
        return await Model.query.gino.first()

    async def update(self, value: float) -> Model:
        updated: Model = await self.get()
        if updated is None:
            return await self.create(value=value)
        await Model.update.values(value=value).gino.status()
        return await self.get()
