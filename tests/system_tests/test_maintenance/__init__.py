import random

from tests import utils

ROUTE = "/maintenance/"


@utils.raise_for_status
def update(client, maintx: dict):
    return client.put(ROUTE, json=maintx)


@utils.raise_for_status
def get(client):
    return client.get(ROUTE)


def random_maintx():
    return dict(value=random.uniform(0, 100))
