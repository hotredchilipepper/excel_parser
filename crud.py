from sqlalchemy import (
    and_,
    or_,
)
from models import *


def insert_row(row: dict) -> str:
    """Функция для добавления новой строки в БД

    Params:
        row: dict

    """
    ins = data_table.insert().values(
        company=row["company"],
        kind=row["kind"],
        type=row["type"],
        data1=row["data1"],
        data2=row["data2"],
        total=row["total"],
        date=row["date"]
    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
    return "ok"
