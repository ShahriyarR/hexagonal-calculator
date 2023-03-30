"""empty message

Revision ID: 0964880e1c92
Revises: 
Create Date: 2023-03-30 19:37:00.986298

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0964880e1c92"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "calculation",
        sa.Column(
            "id",
            sa.BigInteger().with_variant(sa.Integer(), "sqlite"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("uuid", sa.String(), nullable=False),
        sa.Column("left", sa.DECIMAL(), nullable=False),
        sa.Column("right", sa.DECIMAL(), nullable=False),
        sa.Column("action", sa.String(), nullable=False),
        sa.Column("result", sa.DECIMAL(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("left", "right", "action", name="u_lra_x_1"),
        sa.UniqueConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("calculation")
    # ### end Alembic commands ###
