"""This module is for schemas related to maintenance.

These schemas are used for creating new instances of maintx. Returning
paginated result (`Paginated`) and transforming a maintx

"""
import datetime
from typing import List
from typing import Optional

import pydantic

from bierproductie_api.domain import base_schemas


class _Base(pydantic.BaseModel):
    """Used as baseclass for all other schemas inside this module.

    The base schema is kept private (by leftpadding with `_`).
    """
    value: Optional[float] = pydantic.Field(None)
    updated_ts: Optional[datetime.datetime] = pydantic.Field(None)


class Create(pydantic.BaseModel):
    """Create schema is used for validating POST requests."""
    value: float = pydantic.Field(...)


class Update(pydantic.BaseModel):
    """Update schema is used for validating POST requests."""
    value: float = pydantic.Field(...)


class DB(_Base):
    """DB schema is used for transforming an ORM model to a pydantic model."""
    updated_ts: datetime.datetime = pydantic.Field(...)

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
