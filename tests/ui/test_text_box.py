import allure
import pytest

from pages.text_box_page import TextBoxPage


@allure.feature("Text Box")
@allure.title("Заполнение формы Text Box отображает введённые данные в выводе")
@pytest.mark.ui
def test_text_box_submit(page):
    text_box = TextBoxPage(page).open()

    text_box.fill_form(
        name="Ivan Petrov",
        email="ivan.petrov@example.com",
        current="Lenina 1, Moscow",
        permanent="Pushkina 2, Moscow",
    ).submit()

    output = text_box.get_output()

    with allure.step("Проверить, что вывод соответствует введённым данным"):
        assert "Ivan Petrov" in output["name"]
        assert "ivan.petrov@example.com" in output["email"]
        assert "Lenina 1, Moscow" in output["current"]
        assert "Pushkina 2, Moscow" in output["permanent"]
