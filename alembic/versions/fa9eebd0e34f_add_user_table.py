"""add user table

Revision ID: fa9eebd0e34f
Revises: 22bdb48a976d
Create Date: 2022-02-20 16:51:41.345827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa9eebd0e34f'
down_revision = '22bdb48a976d'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
pass


def downgrade():
    pass
