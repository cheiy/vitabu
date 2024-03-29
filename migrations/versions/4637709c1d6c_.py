"""empty message

Revision ID: 4637709c1d6c
Revises: 45f0d33c1376
Create Date: 2023-07-16 18:06:36.642231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4637709c1d6c'
down_revision = '45f0d33c1376'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'users', ['listed_by'], ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_listings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
