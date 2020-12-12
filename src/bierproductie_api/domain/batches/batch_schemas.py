"""This module is for schemas related to batches.

These schemas are used for creating new instances of batch. Returning
paginated result (`Paginated`) and transforming a batch

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

    speed: Optional[int] = pydantic.Field(None)
    amount_to_produce: Optional[int] = pydantic.Field(None)
    started_dt: Optional[datetime.datetime] = pydantic.Field(None)
    recipe_id: Optional[str] = pydantic.Field(None, max_length=128)
    finished_dt: Optional[datetime.datetime] = pydantic.Field(None)
    oee: Optional[float] = pydantic.Field(None)


class Create(_Base):
    """Create schema is used for validating POST requests."""


class Update(_Base):
    """Update schema is used for validating POST requests."""


class DB(_Base):
    """DB schema is used for transforming an ORM model to a pydantic model."""
    identifier: int

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
