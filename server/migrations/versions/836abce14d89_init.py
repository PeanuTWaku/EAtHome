"""init

Revision ID: 836abce14d89
Revises: 
Create Date: 2022-11-10 21:06:26.593896

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '836abce14d89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('account', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('display_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('phone', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('account')
    )
    op.create_table('shop',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('revenue', sa.Integer(), nullable=False),
    sa.Column('owner_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['owner_name'], ['user.account'], ),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_index(op.f('ix_shop_category'), 'shop', ['category'], unique=False)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('PLACE', 'FINISH', 'CANCEL', name='orderstatus'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('finished_at', sa.DateTime(), nullable=True),
    sa.Column('method', sa.Enum('PICKUP', 'DELIVERY', name='ordermethod'), nullable=False),
    sa.Column('subtotal', sa.Integer(), nullable=False),
    sa.Column('delivery_fee', sa.Integer(), nullable=False),
    sa.Column('customer_account', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('shopname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['customer_account'], ['user.account'], ),
    sa.ForeignKeyConstraint(['shopname'], ['shop.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_index(op.f('ix_shop_category'), table_name='shop')
    op.drop_table('shop')
    op.drop_table('user')
    # ### end Alembic commands ###
