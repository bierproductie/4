"""
Helper class for executing SQL code.

This file is used for simplyfying logic in the different migration version
files. Instead of using the ORM for migrations we craft our own SQL.
"""
import pathlib

from sqlalchemy import orm


def execute(bind, path: str):
    """
    Execute SQL.

    Executes SQL found in the file provided by the path and commits it to the
    DB.

    Args:
        bind:
            Bind to the database.
        path (str):
            Relative path to the SQL file, the path is relative to
            migrations/versions/YOUR_PATH_FROM_HERE.
    """
    session = orm.Session(bind=bind)
    path = "migrations/versions/{path}".format(path=path)
    file_path = pathlib.Path(path).absolute()
    with open(file_path) as sql_file:
        sql_to_execute = sql_file.read()
        session.execute(sql_to_execute)
        session.commit()
