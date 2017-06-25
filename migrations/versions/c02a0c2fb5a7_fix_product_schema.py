"""Fix product schema

Revision ID: c02a0c2fb5a7
Revises: 4d7dc047efed
Create Date: 2017-06-24 23:20:55.937976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c02a0c2fb5a7'
down_revision = '4d7dc047efed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')

    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('order', sa.Integer(), nullable=True),
        sa.Column('hidden', sa.Boolean(), nullable=True),
        sa.Column('url_github', sa.String(), nullable=True),
        sa.Column('url_circleci', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.create_table(
        'product',
        sa.Column('key', sa.Integer(), nullable=False),
        sa.Column('id', sa.String(), nullable=True),
        sa.Column('index', sa.Integer(), nullable=True),
        sa.Column('hidden', sa.Boolean(), nullable=True),
        sa.Column('url_github', sa.String(), nullable=True),
        sa.Column('url_circleci', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('key')
    )
    # ### end Alembic commands ###