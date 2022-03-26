"""empty message

Revision ID: 6f6ceec292ec
Revises: c85b4c5bbb29
Create Date: 2022-03-25 17:41:09.253664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f6ceec292ec'
down_revision = 'c85b4c5bbb29'
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
    op.add_column('valla', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('valla', sa.Column('code', sa.String(length=10), nullable=False))
    op.add_column('valla', sa.Column('name', sa.String(length=150), nullable=False))
    op.add_column('valla', sa.Column('estructure', sa.String(length=50), nullable=False))
    op.add_column('valla', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.add_column('valla', sa.Column('client_id', sa.Integer(), nullable=False))
    op.drop_constraint('valla_site_code_key', 'valla', type_='unique')
    op.create_unique_constraint(None, 'valla', ['code'])
    op.create_foreign_key(None, 'valla', 'owner', ['owner_id'], ['id'])
    op.create_foreign_key(None, 'valla', 'client', ['client_id'], ['id'])
    op.drop_column('valla', 'type')
    op.drop_column('valla', 'owner_name')
    op.drop_column('valla', 'valla_id')
    op.drop_column('valla', 'client_name')
    op.drop_column('valla', 'site_code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('valla', sa.Column('site_code', sa.VARCHAR(length=10), autoincrement=False, nullable=False))
    op.add_column('valla', sa.Column('client_name', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    op.add_column('valla', sa.Column('valla_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('valla', sa.Column('owner_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.add_column('valla', sa.Column('type', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'valla', type_='foreignkey')
    op.drop_constraint(None, 'valla', type_='foreignkey')
    op.drop_constraint(None, 'valla', type_='unique')
    op.create_unique_constraint('valla_site_code_key', 'valla', ['site_code'])
    op.drop_column('valla', 'client_id')
    op.drop_column('valla', 'owner_id')
    op.drop_column('valla', 'estructure')
    op.drop_column('valla', 'name')
    op.drop_column('valla', 'code')
    op.drop_column('valla', 'id')
    op.drop_table('owner')
    op.drop_table('client')
    # ### end Alembic commands ###
