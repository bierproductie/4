"""This module is for setting up alembic so it's ready for migrations.

This is done by utilizing the config_loader from bierproductie_api.
"""
import logging
import pathlib
import sys
import time
from logging import config as logging_config


from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool

# Make the project importable noqa: isort skip
PROJECT_ROOT_DIR = str(pathlib.Path(__file__).parents[1])  # noqa: isort skip
sys.path.append(PROJECT_ROOT_DIR)  # noqa: isort skip

import bierproductie_api
from bierproductie_api.core import config_loader
from bierproductie_api.core import db


app = bierproductie_api.create_app()
target_metadata = db.DB

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
logging_config.fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", str(config_loader.DB_DSN))


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    retries = 0
    while True:
        try:
            retries += 1
            connection = connectable.connect()
        except Exception:
            if retries < config_loader.DB_RETRY_LIMIT:
                logging.info("Waiting for the database to start...")
                time.sleep(config_loader.DB_RETRY_INTERVAL)
            else:
                logging.error("Max retries reached.")
                raise Exception("Max retries reached.")
        else:
            break

    with connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
