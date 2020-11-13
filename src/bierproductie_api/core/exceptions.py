"""This module is for custom exceptions to make the exceptions layer as
independant as possible on the chosen framework.
"""
import fastapi


class NotFound(fastapi.HTTPException):

    def __init__(self, detail=None):
        super().__init__(status_code=404, detail=detail)


class Conflict(fastapi.HTTPException):

    def __init__(self, detail="Such an entry already exists"):
        super().__init__(status_code=409, detail=detail)
