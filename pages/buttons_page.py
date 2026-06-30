import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class ButtonsPage(BasePage):
    """Страница Buttons: /buttons."""

    PATH = "/buttons"

    def __init__(self, page: Page):
        super().__init__(page)
        self.double_click_btn = page.locator("#doubleClickBtn")
        self.right_click_btn = page.locator("#rightClickBtn")
        self.double_click_msg = page.locator("#doubleClickMessage")
        self.right_click_msg = page.locator("#rightClickMessage")

    @allure.step("Двойной клик по кнопке")
    def double_click(self) -> "ButtonsPage":
        self.double_click_btn.scroll_into_view_if_needed()
        self.double_click_btn.dblclick()
        return self

    @allure.step("Правый клик по кнопке")
    def right_click(self) -> "ButtonsPage":
        self.right_click_btn.scroll_into_view_if_needed()
        self.right_click_btn.click(button="right")
        return self

    @allure.step("Прочитать сообщение двойного клика")
    def double_click_message(self) -> str:
        return self.double_click_msg.inner_text()

    @allure.step("Прочитать сообщение правого клика")
    def right_click_message(self) -> str:
        return self.right_click_msg.inner_text()
