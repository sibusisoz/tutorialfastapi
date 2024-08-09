"""create  tables

Revision ID: 30db8f4269d2
Revises: 
Create Date: 2024-08-09 01:46:33.769131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
  
# revision identifiers, used by Alembic. 
revision: str = '30db8f4269d2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table("tposts",sa.Column("id",sa.Integer(),nullable=False,primary_key=True)
                            ,sa.Column("title",sa.String(),nullable=False) 
                            ,sa.Column("content",sa.String(),nullable=False)
                            ,sa.Column("published",sa.Boolean(),server_default=("TRUE"),nullable=False)
                            ,sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False)
                            ,sa.Column("owner_id",sa.Integer(),nullable=False)
                            )
    
    
    op.create_table("tusers",sa.Column("id",sa.Integer(),nullable=False)
                            ,sa.Column("email",sa.String(),nullable=False)
                            ,sa.Column("password",sa.String(),nullable=False)
                            ,sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False)
                            ,sa.PrimaryKeyConstraint("id")
                            ,sa.UniqueConstraint("email")
                            )
    op.create_table('tvotes',sa.Column('user_id', sa.Integer(), nullable=False)
                            ,sa.Column('post_id', sa.Integer(), nullable=False) 
                            )  
    pass

def downgrade() -> None: 
    pass   