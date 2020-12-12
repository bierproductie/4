"""Basic positive tests (happy paths).
This module executes API calls with valid required parameters.
Validation checks:
    Validate status code: All requests should return 2XX HTTP status codes.
    Validate payload: Response is a well-formed JSON object.
    Validate state: GET requests should not change state.
    Validate headers: Verifies if headers are the same as expected.
"""
from tests import utils
from tests.system_tests import test_maintenance


def test_validate_status_codes(client):

    maintx = test_maintenance.random_maintx()

    # Get maintx list should give 200 OK
    data, status_code = test_maintenance.get(client=client)
    assert status_code == 200

    data, status_code = test_maintenance.update(client=client,
                                                maintx=maintx)
    assert status_code == 200


def test_validate_payload(client):
    maintx = test_maintenance.random_maintx()

    data, _ = test_maintenance.update(client=client, maintx=maintx)
    utils.no_state_change(data=data, model=maintx)


def test_performance_sanity(client):
    mock_maintx = test_maintenance.random_maintx()

    @utils.time_it
    def update(c, u):
        return test_maintenance.update(client=c, maintx=u)

    maintx, _ = update(c=client, u=mock_maintx)
