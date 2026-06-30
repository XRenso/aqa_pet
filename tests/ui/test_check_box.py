import allure
import pytest

from pages.check_box_page import CheckBoxPage


@allure.feature("Check Box")
@allure.title("Раскрытие дерева и выбор узла Home отмечает все вложенные пункты")
@pytest.mark.ui
def test_check_box_select_home(page):
    check_box = CheckBoxPage(page).open()

    check_box.expand_tree()
    check_box.check_home()

    result = check_box.get_result()

    with allure.step("Проверить, что в результате есть ключевые пункты"):
        assert "home" in result
        assert "desktop" in result
        assert "documents" in result
        assert "downloads" in result
