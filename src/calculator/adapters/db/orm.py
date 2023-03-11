from sqlalchemy import (
    DECIMAL,
    BigInteger,
    Column,
    DateTime,
    MetaData,
    String,
    Table,
    UniqueConstraint,
)
from sqlalchemy.orm import registry

from calculator.domain.model import model

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

calculation = Table(
    "calculation",
    mapper_registry.metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("uuid", String, unique=True, nullable=False),
    Column("left", DECIMAL, nullable=False),
    Column("right", DECIMAL, nullable=False),
    Column("action", String, nullable=False),
    Column("result", DECIMAL, nullable=False),
    Column("created_at", DateTime, nullable=False),
    Column("updated_at", DateTime, nullable=False),
    UniqueConstraint("left", "right", "action", name="u_lra_x_1"),
)


def start_mappers():
    mapper_registry.map_imperatively(model.Calculation, calculation)
