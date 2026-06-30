# aqa_pet

pytest · Playwright (UI) · requests (API) · Allure

```
pages/        # Page Object
clients/      # API-клиент
tests/ui/     # UI
tests/api/    # API
config.py     # .env
```

## Установка

```bash
cp .env.example .env
pip install -r requirements.txt
playwright install
```

## Запуск

```bash
pytest                # ui + api
pytest -m ui          # ui
pytest -m api         # api
```

## Отчёт

```bash
allure serve allure-results
```
