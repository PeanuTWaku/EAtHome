"""Add product and record

Revision ID: 633f772c0430
Revises: 836abce14d89
Create Date: 2022-11-11 00:50:51.957452

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '633f772c0430'
down_revision = '836abce14d89'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('traderecord',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('action', sa.Enum('RECHARGE', 'ORDER', 'CANCEL', name='tradeaction'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('initiator', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('recipient', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_account', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['user_account'], ['user.account'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('image_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('shopname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['shopname'], ['shop.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderproductlink',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderproductlink')
    op.drop_table('product')
    op.drop_table('traderecord')
    # ### end Alembic commands ###