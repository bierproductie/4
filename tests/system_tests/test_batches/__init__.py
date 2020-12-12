import random

from tests import utils

ROUTE = "/batches/"


@utils.raise_for_status
def create_batch(client, batch: dict):
    return client.post(ROUTE, json=batch)


@utils.raise_for_status
def update_batch(client, batch: dict, identifier: int):
    route = get_route(identifier=identifier)
    return client.put(route, json=batch)


@utils.raise_for_status
def delete_batch(client, identifier: int):
    route = get_route(identifier=identifier)
    return client.delete(route)


@utils.raise_for_status
def get_batch(client, identifier: int):
    route = get_route(identifier=identifier)
    return client.get(route)


@utils.raise_for_status
def get_batches(client):
    return client.get(ROUTE)


def get_route(identifier: int):
    return f"{ROUTE}{identifier}"


def random_batch(recipe_name: str):
    return {
        "speed": random.randint(0, 300),
        "amount_to_produce": random.randint(0, 200),
        "started_dt": utils.random_datetime(2020, 2050).isoformat(),
        "recipe_id": recipe_name,
        "finished_dt": utils.random_datetime(2020, 2050).isoformat(),
        "oee": random.uniform(0, 200),
    }
