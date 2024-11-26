"""migacao

Revision ID: bff6abec6011
Revises: 
Create Date: 2024-11-22 09:34:56.585811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bff6abec6011'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estudante',
    sa.Column('id_estudante', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('curso', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id_estudante')
    )
    op.create_table('inscricao',
    sa.Column('id_inscricao', sa.Integer(), nullable=False),
    sa.Column('disciplina', sa.String(length=100), nullable=True),
    sa.Column('semestre', sa.String(length=10), nullable=True),
    sa.Column('id_estudante', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_estudante'], ['estudante.id_estudante'], ),
    sa.PrimaryKeyConstraint('id_inscricao')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inscricao')
    op.drop_table('estudante')
    # ### end Alembic commands ###
