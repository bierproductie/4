"""This module is for implementing recipe services.

The Service class' job is to interface with the recipe queries, and
transform the result provided by the Quries class into Schemas. When
creating an instance of Service() you shouldn't call
`service._queries()` directly, hence why it's declared as private (_).
"""
from typing import List

import pydantic

from bierproductie_api.core import exceptions
from bierproductie_api.domain import base_schemas
from bierproductie_api.domain.recipes import recipe_queries
from bierproductie_api.domain.recipes import recipe_schemas


class Service:
    """Service."""

    def __init__(self, queries: recipe_queries.Queries):
        """__init__.

        Args:
            queries (recipe_queries.Queries): queries
        """
        self._queries = queries

    async def create(self,
                     recipe: recipe_schemas.Create) -> recipe_schemas.DB:
        """create.

        Args:
            recipe (recipe_schemas.Create): recipe
        Returns:
            recipe_schemas.DB:
        """
        new_recipe = await self._queries.create(recipe=recipe)
        return recipe_schemas.DB.from_orm(new_recipe)

    async def get_by_id(
            self, name: str) -> recipe_schemas.DB:
        """Gets the recipe that matches the provided identifier.

        Args:
            name (str): The name of the recipe
        Returns:
            recipe_schemas.DB: If the recipe is found, otherwise 404.
        """
        try:
            return await self._queries.get_by_id(name=name)
        except Exception as e:
            raise exceptions.NotFound from e

    async def get_list(self) -> List[recipe_schemas.DB]:
        """Gets a paginated result list of recipes.

        Returns:
            recipe_schemas.Paginated:
        """
        recipes = await self._queries.get_list()
        return [recipe_schemas.DB.from_orm(recipe) for recipe in recipes]

    async def update(self, name: str, new_recipe: recipe_schemas.Update) -> recipe_schemas.DB:
        """Updates an existing recipe.

        Args:
            name (str): name of the recipe
            new_recipe (recipe_schemas.Update): new_recipe
        Returns:
            recipe_schemas.DB:
        """
        old_recipe = await self._queries.get_by_id(name=name)

        updated_recipe = await self._queries.update(old_recipe=old_recipe,
                                                    new_recipe=new_recipe)
        return recipe_schemas.DB.from_orm(updated_recipe)

    async def delete(self,
                     name: str) -> recipe_schemas.DB:
        """Deletes a specific recipe
        Args:
            identifier (float): identifier
        Returns:
            recipe_schemas.DB:
        """
        deleted_recipe = await self._queries.delete(name=name)
        return recipe_schemas.DB.from_orm(deleted_recipe)
