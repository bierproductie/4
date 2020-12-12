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
    data, status_code = test_data_over_time.get_data_over_time(
        client=client, batch_id=1)
    assert status_code == 200

    # For create methods we expect 201 Created
    data, status_code = create_random_data_entrypoint(client=client)
    assert status_code == 201


def test_validate_payload(client):
    data_entrypoint = random_data_entrypoint(client=client)
    data, _ = create_random_data_entrypoint(
        client=client, data_entrypoint=data_entrypoint)

    utils.no_state_change(data=data, model=data_entrypoint)


def test_performance_sanity(client):
    data_entrypoint = random_data_entrypoint(client=client)

    @utils.time_it
    def create(c, u):
        return test_data_over_time.create_data_entrypoint(client=c,
                                                          data_entrypoint=u)

    data_entrypoint, _ = create(c=client, u=data_entrypoint)

    @utils.time_it
    def get(c, batch_id: int):
        return test_data_over_time.get_data_over_time(
            client=c, batch_id=batch_id)

    get(c=client, batch_id=data_entrypoint["batch_id"])
