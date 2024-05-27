"""empty message

Revision ID: fa9acd963c90
Revises: bc878a2ddbac
Create Date: 2023-11-09 19:31:31.533500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa9acd963c90'
down_revision = 'bc878a2ddbac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_roles',
    sa.Column('User_id', sa.Integer(), nullable=False),
    sa.Column('roles_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['User_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['roles_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('User_id', 'roles_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    # ### end Alembic commands ###
