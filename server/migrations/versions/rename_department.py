"""rename department

Revision ID: rename_department
Revises: 3a2d1137b1ad
Create Date: 2024-06-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'rename_department'
down_revision = '3a2d1137b1ad'
branch_labels = None
depends_on = None

def upgrade():
    # Rename table 'department' to 'departments'
    op.rename_table('department', 'departments')

def downgrade():
    # Rename table 'departments' back to 'department'
    op.rename_table('departments', 'department')
