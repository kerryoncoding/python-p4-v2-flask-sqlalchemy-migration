"""rename address

Revision ID: 67e538ad8912
Revises: 8f37e432f808
Create Date: 2023-12-20 10:29:04.574871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67e538ad8912'
down_revision = '8f37e432f808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')

    # ### end Alembic commands ###
