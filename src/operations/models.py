from sqlalchemy import TIMESTAMP, Column, Integer, MetaData, String, Table, ForeignKey
from src.auth.models import user

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("task_name", String, nullable=False),
    Column("task_description", String, nullable=True),
    Column("task_start", TIMESTAMP, nullable=False),
    Column("task_end", TIMESTAMP, nullable=False),
    Column("task_create", TIMESTAMP, nullable=False),
    Column("task_author", Integer, ForeignKey(user.c.id))
)
