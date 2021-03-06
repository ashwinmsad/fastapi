"""auto vote

Revision ID: 086e195be3e5
Revises: e9587b7f440e
Create Date: 2022-02-20 17:40:33.946385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '086e195be3e5'
down_revision = 'e9587b7f440e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.drop_column('posts', 'Content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('Content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('posts', 'content')
    op.drop_table('votes')
    # ### end Alembic commands ###
