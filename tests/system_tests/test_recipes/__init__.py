import random

from tests import utils

ROUTE = "/recipes/"


@utils.raise_for_status
def create_recipe(client, recipe: dict):
    return client.post(ROUTE, json=recipe)


@utils.raise_for_status
def update_recipe(client, recipe: dict, name: str):
    return client.put(ROUTE + name, json=recipe)


@utils.raise_for_status
def delete_recipe(client, name: str):
    return client.delete(ROUTE + name)


@utils.raise_for_status
def get_recipe(client, name: str):
    return client.get(ROUTE + name)


@utils.raise_for_status
def get_recipes(client):
    return client.get(ROUTE)


def random_recipe():
    return {
        "machine_id": random.uniform(1, 100),
        "max_speed": random.randint(0, 200),
        "recommended_speed": random.randint(0, 200),
        "name": utils.random_string(8),
    }
