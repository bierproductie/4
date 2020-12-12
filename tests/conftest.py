"""This module is for setting up our APP, so that test cases doesn't need to"""
import pathlib
import subprocess
import sys

import bierproductie_api
import pytest
from fastapi import testclient


@pytest.fixture
def app():
    """app."""
    return bierproductie_api.create_app()


@pytest.fixture
def client(app):
    """client.

    Args:
        app:
    """
    cwd = pathlib.Path(__file__).parent.parent
    try:
        subprocess.check_call(["alembic", "upgrade", "head"], cwd=cwd)
    except subprocess.CalledProcessError:
        sys.exit(1)
    with testclient.TestClient(app) as test_client:
        yield test_client
