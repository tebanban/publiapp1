"""empty message

Revision ID: 6b1658e36215
Revises: af639dd53699
Create Date: 2022-04-07 11:35:46.178924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b1658e36215'
down_revision = 'af639dd53699'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('name', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'name')
    # ### end Alembic commands ###