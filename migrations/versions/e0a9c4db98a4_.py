"""empty message

Revision ID: e0a9c4db98a4
Revises: 24b14e42e2b9
Create Date: 2022-04-08 15:06:53.857152

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e0a9c4db98a4'
down_revision = '24b14e42e2b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('client', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('order', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('owner', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('user', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('valla', sa.Column('comment', sa.Text(), nullable=True))
    op.add_column('valla', sa.Column('type_id', sa.Integer(), nullable=False))
    op.alter_column('valla', 'format',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('valla', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.create_foreign_key(None, 'valla', 'type', ['type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'valla', type_='foreignkey')
    op.alter_column('valla', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('valla', 'format',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.drop_column('valla', 'type_id')
    op.drop_column('valla', 'comment')
    op.alter_column('user', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('owner', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('order', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('client', 'created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_table('type')
    # ### end Alembic commands ###
