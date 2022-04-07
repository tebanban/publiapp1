"""empty message

Revision ID: fbf7f2a830a4
Revises: 19e4b9b73e31
Create Date: 2022-03-22 12:07:42.935102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbf7f2a830a4'
down_revision = '19e4b9b73e31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('owner', sa.String(length=150), nullable=False),
    sa.Column('size', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('price_low', sa.Integer(), nullable=True),
    sa.Column('price_high', sa.Integer(), nullable=True),
    sa.Column('view', sa.String(length=50), nullable=False),
    sa.Column('route', sa.String(length=150), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('client', sa.String(length=150), nullable=True),
    sa.Column('status', sa.String(length=40), nullable=True),
    sa.Column('register_date', sa.Date(), nullable=False),
    sa.Column('register_user', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site')
    # ### end Alembic commands ###