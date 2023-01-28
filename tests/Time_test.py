import xml.etree.ElementTree as ET
from datetime import datetime

import pytest

from Pages.ConfPage import ConfPage
from Pages.TimePage import TimePage
from api.cam import CamApi


class TestTimeFormat:
    iframe_selector = "#frame_subpage"
    save_button_selector = "#button_devicetime_save"

    @pytest.mark.parametrize("value", ["1", "0", "2"])
    def test_data_format(self, page, value):
        "Проверка смены формата даты"
        timepage = TimePage(page)
        confpage = ConfPage(page)
        iframe = page.frame_locator(self.iframe_selector)
        confpage.system_button.click()  # Нажимаем на кнопку Система
        confpage.time_button.click()
        page.wait_for_load_state("networkidle")
        timepage.data_format.select_option(value=value)
        iframe.locator(self.save_button_selector).click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        date_format_request = CamApi().get_cam_system_info()
        data_from_api = ET.fromstring(date_format_request.content)[0][1].text
        assert data_from_api == value, f"Формат даты: {data_from_api} не совпадает с введеныым {value}"

    @pytest.mark.parametrize("value", ["1", "0"])
    def test_time_format(self, page, value):
        "Проверка смены формата времени"
        timepage = TimePage(page)
        confpage = ConfPage(page)
        iframe = page.frame_locator(self.iframe_selector)
        confpage.system_button.click()
        confpage.time_button.click()
        page.wait_for_load_state("networkidle")
        timepage.time_format.select_option(value=value)
        iframe.locator(self.save_button_selector).click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        time_format_request = CamApi().get_cam_system_info()
        time_from_api = ET.fromstring(time_format_request.content)[0][2].text
        assert time_from_api == value, f"Формат времени: {time_from_api} не совпадает с введеным {value}"

    def test_setup_time(self, page):
        "Проверка сетапа настроек времени устройства"
        iframe = page.frame_locator(self.iframe_selector)
        timepage = TimePage(page)
        confpage = ConfPage(page)
        confpage.system_button.click()
        confpage.time_button.click()
        page.wait_for_load_state("networkidle")
        timepage.time_zone_selector.select_option(value="28")
        timepage.dst_check.set_checked(checked=True, force=True)
        timepage.dst_value.select_option(value="3")
        timepage.dst_start_month.select_option(value="3")
        timepage.dst_start_day.select_option(value="1")
        timepage.dst_start_weekday.select_option(value="2")
        timepage.dst_end_day.select_option(value="4")
        timepage.dst_end_month.select_option(value="4")
        timepage.dst_end_weekday.select_option(value="6")
        timepage.ntp_check.set_checked(checked=True, force=True)
        timepage.input_ntp_adres.fill("time.google.com")
        timepage.input_ntp_server_port.fill("124")
        timepage.input_ntp_interval.fill("2")
        iframe.locator(self.save_button_selector).click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        time_format_request = CamApi().get_cam_time_setting()
        time_zone_from_api = ET.fromstring(time_format_request.content)[0][1].text
        assert time_zone_from_api == "MSK-3"
        time_dst_from_api = ET.fromstring(time_format_request.content)[0][3][0].text
        assert time_dst_from_api == "1"
        summer_time_bias_from_api = ET.fromstring(time_format_request.content)[0][3][1].text
        assert summer_time_bias_from_api == "7200"  # В апи запросе у нас секунды, поэтому и 7200, хотя сетапим 120 минут
        summer_time_begin_month_from_api = ET.fromstring(time_format_request.content)[0][3][2][0].text
        assert summer_time_begin_month_from_api == "3"
        summer_time_begin_week_from_api = ET.fromstring(time_format_request.content)[0][3][2][1].text
        assert summer_time_begin_week_from_api == "1"
        summer_time_begin_day_from_api = ET.fromstring(time_format_request.content)[0][3][2][2].text
        assert summer_time_begin_day_from_api == "2"
        summer_time_end_month_from_api = ET.fromstring(time_format_request.content)[0][3][3][0].text
        assert summer_time_end_month_from_api == "4"
        summer_time_end_week_from_api = ET.fromstring(time_format_request.content)[0][3][3][1].text
        assert summer_time_end_week_from_api == "4"
        summer_time_end_day_from_api = ET.fromstring(time_format_request.content)[0][3][3][2].text
        assert summer_time_end_day_from_api == "6"
        ntp_server_from_api = ET.fromstring(time_format_request.content)[0][4][0].text
        assert ntp_server_from_api == "time.google.com"
        ntp_port_from_api = ET.fromstring(time_format_request.content)[0][4][1].text
        assert ntp_port_from_api == "124"
        ntp_delay_from_api = ET.fromstring(time_format_request.content)[0][4][2].text
        assert ntp_delay_from_api == "2"

    def test_date_picker(self, page):
        "Проверка ручного ввода даты"
        iframe = page.frame_locator(self.iframe_selector)
        timepage = TimePage(page)
        confpage = ConfPage(page)
        confpage.system_button.click()
        confpage.time_button.click()
        page.wait_for_load_state("networkidle")
        timepage.manual_time_check.set_checked(checked=True, force=True)
        timepage.input_manual_date.click(force=True)
        assert iframe.locator("#ui-datepicker-div").is_visible()
        timepage.data_picker_month.select_option(value="0")
        timepage.data_picker_year.select_option(value="2020")
        page.wait_for_timeout(1000)
        timepage.get_calendar_date("23").click(force=True)
        iframe.locator(self.save_button_selector).click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        time_format_request = CamApi().get_cam_time_setting()
        current_date_from_api = ET.fromstring(time_format_request.content)[0][2].text
        date = datetime.strptime(current_date_from_api, "%Y-%m-%dT%H:%M:%S")
        assert date.day == 23
        assert date.year == 2020
        assert date.month == 1

    def test_time_sync_pc(self, page):
        "Проверка синхронизации времени с ПК"
        iframe = page.frame_locator(self.iframe_selector)
        timepage = TimePage(page)
        confpage = ConfPage(page)
        confpage.system_button.click()
        confpage.time_button.click()
        page.wait_for_load_state("networkidle")
        timepage.manual_time_check.set_checked(checked=True, force=True)
        timepage.sync_pc.set_checked(checked=True, force=True)
        iframe.locator(self.save_button_selector).click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        assert timepage.input_manual_date.is_disabled()
        assert iframe.locator("#timer_manual_settime_hour").is_disabled()
        assert iframe.locator("#timer_manual_settime_minute").is_disabled()
        assert iframe.locator("#timer_manual_settime_second").is_disabled()
        time_request = CamApi().get_cam_time_setting()
        time_mode_from_api = ET.fromstring(time_request.content)[0][0].text
        assert time_mode_from_api == "0"
