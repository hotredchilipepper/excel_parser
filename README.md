# excel_parser

1. Клонировать репозиторий
2. Создать вирутальное окружение командой:
    python -m venv name
3. Активировать виртуальное окружение командой:
    -Для Wondows
        .\venv\Scripts\activate
    -Для Linux
        source venv/bin/activate

4. Обновить зависимости
    pip install --upgrade pip

5. Установить зависимости небоходимые для работы программы
    pip install -r requirements.txt

6. Запускаем приложение командой:
    uvicorn main:app

7. Переходим в интерфейс docs по адресу:
    http://127.0.0.1:8000/docs

8. После заверешения использования программы
-остановить работу CTRL+C
-отключить виртуальное окружение deactivate