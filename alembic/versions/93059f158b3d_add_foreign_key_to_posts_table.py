"""add foreign key to posts table

Revision ID: 93059f158b3d
Revises: fa9eebd0e34f
Create Date: 2022-02-20 17:01:58.005137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93059f158b3d'
down_revision = 'fa9eebd0e34f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
