"""Endpoints starting with /recipes/ are defined here.

This module contains all API endpoints which path contains '/recipes/'.
Not that no "business-logic" is defined in here, we simply pass in onto
the recipe service from the `service_factory`, by doing it this way
the controller only knows which methods it can call in recipe Service
but nothing about the database.
"""
from typing import List

import fastapi
from starlette import status

from bierproductie_api.core import service_factory
from bierproductie_api.domain.recipes import recipe_schemas

router = fastapi.APIRouter()


@router.get('/', response_model=List[recipe_schemas.DB])
async def get_recipes(service=fastapi.Depends(
        service_factory.get_recipe_services)):
    """Get a paginated list of recipes.

    Args:
        service:
    """
    return await service.get_list()


@router.post('/',
             response_model=recipe_schemas.DB,
             status_code=status.HTTP_201_CREATED)
async def add_recipe(recipe: recipe_schemas.Create,
                     service=fastapi.Depends(
                         service_factory.get_recipe_services)):
    """Create a new recipe.

    TODO(Add Doc)
    Args:
        recipe (recipe_schemas.Create): recipe
    """
    return await service.create(recipe=recipe)


@router.put('/{name}', response_model=recipe_schemas.DB)
async def update_recipe(name: str,
                        recipe: recipe_schemas.Update,
                        service=fastapi.Depends(
                            service_factory.get_recipe_services)):
    """Updates an existing recipe.

    TODO(Add Doc and fix exception text)
    Args:
        name (str): name
    """
    return await service.update(name=name, new_recipe=recipe)


@router.get('/{name}', response_model=recipe_schemas.DB)
async def get_recipe(name: str,
                     service=fastapi.Depends(
                         service_factory.get_recipe_services)):
    """Get a recipe with the provided recipe name.

    TODO(Add Doc)
    Args:
        name (str): name
    """
    return await service.get_by_id(name=name)


@router.delete('/{name}', response_model=recipe_schemas.DB)
async def delete_recipe(name: str,
                        service=fastapi.Depends(
                            service_factory.get_recipe_services)):
    """Deletes the recipe that belongs to the provided recipe name.

    TODO(Add Doc)
    Args:
        name (str): name
    """
    return await service.delete(name=name)
