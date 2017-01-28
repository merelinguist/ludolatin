"""empty message

Revision ID: 4d4a44bff79d
Revises: e621838fc63d
Create Date: 2017-01-28 16:49:41.135115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d4a44bff79d'
down_revision = 'e621838fc63d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todolist')
    op.drop_table('todo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('description', sa.VARCHAR(length=128), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('finished_at', sa.DATETIME(), nullable=True),
    sa.Column('is_finished', sa.BOOLEAN(), nullable=True),
    sa.Column('creator', sa.VARCHAR(length=64), nullable=True),
    sa.Column('todolist_id', sa.INTEGER(), nullable=True),
    sa.CheckConstraint(u'is_finished IN (0, 1)'),
    sa.ForeignKeyConstraint(['creator'], [u'user.username'], ),
    sa.ForeignKeyConstraint(['todolist_id'], [u'todolist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todolist',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=128), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('creator', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['creator'], [u'user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###