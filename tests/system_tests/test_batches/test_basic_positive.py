"""Basic positive tests (happy paths).
This module executes API calls with valid required parameters.
Validation checks:
    Validate status code: All requests should return 2XX HTTP status codes.
    Validate payload: Response is a well-formed JSON object.
    Validate state: GET requests should not change state.
    Validate headers: Verifies if headers are the same as expected.
"""
from tests import utils
from tests.system_tests import test_batches, test_recipes


def test_validate_status_codes(client):
    random_recipe = test_recipes.random_recipe()
    recipe, _ = test_recipes.create_recipe(client=client, recipe=random_recipe)

    batch = test_batches.random_batch(recipe_name=recipe["name"])

    # Get batch list should give 200 OK
    data, status_code = test_batches.get_batches(client=client)
    assert status_code == 200

    # For create methods we expect 201 Created
    data, status_code = test_batches.create_batch(client=client,
                                                  batch=batch)
    assert status_code == 201
    identifier = data["identifier"]

    # Retrieve, we expect 200 OK here.
    data, status_code = test_batches.get_batch(
        client=client, identifier=identifier)
    assert status_code == 200

    # Delete, since we are returning the deleted batch, a 200 OK is expected
    # instead of 204 No Content.
    data, status_code = test_batches.delete_batch(
        client=client, identifier=identifier)
    assert status_code == 200


def test_validate_payload(client):
    random_recipe = test_recipes.random_recipe()
    recipe, _ = test_recipes.create_recipe(client=client, recipe=random_recipe)
    batch = test_batches.random_batch(recipe_name=recipe["name"])

    # Check if the payload when creating a batch matches what we thing.
    data, _ = test_batches.create_batch(client=client, batch=batch)

    # API should save the email as lowercase.
    utils.no_state_change(data=data, model=batch)

    # Check if the provided identifier (UUID4) is valid
    identifier = data["identifier"]
    # Check if valid identifier TODO

    data, _ = test_batches.get_batch(client=client, identifier=identifier)
    utils.no_state_change(data=data, model=batch)

    # Delete, since we are returning the deleted batch, a 200 OK is expected
    data, status_code = test_batches.delete_batch(
        client=client, identifier=identifier)
    utils.no_state_change(data=data, model=batch)


def test_validate_headers(client):
    pass


def test_performance_sanity(client):
    random_recipe = test_recipes.random_recipe()
    recipe, _ = test_recipes.create_recipe(client=client, recipe=random_recipe)
    random_batch = test_batches.random_batch(recipe_name=recipe["name"])


    @utils.time_it
    def create(c, u):
        return test_batches.create_batch(client=c, batch=u)

    batch, _ = create(c=client, u=random_batch)

    @utils.time_it
    def get(c, identifier: int):
        return test_batches.get_batch(client=c, identifier=identifier)

    get(c=client, identifier=batch["identifier"])

    @utils.time_it
    def delete(c, identifier: int):
        return test_batches.delete_batch(client=c, identifier=identifier)

    delete(c=client, identifier=batch["identifier"])
