import allure
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class WebTablesPage(BasePage):
    """Страница Web Tables: /webtables."""

    PATH = "/webtables"

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_new_record = page.locator("#addNewRecordButton")
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.age = page.locator("#age")
        self.salary = page.locator("#salary")
        self.department = page.locator("#department")
        self.submit_btn = page.locator("#submit")

    @allure.step("Открыть форму добавления записи")
    def open_add_form(self) -> "WebTablesPage":
        self._scroll_and_click(self.add_new_record)
        return self

    @allure.step("Заполнить и сохранить запись")
    def add_record(
        self, first: str, last: str, email: str, age: str, salary: str, department: str
    ) -> "WebTablesPage":
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        self.age.fill(age)
        self.salary.fill(salary)
        self.department.fill(department)
        self._js_click(self.submit_btn)
        return self

    def row_by_text(self, text: str) -> Locator:
        return self.page.get_by_role("row").filter(has_text=text)
