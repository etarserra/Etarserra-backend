"""empty message

Revision ID: ab6746340aca
Revises: 889f3785ff64
Create Date: 2022-08-02 20:14:33.233095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab6746340aca'
down_revision = '889f3785ff64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_tag',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_tag')
    # ### end Alembic commands ###
