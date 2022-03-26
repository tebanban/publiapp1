"""empty message

Revision ID: 2c25cf82d851
Revises: 6f6ceec292ec
Create Date: 2022-03-25 17:45:54.324640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c25cf82d851'
down_revision = '6f6ceec292ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('company', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('company'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('company', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('company'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('valla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('size', sa.String(length=50), nullable=False),
    sa.Column('estructure', sa.String(length=50), nullable=False),
    sa.Column('price_low', sa.Float(), nullable=True),
    sa.Column('price_high', sa.Float(), nullable=True),
    sa.Column('view', sa.String(length=150), nullable=False),
    sa.Column('route', sa.String(length=150), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=40), nullable=True),
    sa.Column('register_date', sa.Date(), nullable=False),
    sa.Column('register_user', sa.String(length=60), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('valla')
    op.drop_table('owner')
    op.drop_table('client')
    # ### end Alembic commands ###
