import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Union
import uvicorn
import logging
from pathlib import Path
import datetime
import crud
app = FastAPI()

logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")


def data_transformation(data: list):
    """Функция преобразующая список строк из exel файла
        в удобный вид для работы с данными.

    Params:
        data: list

    """
    day = 1
    for dat in data:
        date = datetime.date(2023, 2, day)
        dic1 = {
            "company": dat[1],
            "kind": "fact",
            "type": "Qliq",
            "data1": dat[2],
            "data2": dat[3],
            "total": dat[2] + dat[3],
            "date": date
        }
        dic2 = {
            "company": dat[1],
            "kind": "fact",
            "type": "Qoil",
            "data1": dat[4],
            "data2": dat[5],
            "total": dat[4] + dat[5],
            "date": date
        }
        dic3 = {
            "company": dat[1],
            "kind": "forecast",
            "type": "Qliq",
            "data1": dat[6],
            "data2": dat[7],
            "total": dat[6] + dat[7],
            "date": date
        }
        dic4 = {
            "company": dat[1],
            "kind": "forecast",
            "type": "Qoil",
            "data1": dat[8],
            "data2": dat[9],
            "total": dat[8] + dat[9],
            "date": date
        }
        day += 1
        array_row = [dic1, dic2, dic3, dic4]
        for row in array_row:
            crud.insert_row(row)
    return 'ok'


@app.post("/api/v1/parser_file")
def upload_file(sheet: Union[str, None] = None, row: Union[int, None] = None, file: UploadFile = File(description="Download excel file for parsing")):
    """Метод POST, загрузки файла exel для парсинга.

        Params:\n
            sheet: название листа файла с котрого парсить данные.\n
            row: индекс строки с которой начинается парсинг данных.
    """
    valid_file_extensions = ["xlsx", "xls"]
    if file.filename.split(".")[1] not in valid_file_extensions:
        raise HTTPException(status_code=404, detail="Недопустимый тип файла")
    if sheet is None:
        sheet = 'Sheet1'
    try:
        df = pd.read_excel(file.file.read(), sheet_name=sheet)
    except ValueError:
        raise HTTPException(
            status_code=404, detail="Некорректное название листа")
    if row is None:
        row = 2
    if row < 2:
        raise HTTPException(
            status_code=404, detail="Выбрано неккоректное значение строки с которой будет производиться запись")
    array_insert = df.values.tolist()[row:]
    if len(array_insert) == 0:
        raise HTTPException(
            status_code=404, detail="Выбрано неккоректное значение строки с которой будет производиться запись")
    # Замена пустых значений в dataframe на ноль.
    df = df.fillna(0)
    # Запись в БД новых данных, расчет тотала по дате.
    data_transformation(array_insert)

    return {'status': '1', 'data': "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")

