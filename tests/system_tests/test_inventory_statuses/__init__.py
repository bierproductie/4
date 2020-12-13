import random

from tests import utils

ROUTE = "/inventory_statuses/"


@utils.raise_for_status
def create_inventory_status(client, inventory_status: dict):
    return client.post(ROUTE, json=inventory_status)


@utils.raise_for_status
def update_inventory_status(client, inventory_status: dict, name: str):
    return client.put(ROUTE + name, json=inventory_status)


@utils.raise_for_status
def delete_inventory_status(client, name: str):
    return client.delete(ROUTE + name)


@utils.raise_for_status
def get_inventory_status(client, name: str):
    return client.get(ROUTE + name)


@utils.raise_for_status
def get_inventory_statuses(client, page: int = 1, page_size: int = 50):
    return client.get(ROUTE, params={
        'page': page,
        'page_size': page_size
    })


def random_inventory_status():
    return {
        "name": utils.random_string(8),
        "max_value": random.uniform(0, 200),
        "current_value": random.uniform(0, 200),
    }
