"""empty message

Revision ID: ebdab63129cc
Revises: ef2dd074a24f
Create Date: 2022-04-14 00:41:41.319784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebdab63129cc'
down_revision = 'ef2dd074a24f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('company', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('company'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('company', sa.String(length=80), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('company'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_price', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('finish_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('payment_date', sa.DateTime(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('valla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('format', sa.String(length=20), nullable=False),
    sa.Column('ligth', sa.Boolean(), nullable=True),
    sa.Column('price_low', sa.Float(), nullable=True),
    sa.Column('price_high', sa.Float(), nullable=True),
    sa.Column('view', sa.String(length=150), nullable=False),
    sa.Column('route', sa.String(length=150), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
    sa.ForeignKeyConstraint(['size_id'], ['size.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('valla')
    op.drop_table('payment')
    op.drop_table('order')
    op.drop_table('client')
    op.drop_table('user')
    op.drop_table('type')
    op.drop_table('status')
    op.drop_table('size')
    op.drop_table('role')
    op.drop_table('owner')
    # ### end Alembic commands ###