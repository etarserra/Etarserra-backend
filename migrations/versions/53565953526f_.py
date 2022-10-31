"""empty message

Revision ID: 53565953526f
Revises: 92b33ef46e77
Create Date: 2022-08-19 20:39:24.098624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53565953526f'
down_revision = '92b33ef46e77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('creationTimeStamp', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'file', 'user', ['creator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'file', type_='foreignkey')
    op.drop_column('file', 'creationTimeStamp')
    # ### end Alembic commands ###
