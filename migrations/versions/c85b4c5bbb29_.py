"""empty message

Revision ID: c85b4c5bbb29
Revises: f16f3de08d71
Create Date: 2022-03-23 14:06:46.095133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c85b4c5bbb29'
down_revision = 'f16f3de08d71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('valla',
    sa.Column('valla_id', sa.Integer(), nullable=False),
    sa.Column('site_code', sa.String(length=10), nullable=False),
    sa.Column('owner_name', sa.String(length=150), nullable=False),
    sa.Column('size', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('price_low', sa.Integer(), nullable=True),
    sa.Column('price_high', sa.Integer(), nullable=True),
    sa.Column('view', sa.String(length=150), nullable=False),
    sa.Column('route', sa.String(length=150), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('client_name', sa.String(length=150), nullable=True),
    sa.Column('status', sa.String(length=40), nullable=True),
    sa.Column('register_date', sa.Date(), nullable=False),
    sa.Column('register_user', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('valla_id'),
    sa.UniqueConstraint('site_code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('valla')
    # ### end Alembic commands ###
