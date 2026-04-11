# data_handler.py
import json
from pathlib import Path

# Константа с путем к файлу
DATA_FILE = Path("finance.json")

def load_data() -> dict:
    """Загружает данные из JSON-файла. Если файла нет - возвращает пустую структуру."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Возвращаем базовую структуру данных
        return {"operations": []}


def save_data(data: dict) -> None:
    """Сохраняет данные в JSON-файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_data_file_path() -> Path:
    """Возвращает путь к файлу данных (для удобства)"""
    return DATA_FILE
