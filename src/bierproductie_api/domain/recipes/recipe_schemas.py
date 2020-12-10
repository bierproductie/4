"""This module is for schemas related to recipes.

These schemas are used for creating new instances of recipe. Returning
paginated result (`Paginated`) and transforming a recipe

"""
from typing import Optional

import pydantic


class _Base(pydantic.BaseModel):
    """Used as baseclass for all other schemas inside this module.

    The base schema is kept private (by leftpadding with `_`).
    """

    machine_id: Optional[float] = pydantic.Field(None)
    max_speed: Optional[int] = pydantic.Field(None)
    recommended_speed: Optional[int] = pydantic.Field(None)
    name: Optional[str] = pydantic.Field(None, max_length=128)


class Create(_Base):
    """Create schema is used for validating POST requests."""
    machine_id: float
    max_speed: int = pydantic.Field(..., ge=0, le=1000)
    recommended_speed: int = pydantic.Field(..., ge=0, le=1000)
    name: str = pydantic.Field(..., max_length=128)


class Update(_Base):
    """Update schema is used for validating POST requests."""


class DB(_Base):
    """DB schema is used for transforming an ORM model to a pydantic model."""
    class Config:
        """We set orm_mode to True to allow transforming the ORM model."""

        orm_mode = True
