"""Basic positive tests (happy paths).
This module executes API calls with valid required parameters.
Validation checks:
    Validate status code: All requests should return 2XX HTTP status codes.
    Validate payload: Response is a well-formed JSON object.
    Validate state: GET requests should not change state.
    Validate headers: Verifies if headers are the same as expected.
"""

import datetime

from tests.system_tests import test_data_over_time
from tests.system_tests import test_recipes
from tests.system_tests import test_batches
from tests import utils


def random_data_entrypoint(client):
    random_recipe = test_recipes.random_recipe()
    recipe, _ = test_recipes.create_recipe(client=client, recipe=random_recipe)
    random_batch = test_batches.random_batch(recipe_name=recipe["name"])
    batch, _ = test_batches.create_batch(client=client, batch=random_batch)
    return test_data_over_time.random_data_entrypoint(
        batch_id=batch["identifier"])


def create_random_data_entrypoint(client, data_entrypoint=None):
    if data_entrypoint is None:
        data_entrypoint = random_data_entrypoint(client=client)
    return test_data_over_time.create_data_entrypoint(
        client=client, data_entrypoint=data_entrypoint)


def test_validate_status_codes(client):
    # Get data_entrypoint list should give 200 OK
    data, status_code = test_data_over_time.get_data_over_time(client=client)
    assert status_code == 200

    # For create methods we expect 201 Created
    data, status_code = create_random_data_entrypoint(client=client)
    assert status_code == 201
    measurement_ts = data["measurement_ts"]

    # Retrieve, we expect 200 OK here.
    data, status_code = test_data_over_time.get_data_entrypoint(
        client=client, measurement_ts=measurement_ts)
    assert status_code == 200

    # Delete, since we are returning the deleted data_entrypoint, a 200 OK is
    # expected instead of 204 No Content.
    data, status_code = test_data_over_time.delete_data_entrypoint(
        client=client, measurement_ts=measurement_ts)
    assert status_code == 200


def test_validate_payload(client):
    data_entrypoint = random_data_entrypoint(client=client)
    data, _ = create_random_data_entrypoint(
        client=client, data_entrypoint=data_entrypoint)

    # API should save the email as lowercase.
    utils.no_state_change(data=data, model=data_entrypoint)

    measurement_ts = data["measurement_ts"]

    data, _ = test_data_over_time.get_data_entrypoint(
        client=client, measurement_ts=measurement_ts)
    utils.no_state_change(data=data, model=data_entrypoint)

    # Delete, since we are returning the deleted data_entrypoint, a 200 OK is
    # expected
    data, status_code = test_data_over_time.delete_data_entrypoint(
        client=client, measurement_ts=measurement_ts)
    utils.no_state_change(data=data, model=data_entrypoint)


def test_validate_headers(client):
    pass


def test_performance_sanity(client):
    data_entrypoint = random_data_entrypoint(client=client)

    @utils.time_it
    def create(c, u):
        return test_data_over_time.create_data_entrypoint(client=c,
                                                          data_entrypoint=u)

    data_entrypoint, _ = create(c=client, u=data_entrypoint)

    @utils.time_it
    def get(c, measurement_ts: datetime.datetime):
        return test_data_over_time.get_data_entrypoint(
            client=c,
            measurement_ts=measurement_ts)

    get(c=client, measurement_ts=data_entrypoint["measurement_ts"])

    @utils.time_it
    def delete(c, measurement_ts: datetime.datetime):
        return test_data_over_time.delete_data_entrypoint(
            client=c, measurement_ts=measurement_ts)

    delete(c=client, measurement_ts=data_entrypoint["measurement_ts"])
