"""Add bio column

Revision ID: 60d1678977ab
Revises: 6956f6f2a0a1
Create Date: 2023-10-08 17:13:44.452394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d1678977ab'
down_revision = '6956f6f2a0a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('bio')

    # ### end Alembic commands ###
