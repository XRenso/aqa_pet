import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    """Страница Practice Form: /automation-practice-form."""

    PATH = "/automation-practice-form"

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.mobile = page.locator("#userNumber")
        self.gender_male = page.locator("label[for='gender-radio-1']")
        self.hobby_sports = page.locator("label[for='hobbies-checkbox-1']")
        self.submit_btn = page.locator("#submit")

        self.modal_title = page.locator("#example-modal-sizes-title-lg")
        self.modal_table = page.locator(".modal-body table")

    @allure.step("Заполнить обязательные поля формы")
    def fill_form(
        self,
        first: str,
        last: str,
        email: str,
        mobile: str,
        gender: bool = True,
        sports: bool = True,
    ) -> "PracticeFormPage":
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        if gender:
            self._scroll_and_click(self.gender_male)
        self.mobile.fill(mobile)
        if sports:
            self._scroll_and_click(self.hobby_sports)
        return self

    @allure.step("Отправить форму")
    def submit(self) -> "PracticeFormPage":
        self._js_click(self.submit_btn)
        return self

    @allure.step("Дождаться модального окна с результатом")
    def get_modal_title(self) -> str:
        expect(self.modal_title).to_be_visible()
        return self.modal_title.inner_text()

    @allure.step("Получить текст таблицы результата")
    def get_modal_table_text(self) -> str:
        return self.modal_table.inner_text()
