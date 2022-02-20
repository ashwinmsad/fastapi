"""add content column to posts table

Revision ID: 22bdb48a976d
Revises: 1dcdba7df35c
Create Date: 2022-02-20 16:39:07.147158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22bdb48a976d'
down_revision = '1dcdba7df35c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("Content",sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column("posts","Content")
    pass
