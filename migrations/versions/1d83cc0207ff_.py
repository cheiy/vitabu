"""empty message

Revision ID: 1d83cc0207ff
Revises: e23c62e03355
Create Date: 2023-07-08 22:11:26.004331

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1d83cc0207ff'
down_revision = 'e23c62e03355'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'subjects', ['subject_id'], ['subject_id'])

    with op.batch_alter_table('listings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['user_id'])

    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.alter_column('ISBN_code',
               existing_type=mysql.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.alter_column('added_by',
               existing_type=mysql.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.alter_column('date_added',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.Integer(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.create_unique_constraint(None, ['ISBN_code'])
        batch_op.create_foreign_key(None, 'users', ['added_by'], ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('date_added',
               existing_type=sa.Integer(),
               type_=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('added_by',
               existing_type=sa.Integer(),
               type_=mysql.BIGINT(),
               existing_nullable=True)
        batch_op.alter_column('ISBN_code',
               existing_type=sa.Integer(),
               type_=mysql.BIGINT(),
               existing_nullable=True)

    with op.batch_alter_table('listings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
