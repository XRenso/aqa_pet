import allure
import pytest

from pages.buttons_page import ButtonsPage


@allure.feature("Buttons")
@allure.title("Double click и right click показывают соответствующие сообщения")
@pytest.mark.ui
def test_buttons_clicks(page):
    buttons = ButtonsPage(page).open()

    buttons.double_click()
    buttons.right_click()

    with allure.step("Проверить сообщения double и right click"):
        assert buttons.double_click_message() == "You have done a double click"
        assert buttons.right_click_message() == "You have done a right click"
