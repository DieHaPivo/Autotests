import xml.etree.ElementTree as ET

from Pages.ConfPage import ConfPage
from Pages.NetworkPage import SmtpPage, CloudPage
from api.cam import CamApi


class TestNetwork:

    def test_smtp_gmail_preset(self, page):
        conf_page = ConfPage(page)
        smtp_page = SmtpPage(page)
        conf_page.network_button.click()
        conf_page.smtp_button.click()
        page.wait_for_load_state("networkidle")
        smtp_page.gmail_preset_button.click(force=True)
        assert smtp_page.iframe.locator("#input_smtp_server_address").input_value() == "smtp.gmail.com"
        assert smtp_page.iframe.locator("#select_smtp_ssl_enable").input_value() == "1"
        smtp_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        smtp_request = CamApi().get_cam_smtp_info()
        smtp_host_from_api = ET.fromstring(smtp_request.content)[0][0].text
        assert smtp_host_from_api == "smtp.gmail.com"
        smtp_port_from_api = ET.fromstring(smtp_request.content)[0][1].text
        assert smtp_port_from_api == '465'
        smtp_ssl_from_api = ET.fromstring(smtp_request.content)[0][4].text
        assert smtp_ssl_from_api == '1'

    def test_smtp_outlook_preset(self, page):
        conf_page = ConfPage(page)
        smtp_page = SmtpPage(page)
        conf_page.network_button.click()
        conf_page.smtp_button.click()
        page.wait_for_load_state("networkidle")
        smtp_page.outlook_preset_button.click(force=True)
        assert smtp_page.iframe.locator("#input_smtp_server_address").input_value() == "smtp.live.com"
        assert smtp_page.iframe.locator("#select_smtp_ssl_enable").input_value() == "1"
        smtp_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        smtp_request = CamApi().get_cam_smtp_info()
        smtp_host_from_api = ET.fromstring(smtp_request.content)[0][0].text
        assert smtp_host_from_api == "smtp.live.com"
        smtp_port_from_api = ET.fromstring(smtp_request.content)[0][1].text
        assert smtp_port_from_api == '465'
        smtp_ssl_from_api = ET.fromstring(smtp_request.content)[0][4].text
        assert smtp_ssl_from_api == '1'

    def test_smtp_yahoo_preset(self, page):
        conf_page = ConfPage(page)
        smtp_page = SmtpPage(page)
        conf_page.network_button.click()
        conf_page.smtp_button.click()
        page.wait_for_load_state("networkidle")
        smtp_page.yahoo_preset_button.click(force=True)
        assert smtp_page.iframe.locator("#input_smtp_server_address").input_value() == "smtp.mail.yahoo.com"
        assert smtp_page.iframe.locator("#select_smtp_ssl_enable").input_value() == "1"
        smtp_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        smtp_request = CamApi().get_cam_smtp_info()
        smtp_host_from_api = ET.fromstring(smtp_request.content)[0][0].text
        assert smtp_host_from_api == "smtp.mail.yahoo.com"
        smtp_port_from_api = ET.fromstring(smtp_request.content)[0][1].text
        assert smtp_port_from_api == '465'
        smtp_ssl_from_api = ET.fromstring(smtp_request.content)[0][4].text
        assert smtp_ssl_from_api == '1'

    def test_smtp_auth(self, page):
        conf_page = ConfPage(page)
        smtp_page = SmtpPage(page)
        conf_page.network_button.click()
        conf_page.smtp_button.click()
        page.wait_for_load_state("networkidle")
        smtp_page.username_input.fill("test")
        smtp_page.password_input.fill("12345")
        smtp_page.device_name_input.fill("tr-1337")
        smtp_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        smtp_request = CamApi().get_cam_smtp_info()
        smtp_username_from_api = ET.fromstring(smtp_request.content)[0][2].text
        assert smtp_username_from_api == "test"
        smtp_password_from_api = ET.fromstring(smtp_request.content)[0][3].text
        assert smtp_password_from_api == "12345"
        smtp_device_name_from_api = ET.fromstring(smtp_request.content)[0][5].text
        assert smtp_device_name_from_api == "tr-1337"

    def test_recipient_fill(self, page):
        conf_page = ConfPage(page)
        smtp_page = SmtpPage(page)
        conf_page.network_button.click()
        conf_page.smtp_button.click()
        page.wait_for_load_state("networkidle")
        smtp_page.recipient_one_input.fill("test@test.test")
        smtp_page.recipient_two_input.fill("test2@mli.ru")
        smtp_page.recipient_three_input.fill("test3@buba.yuba")
        smtp_page.recipient_four_input.fill("test4@gachi.cum")
        smtp_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        smtp_request = CamApi().get_cam_smtp_info()
        smtp_recipient_one_from_api = ET.fromstring(smtp_request.content)[0][7].text
        assert smtp_recipient_one_from_api == "test@test.test"
        smtp_recipient_two_from_api = ET.fromstring(smtp_request.content)[0][8].text
        assert smtp_recipient_two_from_api == "test2@mli.ru"
        smtp_recipient_three_from_api = ET.fromstring(smtp_request.content)[0][9].text
        assert smtp_recipient_three_from_api == 'test3@buba.yuba'
        smtp_recipient_four_from_api = ET.fromstring(smtp_request.content)[0][10].text
        assert smtp_recipient_four_from_api == "test4@gachi.cum"

    def test_cloud_plugin(self, page):
        conf_page = ConfPage(page)
        cloud_page = CloudPage(page)
        conf_page.network_button.click()
        conf_page.cloud_button.click()
        page.wait_for_load_state("networkidle")
        cloud_page.plugin_checkbox.set_checked(checked=True, force=True)
        cloud_page.idle_timeout_input.fill("12345")
        cloud_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        cloud_plugin_request = CamApi().get_cloud_plugin_info()
        cloud_plugin_status_from_api = ET.fromstring(cloud_plugin_request.content)[0][0].text
        assert cloud_plugin_status_from_api == "1"
        cloud_plugin_timeout_from_api = ET.fromstring(cloud_plugin_request.content)[0][1].text
        assert cloud_plugin_timeout_from_api == "12345"
