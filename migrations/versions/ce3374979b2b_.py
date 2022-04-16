"""empty message

Revision ID: ce3374979b2b
Revises: 52cd83f06e5b
Create Date: 2022-03-22 16:01:12.497630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce3374979b2b'
down_revision = '52cd83f06e5b'
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
    sa.Column('view', sa.String(length=150), nullable=False),
    sa.Column('route', sa.String(length=150), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('client', sa.String(length=150), nullable=True),
    sa.Column('status', sa.String(length=40), nullable=True),
    sa.Column('register_date', sa.Date(), nullable=False),
    sa.Column('register_user', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site')
    # ### end Alembic commands ###
