"""This module is used as a factory."""
from bierproductie_api.domain.recipes import recipe_queries
from bierproductie_api.domain.recipes import recipe_services


def get_recipe_services() -> recipe_services.Service:
    return recipe_services.Service(recipe_queries.Queries())
