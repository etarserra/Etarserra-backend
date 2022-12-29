"""empty message

Revision ID: f949b0f1562d
Revises: def91b06fa61
Create Date: 2022-12-28 19:32:07.077514

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f949b0f1562d'
down_revision = 'def91b06fa61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=mysql.VARCHAR(collation='utf8_unicode_ci', length=100),
               type_=sa.String(length=1000),
               existing_nullable=True)

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

    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(collation='utf8_unicode_ci', length=100),
               existing_nullable=True)

    # ### end Alembic commands ###