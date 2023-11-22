"""empty message

Revision ID: 8c74002b8935
Revises: ae221c1af9e3
Create Date: 2023-11-21 20:33:07.807403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c74002b8935'
down_revision = 'ae221c1af9e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.String(length=10), nullable=True),
    sa.Column('mass', sa.String(length=10), nullable=True),
    sa.Column('hair_color', sa.String(length=50), nullable=True),
    sa.Column('skin_color', sa.String(length=50), nullable=True),
    sa.Column('eye_color', sa.String(length=50), nullable=True),
    sa.Column('birth_year', sa.String(length=10), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorite_characters',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('favorite_planets',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.drop_table('user')
    op.drop_table('character')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('height', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('mass', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('hair_color', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('skin_color', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('eye_color', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('birth_year', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='character_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('favorite_planets')
    op.drop_table('favorite_characters')
    op.drop_table('users')
    op.drop_table('characters')
    # ### end Alembic commands ###