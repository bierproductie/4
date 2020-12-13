"""This module is for schemas related to inventory_statuses.

These schemas are used for creating new instances of inventory_status. Returning
paginated result (`Paginated`) and transforming a inventory_status

"""
from typing import List
from typing import Optional

import pydantic

from bierproductie_api.domain import base_schemas


class _Base(pydantic.BaseModel):
    """Used as baseclass for all other schemas inside this module.

    The base schema is kept private (by leftpadding with `_`).
    """
    name: Optional[str] = pydantic.Field(None)
    max_value: Optional[float] = pydantic.Field(None)
    current_value: Optional[float] = pydantic.Field(None)


class Create(_Base):
    """Create schema is used for validating POST requests."""


class Update(_Base):
    """Update schema is used for validating POST requests."""


class DB(_Base):
    """DB schema is used for transforming an ORM model to a pydantic model."""

    class Config:
        """We set orm_mode to True to allow transforming the ORM model."""

        orm_mode = True


class Paginated(pydantic.BaseModel):
    """Paginated result schema.

    An example paginated result could look like this.
    return {
        results = [],
        pagination {
            more = True,
            total = 1000
        }
    }
    """

    results: List[DB]
    pagination: base_schemas.Pagination
