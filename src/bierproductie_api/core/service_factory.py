"""This module is used as a factory."""
from bierproductie_api.domain.batches import batch_queries
from bierproductie_api.domain.batches import batch_services
from bierproductie_api.domain.data_over_time import data_entrypoint_queries
from bierproductie_api.domain.data_over_time import data_entrypoint_services
from bierproductie_api.domain.inventory_statuses import \
    inventory_status_queries
from bierproductie_api.domain.inventory_statuses import \
    inventory_status_services
from bierproductie_api.domain.maintenance import maintx_queries
from bierproductie_api.domain.maintenance import maintx_services
from bierproductie_api.domain.recipes import recipe_queries
from bierproductie_api.domain.recipes import recipe_services
from bierproductie_api.domain.commands import command_services

def get_recipe_services() -> recipe_services.Service:
    return recipe_services.Service(recipe_queries.Queries())


def get_batch_services() -> batch_services.Service:
    return batch_services.Service(queries=batch_queries.Queries(),
                                  recipe_queries=recipe_queries.Queries())


def get_data_entrypoint_services() -> data_entrypoint_services.Service:
    return data_entrypoint_services.Service(
        dot_queries=data_entrypoint_queries.Queries(),
        recipe_queries=recipe_queries.Queries(),
        batch_queries=batch_queries.Queries())


def get_maintx_services() -> maintx_services.Service:
    return maintx_services.Service(maintx_queries.Queries())


def get_inventory_status_services() -> inventory_status_services.Service:
    return inventory_status_services.Service(
        inventory_status_queries.Queries())


def get_command_services() -> command_services.Service:
    return command_services.Service()
