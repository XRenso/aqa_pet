import os

from dotenv import load_dotenv

# Загружаем переменные из .env (если файл есть). В CI значения приходят
# из переменных окружения и .env не требуется.
load_dotenv()

UI_BASE_URL = os.getenv("UI_BASE_URL", "https://demoqa.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://fakestoreapi.com")
