"""init

Revision ID: d9a5825853bd
Revises: 
Create Date: 2021-11-17 08:48:00.501073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9a5825853bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('jobs')