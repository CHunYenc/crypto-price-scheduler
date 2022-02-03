"""empty message

Revision ID: ef11ed8a5ece
Revises: fb6bff147f9e
Create Date: 2022-02-02 00:07:03.019673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef11ed8a5ece'
down_revision = 'fb6bff147f9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('focus_symbol_symbol_A_key', 'focus_symbol', type_='unique')
    op.drop_constraint('focus_symbol_symbol_B_key', 'focus_symbol', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('focus_symbol_symbol_B_key', 'focus_symbol', ['symbol_B'])
    op.create_unique_constraint('focus_symbol_symbol_A_key', 'focus_symbol', ['symbol_A'])
    # ### end Alembic commands ###