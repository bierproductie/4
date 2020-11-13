"""Common schemas
"""
import pydantic


class Pagination(pydantic.BaseModel):
    """Pagination"""
    more: bool
    total: int
    number_of_pages: int
