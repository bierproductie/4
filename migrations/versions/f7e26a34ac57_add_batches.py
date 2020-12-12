"""add_batches


Revision ID: f7e26a34ac57
Revises: 7078d771234e
Create Date: 2020-12-10 12:20:04.880063

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
revision = 'f7e26a34ac57'
down_revision = '7078d771234e'
branch_labels = None
depends_on = None

def upgrade():
    helper.execute(bind=op.get_bind(), path="add_batches/upgrade.sql")

def downgrade():
    helper.execute(bind=op.get_bind(), path="add_batches/downgrade.sql")
