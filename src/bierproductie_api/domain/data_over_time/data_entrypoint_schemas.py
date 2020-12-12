"""This module is for schemas related to data_over_time.

These schemas are used for creating new instances of data_entrypoint. Returning
paginated result (`Paginated`) and transforming a data_entrypoint

"""
from typing import List, Optional
import datetime

import pydantic

from bierproductie_api.domain import base_schemas


class _Base(pydantic.BaseModel):
    """Used as baseclass for all other schemas inside this module.

    The base schema is kept private (by leftpadding with `_`).
    """

    batch_id: Optional[int] = pydantic.Field(None)
    measurement_ts: Optional[datetime.datetime] = pydantic.Field(None)
    temperature: Optional[float] = pydantic.Field(None)
    humidity: Optional[float] = pydantic.Field(None)
    vibration: Optional[float] = pydantic.Field(None)
    produced: Optional[int] = pydantic.Field(None)
    state: Optional[int] = pydantic.Field(None)
    rejected: Optional[int] = pydantic.Field(None)


class Create(pydantic.BaseModel):
    """Create schema is used for validating POST requests."""
    batch_id: int = pydantic.Field(...)
    measurement_ts: datetime.datetime = pydantic.Field(...)
    temperature: float = pydantic.Field(...)
    humidity: float = pydantic.Field(...)
    vibration: float = pydantic.Field(...)
    produced: int = pydantic.Field(..., ge=0)
    state: int = pydantic.Field(...)
    rejected: int = pydantic.Field(..., ge=0)

    @pydantic.validator("measurement_ts")
    def ts_must_contain_timezone(cls, value: datetime.datetime):  # This is a class due to the decorator returning a callable classmethod pylint: disable=no-self-argument
        if value.tzinfo is None:
            raise ValueError("Timestamp must contain a timezone")
        return value


class Update(_Base):
    """Update schema is used for validating POST requests."""


class DB(_Base):
    """DB schema is used for transforming an ORM model to a pydantic model."""

    inserted_ts: datetime.datetime

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
