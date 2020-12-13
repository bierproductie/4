"""This module is for implementing batch services.

The Service class' job is to interface with the batch queries, and
transform the result provided by the Queries class into Schemas. When
creating an instance of Service() you shouldn't call
`service._queries()` directly, hence why it's declared as private (_).
"""

from bierproductie_api.core import config_loader
from bierproductie_api.core import exceptions

import requests
from requests import exceptions as request_exceptions


class Service:
    """Service."""

    url = f"{config_loader.OPCUA_CLIENT_URL}/command"
    allowed_methods = {'start', 'stop', 'clear', 'reset', 'abort'}

    def send(self, method: str):
        if method not in self.allowed_methods:
            msg = f"The method: '{method}' is not allowed"
            raise exceptions.BadRequest(detail=msg)
        try:
            requests.post(self.url, json=dict(method=method))
        except request_exceptions.ConnectionError:
            raise exceptions.ServiceUnavailable(
                detail=f"OPC-UA client ({self.url}) is not reachable.")
