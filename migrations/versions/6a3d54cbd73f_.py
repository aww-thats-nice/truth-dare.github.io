"""empty message

Revision ID: 6a3d54cbd73f
Revises: f15a883f58a0
Create Date: 2021-01-25 23:04:42.629775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a3d54cbd73f'
down_revision = 'f15a883f58a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FulfillTask',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bingo_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('user_id', 'bingo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FulfillTask')
    # ### end Alembic commands ###
