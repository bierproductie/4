"""add_recipes


Revision ID: 7078d771234e
Revises: 
Create Date: 2020-12-10 12:16:09.229147

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
revision = '7078d771234e'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    helper.execute(bind=op.get_bind(), path="add_recipes/upgrade.sql")

def downgrade():
    helper.execute(bind=op.get_bind(), path="add_recipes/downgrade.sql")
