"""Initial

Revision ID: 919694b65836
Revises: 
Create Date: 2023-04-27 18:05:58.548162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919694b65836'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_name', sa.String(), nullable=False),
    sa.Column('task_description', sa.String(), nullable=True),
    sa.Column('task_start', sa.TIMESTAMP(), nullable=False),
    sa.Column('task_end', sa.TIMESTAMP(), nullable=False),
    sa.Column('task_create', sa.TIMESTAMP(), nullable=False),
    sa.Column('task_progress', sa.Integer(), nullable=False),
    sa.Column('task_author', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
