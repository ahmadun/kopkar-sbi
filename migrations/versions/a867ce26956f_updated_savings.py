"""updated savings

Revision ID: a867ce26956f
Revises: e081b0fbb208
Create Date: 2022-07-23 19:17:29.954208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a867ce26956f'
down_revision = 'e081b0fbb208'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('savings', 'save_volu',
               existing_type=sa.VARCHAR(length=250, collation='SQL_Latin1_General_CP1_CI_AS'),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('savings', 'save_volu',
               existing_type=sa.VARCHAR(length=250, collation='SQL_Latin1_General_CP1_CI_AS'),
               nullable=False)
    # ### end Alembic commands ###