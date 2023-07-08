"""empty message

Revision ID: ed92ee52907c
Revises: 477034bc3345
Create Date: 2023-07-08 22:36:15.646190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed92ee52907c'
down_revision = '477034bc3345'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('added_by', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['added_by'], ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('added_by')

    # ### end Alembic commands ###
