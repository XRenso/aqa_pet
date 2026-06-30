import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """Страница Text Box: /text-box."""

    PATH = "/text-box"

    def __init__(self, page: Page):
        super().__init__(page)
        self.full_name = page.get_by_placeholder("Full Name")
        self.email = page.get_by_placeholder("name@example.com")
        self.current_address = page.get_by_placeholder("Current Address")
        self.permanent_address = page.locator("#permanentAddress")
        self.submit_btn = page.locator("#submit")

        self.output_name = page.locator("#output #name")
        self.output_email = page.locator("#output #email")
        self.output_current_address = page.locator("#output #currentAddress")
        self.output_permanent_address = page.locator("#output #permanentAddress")

    @allure.step("Заполнить форму Text Box")
    def fill_form(
        self, name: str, email: str, current: str, permanent: str
    ) -> "TextBoxPage":
        self.full_name.fill(name)
        self.email.fill(email)
        self.current_address.fill(current)
        self.permanent_address.fill(permanent)
        return self

    @allure.step("Отправить форму")
    def submit(self) -> "TextBoxPage":
        self._js_click(self.submit_btn)
        return self

    @allure.step("Получить текст вывода")
    def get_output(self) -> dict:
        return {
            "name": self.output_name.inner_text(),
            "email": self.output_email.inner_text(),
            "current": self.output_current_address.inner_text(),
            "permanent": self.output_permanent_address.inner_text(),
        }
