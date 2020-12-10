"""add_data_over_time


Revision ID: 651968959957
Revises: f7e26a34ac57
Create Date: 2020-12-10 12:26:19.486140

"""
import sys
import pathlib

# Make migrations importable. noqa: isort skip
DIR_NAME = str(pathlib.Path(__file__).parents[2]) # noqa: isort skip
sys.path.append(DIR_NAME) # noqa: isort skip

from alembic import op
from sqlalchemy import orm
from migrations import helper


# revision identifiers, used by Alembic.
revision = '651968959957'
down_revision = 'f7e26a34ac57'
branch_labels = None
depends_on = None

def upgrade():
    helper.execute(bind=op.get_bind(), path="add_data_over_time/upgrade.sql")

def downgrade():
    helper.execute(bind=op.get_bind(), path="add_data_over_time/downgrade.sql")
