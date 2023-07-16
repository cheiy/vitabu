"""empty message

Revision ID: 9f0db5811597
Revises: 4637709c1d6c
Create Date: 2023-07-16 18:18:42.935023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f0db5811597'
down_revision = '4637709c1d6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_title', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'books', ['book_title'], ['title'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('book_title')

    # ### end Alembic commands ###