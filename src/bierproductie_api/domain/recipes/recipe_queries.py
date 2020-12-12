"""This module is for all recipe related queries
"""
from typing import List

from bierproductie_api.domain.recipes import recipe_model
from bierproductie_api.domain.recipes import recipe_schemas

CreateSchema = recipe_schemas.Create
UpdateSchema = recipe_schemas.Update
Model = recipe_model.Model


class Queries():
    """Queries
    """

    async def create(self, recipe: CreateSchema) -> Model:
        return await Model.create(**recipe.__dict__)

    async def get_list(self) -> List[Model]:
        recipes: List[Model] = await Model.query.order_by(
            Model.name.asc()
        ).gino.all()
        return recipes

    async def get_by_id(self, name: str) -> Model:
        return await Model.get(name)

    async def delete(self, name: str) -> Model:
        recipe = await self.get_by_id(name)
        await recipe.delete()
        return recipe

    async def update(self, old_recipe: Model,
                     new_recipe: UpdateSchema) -> Model:
        updated_recipe = await old_recipe.update(**new_recipe.__dict__
                                                 ).apply()
        return updated_recipe._instance  # pylint: disable=protected-access
