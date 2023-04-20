import sqlalchemy, datetime
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, JSON, ForeignKey, Table, Column

metadata = MetaData()

roles = Table(
    "user_roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("role_name", String, nullable=False),
    Column("role_permissions", JSON)
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id"))
)

engine = sqlalchemy.create_engine()
metadata.cr
