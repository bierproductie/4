"""Basic positive tests (happy paths).
This module executes API calls with valid required parameters.
Validation checks:
    Validate status code: All requests should return 2XX HTTP status codes.
    Validate payload: Response is a well-formed JSON object.
    Validate state: GET requests should not change state.
    Validate headers: Verifies if headers are the same as expected.
"""


from tests import utils
from tests.system_tests import test_recipes


def test_validate_status_codes(client):

    recipe = test_recipes.random_recipe()

    # Get recipe list should give 200 OK
    data, status_code = test_recipes.get_recipes(client=client)
    assert status_code == 200

    # For create methods we expect 201 Created
    data, status_code = test_recipes.create_recipe(client=client, recipe=recipe)
    assert status_code == 201
    name = data["name"]

    # Retrieve, we expect 200 OK here.
    data, status_code = test_recipes.get_recipe(client=client, name=name)
    assert status_code == 200

    # Delete, since we are returning the deleted recipe, a 200 OK is expected
    # instead of 204 No Content.
    data, status_code = test_recipes.delete_recipe(client=client, name=name)
    assert status_code == 200


def test_validate_payload(client):
    recipe = test_recipes.random_recipe()

    # Check if the payload when creating a recipe matches what we thing.
    data, _ = test_recipes.create_recipe(client=client, recipe=recipe)
    name = data["name"]

    utils.no_state_change(data=data, model=recipe)

    data, _ = test_recipes.get_recipe(client=client, name=name)
    utils.no_state_change(data=data, model=recipe)

    # Delete, since we are returning the deleted recipe, a 200 OK is expected
    data, status_code = test_recipes.delete_recipe(client=client, name=name)
    utils.no_state_change(data=data, model=recipe)


def test_validate_headers(client):
    pass


def test_performance_sanity(client):
    mock_recipe = test_recipes.random_recipe()

    @utils.time_it
    def create(c, u):
        return test_recipes.create_recipe(client=c, recipe=u)

    recipe, _ = create(c=client, u=mock_recipe)

    @utils.time_it
    def get(c, name: str):
        return test_recipes.get_recipe(client=c, name=name)

    get(c=client, name=recipe["name"])

    @utils.time_it
    def delete(c, name: str):
        return test_recipes.delete_recipe(client=c, name=name)

    delete(c=client, name=recipe["name"])
