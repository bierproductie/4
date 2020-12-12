"""add_maintenance


Revision ID: f757869bbcbd
Revises: bc5a1382ddad
Create Date: 2020-12-10 12:27:24.511227

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
revision = 'f757869bbcbd'
down_revision = 'bc5a1382ddad'
branch_labels = None
depends_on = None

def upgrade():
    helper.execute(bind=op.get_bind(), path="add_maintenance/upgrade.sql")

def downgrade():
    helper.execute(bind=op.get_bind(), path="add_maintenance/downgrade.sql")
