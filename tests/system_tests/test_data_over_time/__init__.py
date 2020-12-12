import random

from tests import utils


ROUTE = "/data_over_time/"


@utils.raise_for_status
def create_data_entrypoint(client, data_entrypoint: dict):
    return client.post(ROUTE, json=data_entrypoint)


@utils.raise_for_status
def update_data_entrypoint(client,
                           data_entrypoint: dict,
                           measurement_ts: str):
    return client.put(get_route(measurement_ts=measurement_ts))


@utils.raise_for_status
def delete_data_entrypoint(client, measurement_ts: str):
    return client.delete(get_route(measurement_ts=measurement_ts))


@utils.raise_for_status
def get_data_entrypoint(client, measurement_ts: str):
    return client.get(get_route(measurement_ts=measurement_ts))


@utils.raise_for_status
def get_data_over_time(client, page: int = 1, page_size: int = 50):
    return client.get(ROUTE, params={
        'page': page,
        'page_size': page_size
    })


def get_route(measurement_ts: str):
    return f"{ROUTE}{measurement_ts}"


def random_data_entrypoint(batch_id: int):
    return {
        "batch_id": batch_id,
        "measurement_ts": utils.random_datetime(2020, 2050).isoformat(),
        "temperature": random.uniform(0, 200),
        "humidity": random.uniform(0, 200),
        "vibration": random.uniform(0, 200),
        "produced": random.randint(0, 200),
        "state": random.randint(0, 200),
        "rejected": random.randint(0, 200),
    }
