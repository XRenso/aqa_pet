import allure
import pytest

from pages.practice_form_page import PracticeFormPage


@allure.feature("Practice Form")
@allure.title("Заполнение и отправка формы показывает модалку с результатом")
@pytest.mark.ui
def test_practice_form_submit(page):
    form = PracticeFormPage(page).open()

    form.fill_form(
        first="Ivan",
        last="Petrov",
        email="ivan.petrov@example.com",
        mobile="9991234567",
    ).submit()

    with allure.step("Проверить заголовок и содержимое модального окна"):
        assert form.get_modal_title() == "Thanks for submitting the form"
        table_text = form.get_modal_table_text()
        assert "Ivan Petrov" in table_text
        assert "ivan.petrov@example.com" in table_text
        assert "9991234567" in table_text
