"""empty message

Revision ID: 19f094e8c58e
Revises: 064ac633e501
Create Date: 2023-07-15 14:05:31.908581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '19f094e8c58e'
down_revision = '064ac633e501'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_authors',
    sa.Column('bookauthor_id', sa.BigInteger(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.author_id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['books.book_id'], ),
    sa.PrimaryKeyConstraint('bookauthor_id')
    )
    op.create_table('book_listings',
    sa.Column('booklisting_id', sa.BigInteger(), nullable=False),
    sa.Column('book_id', sa.BigInteger(), nullable=True),
    sa.Column('listing_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.book_id'], ),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.listing_id'], ),
    sa.PrimaryKeyConstraint('booklisting_id')
    )
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.alter_column('isbn_code',
               existing_type=mysql.BIGINT(),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('subject_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('publisher_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('grade_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['isbn_code'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('grade_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('publisher_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('subject_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('isbn_code',
               existing_type=mysql.BIGINT(),
               nullable=False)

    op.drop_table('book_listings')
    op.drop_table('book_authors')
    # ### end Alembic commands ###
