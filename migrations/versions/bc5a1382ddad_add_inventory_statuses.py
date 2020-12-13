"""add_inventory_statuses


Revision ID: bc5a1382ddad
Revises: 651968959957
Create Date: 2020-12-10 12:27:14.142374

"""
import sys
import pathlib

# Make migrations importable. noqa: isort skip
DIR_NAME = str(pathlib.Path(__file__).parents[2])  # noqa: isort skip
sys.path.append(DIR_NAME)  # noqa: isort skip

from alembic import op
from sqlalchemy import orm
from migrations import helper


# revision identifiers, used by Alembic.
revision = 'bc5a1382ddad'
down_revision = '651968959957'
branch_labels = None
depends_on = None


def upgrade():
    helper.execute(bind=op.get_bind(),
                   path="add_inventory_statuses/upgrade.sql")


def downgrade():
    helper.execute(bind=op.get_bind(),
                   path="add_inventory_statuses/downgrade.sql")
