"""
${message}

Revision ID : ${up_revision}
Revises : ${down_revision}
Create Date : ${create_date}

"""

# revision identifiers ,used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}

from alembic import op
import sqlalchemy as sa
${imports_if import else ""}

def upgrade():
    ${upgrades_if upgrades else "pass"}

def downgrade():
    ${downgrades_if downgrades else "pass"}