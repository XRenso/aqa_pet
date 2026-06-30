import allure
import pytest
from playwright.sync_api import expect

from pages.web_tables_page import WebTablesPage


@allure.feature("Web Tables")
@allure.title("Добавление новой записи отображает её в таблице")
@pytest.mark.ui
def test_web_tables_add_record(page):
    web_tables = WebTablesPage(page).open()

    email = "alice.smith@example.com"
    web_tables.open_add_form()
    web_tables.add_record(
        first="Alice",
        last="Smith",
        email=email,
        age="30",
        salary="50000",
        department="QA",
    )

    with allure.step("Проверить, что строка с новой записью появилась в таблице"):
        row = web_tables.row_by_text(email)
        expect(row).to_be_visible()
        expect(row).to_contain_text("Alice")
        expect(row).to_contain_text("Smith")
        expect(row).to_contain_text("QA")
