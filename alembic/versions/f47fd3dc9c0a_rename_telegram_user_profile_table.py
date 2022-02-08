"""rename_telegram_user_profile_table

Revision ID: f47fd3dc9c0a
Revises: 
Create Date: 2022-02-08 17:30:47.570389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f47fd3dc9c0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('telegram_user_profile', 'telegram_profile')


def downgrade():
    op.rename_table('telegram_profile', 'telegram_user_profile')

