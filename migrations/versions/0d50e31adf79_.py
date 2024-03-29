"""empty message

Revision ID: 0d50e31adf79
Revises: 56774ff34055
Create Date: 2023-07-16 15:50:46.414346

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0d50e31adf79'
down_revision = '56774ff34055'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'authors', ['author_id'], ['author_id'])
        batch_op.create_foreign_key(None, 'grades', ['grade_id'], ['grade_id'])
        batch_op.drop_column('book_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_name', mysql.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
