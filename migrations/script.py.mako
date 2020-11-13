"""${message}


Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
import sys
import pathlib

# Make migrations importable. noqa: isort skip
DIR_NAME = str(pathlib.Path(__file__).parents[2]) # noqa: isort skip
sys.path.append(DIR_NAME) # noqa: isort skip

from alembic import op
from sqlalchemy import orm
from migrations import helper
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

def upgrade():
    helper.execute(bind=op.get_bind(), path="${message}/upgrade.sql")

def downgrade():
    helper.execute(bind=op.get_bind(), path="${message}/downgrade.sql")
