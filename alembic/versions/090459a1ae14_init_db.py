"""init_db

Revision ID: 090459a1ae14
Revises: ded38d029cef
Create Date: 2024-05-23 10:54:38.826817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090459a1ae14'
down_revision = 'ded38d029cef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categorias', 'nome',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categorias', 'nome',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    # ### end Alembic commands ###