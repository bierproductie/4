"""This module is used as a factory."""
from bierproductie_api.domain.batches import batch_queries
from bierproductie_api.domain.batches import batch_services
from bierproductie_api.domain.data_over_time import data_entrypoint_queries
from bierproductie_api.domain.data_over_time import data_entrypoint_services
from bierproductie_api.domain.recipes import recipe_queries
from bierproductie_api.domain.recipes import recipe_services


def get_recipe_services() -> recipe_services.Service:
    return recipe_services.Service(recipe_queries.Queries())


def get_batch_services() -> batch_services.Service:
    return batch_services.Service(batch_queries.Queries())


def get_data_entrypoint_services() -> data_entrypoint_services.Service:
    return data_entrypoint_services.Service(data_entrypoint_queries.Queries())
