import xml.etree.ElementTree as ET

import pytest

from Pages.ConfPage import ConfPage
from api.cam import CamApi


class TestName:
    save_button_selector = "#button_device_name_save"  # Переменная с локатором кнопки Сохранить
    name_input_selector = ".cls_subpage_content_input"  # Переменная с локатором поля ввода имени устройства
    iframe_selector = "#frame_subpage"  # Переменная с локатором подстраницы камеры

    @pytest.mark.parametrize("name", ["TR-BUBAYUBA", "£@!$%^&*()(!*&&%!£", "1231234667675567565"])  # Тестовые параметры
    def test_rename(self, page, name):
        "Проверка смены имени камеры"
        confpage = ConfPage(page)  # подгружаем локаторы страницы Настройки
        confpage.system_button.click()  # Нажимаем на кнопку Система
        confpage.general_button.click()  # Нажимаем на кнопку Основные
        iframe = page.frame_locator(self.iframe_selector)  # Переменная подстраницы настроек камеры
        iframe.locator(self.name_input_selector).fill(name)  # Вводим тестовые данные
        iframe.locator(self.save_button_selector).click(
            force=True)  # Нажимаем сохранить(форс потому что HTTP элемент перекрывает кнопку)
        assert page.wait_for_selector(
            "#div_tips_dialog_content").is_visible()  # Ждем выподающюю плашку Настройки приняты
        name_request = CamApi().get_cam_info()  # Используем функцию получения АПИ запроса
        name_from_api = ET.fromstring(name_request.content)[0][0].text  # Получаем из апи запроса, поле Имя камеры
        assert name_from_api == name, f"Имя камеры: {name_from_api} не совпадает с введенным {name}"  # Сравниваем Имя камеры с апи запроса, с тестовым параметром
