"""empty message

Revision ID: b7ffb668896b
Revises: 9f0db5811597
Create Date: 2023-07-16 18:20:23.157234

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7ffb668896b'
down_revision = '9f0db5811597'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.alter_column('book_title',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'books', ['book_title'], ['title'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('book_title',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###