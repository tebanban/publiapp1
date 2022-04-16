"""empty message

Revision ID: 600e27e95065
Revises: 6e7c601c8ab9
Create Date: 2022-04-08 10:23:29.035061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '600e27e95065'
down_revision = '6e7c601c8ab9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('valla', sa.Column('status_id', sa.Integer(), nullable=True))
    op.add_column('valla', sa.Column('size_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'valla', 'status', ['status_id'], ['id'])
    op.create_foreign_key(None, 'valla', 'size', ['size_id'], ['id'])
    op.drop_column('valla', 'structure')
    op.drop_column('valla', 'status')
    op.drop_column('valla', 'size')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('valla', sa.Column('size', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('valla', sa.Column('status', sa.VARCHAR(length=40), autoincrement=False, nullable=True))
    op.add_column('valla', sa.Column('structure', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'valla', type_='foreignkey')
    op.drop_constraint(None, 'valla', type_='foreignkey')
    op.drop_column('valla', 'size_id')
    op.drop_column('valla', 'status_id')
    op.drop_table('status')
    op.drop_table('size')
    # ### end Alembic commands ###
