"""add member

Revision ID: 68ec617084f2
Revises: c9829ba92f1b
Create Date: 2022-08-09 20:43:00.626660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68ec617084f2'
down_revision = 'c9829ba92f1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('nik', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('created_by', sa.String(length=250), nullable=False),
    sa.Column('updated_by', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('nik')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('members')
    # ### end Alembic commands ###
