"""Remove token expiration

Revision ID: 6a9cee4abac1
Revises: 2c139efa98a6
Create Date: 2017-09-15 14:45:21.455235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a9cee4abac1'
down_revision = '2c139efa98a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oauth_accesstoken', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'oauth_accesstoken', 'user', ['user_id'], ['id'])
    op.drop_column('oauth_accesstoken', 'expiration')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oauth_accesstoken', sa.Column('expiration', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'oauth_accesstoken', type_='foreignkey')
    op.drop_column('oauth_accesstoken', 'user_id')
    # ### end Alembic commands ###
