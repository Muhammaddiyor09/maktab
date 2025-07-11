"""s

Revision ID: 61606eee031b
Revises: 557b50b5e8a3
Create Date: 2025-06-24 14:41:38.350777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61606eee031b'
down_revision: Union[str, Sequence[str], None] = '557b50b5e8a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('science', sa.String(length=40), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'science')
    # ### end Alembic commands ###
