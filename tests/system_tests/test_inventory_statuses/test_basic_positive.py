"""Basic positive tests (happy paths).
This module executes API calls with valid required parameters.
Validation checks:
    Validate status code: All requests should return 2XX HTTP status codes.
    Validate payload: Response is a well-formed JSON object.
    Validate state: GET requests should not change state.
    Validate headers: Verifies if headers are the same as expected.
"""
from tests import utils
from tests.system_tests import test_inventory_statuses


def test_validate_status_codes(client):

    inventory_status = test_inventory_statuses.random_inventory_status()

    # Get inventory_status list should give 200 OK
    data, status_code = test_inventory_statuses.get_inventory_statuses(
        client=client)
    assert status_code == 200

    # For create methods we expect 201 Created
    data, status_code = test_inventory_statuses.create_inventory_status(
        client=client,
        inventory_status=inventory_status)
    assert status_code == 201
    name = data["name"]

    # Retrieve, we expect 200 OK here.
    data, status_code = test_inventory_statuses.get_inventory_status(
        client=client, name=name)
    assert status_code == 200

    # Delete, since we are returning the deleted inventory_status, a 200 OK is
    # expected instead of 204 No Content.

    data, status_code = test_inventory_statuses.delete_inventory_status(
        client=client, name=name)
    assert status_code == 200


def test_validate_payload(client):
    inventory_status = test_inventory_statuses.random_inventory_status()

    # Check if the payload when creating a inventory_status matches expectation
    data, _ = test_inventory_statuses.create_inventory_status(
        client=client, inventory_status=inventory_status)
    utils.no_state_change(data=data, model=inventory_status)

    name = data["name"]

    data, _ = test_inventory_statuses.get_inventory_status(
        client=client, name=name)
    utils.no_state_change(data=data, model=inventory_status)

    # Delete, since we are returning the deleted inventory_status, a 200 OK is
    # expected
    data, status_code = test_inventory_statuses.delete_inventory_status(
        client=client, name=name)
    utils.no_state_change(data=data, model=inventory_status)


def test_validate_headers(client):
    pass


def test_performance_sanity(client):
    random_inventory_status = test_inventory_statuses.random_inventory_status()

    @utils.time_it
    def create(c, u):
        return test_inventory_statuses.create_inventory_status(
            client=c,
            inventory_status=u)

    inventory_status, _ = create(c=client, u=random_inventory_status)

    @utils.time_it
    def get(c, name: str):
        return test_inventory_statuses.get_inventory_status(client=c,
                                                            name=name)

    get(c=client, name=inventory_status["name"])

    @utils.time_it
    def delete(c, name: str):
        return test_inventory_statuses.delete_inventory_status(client=c,
                                                               name=name)

    delete(c=client, name=inventory_status["name"])
