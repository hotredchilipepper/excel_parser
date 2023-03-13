# Описание моделей/таблиц БД

from sqlalchemy import MetaData
from database import engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Date,
)

meta = MetaData()

data_table = Table(
    "data_table", meta,
    Column("id", Integer, primary_key=True),
    Column("company", String(64)),
    Column("kind", String(32)),
    Column("type", String(32)),
    Column("data1", Integer),
    Column("data2", Integer),
    Column("total", Integer),
    Column("date", Date)
)

meta.create_all(engine)
