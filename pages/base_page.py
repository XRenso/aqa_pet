import allure
from playwright.sync_api import Locator, Page, expect

from config import UI_BASE_URL


class BasePage:
    """Базовый класс для всех Page Object."""

    BASE_URL = UI_BASE_URL
    PATH = ""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу")
    def open(self) -> "BasePage":
        self.page.goto(f"{self.BASE_URL}{self.PATH}", wait_until="domcontentloaded")
        return self

    def _scroll_and_click(self, locator: Locator) -> None:
        locator.scroll_into_view_if_needed()
        expect(locator).to_be_visible()
        locator.click()

    def _js_click(self, locator: Locator) -> None:
        locator.scroll_into_view_if_needed()
        expect(locator).to_be_visible()
        locator.evaluate("el => el.click()")
