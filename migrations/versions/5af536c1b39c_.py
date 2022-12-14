"""empty message

Revision ID: 5af536c1b39c
Revises: 3192b997fa6b
Create Date: 2022-12-23 12:14:19.879708

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5af536c1b39c'
down_revision = '3192b997fa6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.TINYBLOB(),
               type_=sa.LargeBinary(length=128),
               existing_nullable=False)
        batch_op.alter_column('verificationPinHash',
               existing_type=mysql.TINYBLOB(),
               type_=sa.LargeBinary(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('verificationPinHash',
               existing_type=sa.LargeBinary(length=128),
               type_=mysql.TINYBLOB(),
               existing_nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=sa.LargeBinary(length=128),
               type_=mysql.TINYBLOB(),
               existing_nullable=False)

    # ### end Alembic commands ###
