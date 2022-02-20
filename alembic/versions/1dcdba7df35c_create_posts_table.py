"""create posts table

Revision ID: 1dcdba7df35c
Revises: 
Create Date: 2022-02-20 16:25:04.310386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dcdba7df35c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
    sa.Column("title",sa.String,nullable=False))
    pass


def downgrade():
    pass
