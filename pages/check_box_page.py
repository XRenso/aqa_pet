import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    """Страница Check Box: /checkbox (виджет на базе rc-tree)."""

    PATH = "/checkbox"

    def __init__(self, page: Page):
        super().__init__(page)
        self.home_switcher = page.locator(".rc-tree-switcher").first
        self.home_checkbox = page.get_by_label("Select Home")
        self.result = page.locator("#result")

    @allure.step("Развернуть дерево (узел Home)")
    def expand_tree(self) -> "CheckBoxPage":
        self._scroll_and_click(self.home_switcher)
        return self

    @allure.step("Отметить узел Home")
    def check_home(self) -> "CheckBoxPage":
        self._scroll_and_click(self.home_checkbox)
        return self

    @allure.step("Получить список выбранных пунктов")
    def get_result(self) -> str:
        expect(self.result).to_be_visible()
        return self.result.inner_text()
