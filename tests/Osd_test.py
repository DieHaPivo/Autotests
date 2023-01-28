import xml.etree.ElementTree as ET

from Pages.ConfPage import ConfPage
from Pages.OsdPage import OsdPage
from api.cam import CamApi


class TestOsd:

    def test_osd_enable(self, page):
        conf_page = ConfPage(page)
        osd_page = OsdPage(page)
        conf_page.av_button.click()
        conf_page.osd_button.click()
        page.wait_for_timeout(1000)
        osd_page.custom_osd_checkbox.set_checked(checked=True, force=True)
        osd_page.device_name_checkbox.set_checked(checked=True, force=True)
        osd_page.device_time_checkbox.set_checked(checked=True, force=True)
        osd_page.save_button.click(force=True)
        osd_request = CamApi().get_osd_info()
        time_osd_from_api = ET.fromstring(osd_request.content)[0][0][0][0].text
        assert time_osd_from_api == "1"
        name_osd_from_api = ET.fromstring(osd_request.content)[0][1][0][0].text
        assert name_osd_from_api == "1"
        custom_osd_from_api = ET.fromstring(osd_request.content)[0][3][0][0].text
        assert custom_osd_from_api == "1"

    def test_osd_disable(self, page):
        conf_page = ConfPage(page)
        osd_page = OsdPage(page)
        conf_page.av_button.click()
        conf_page.osd_button.click()
        page.wait_for_timeout(1000)
        osd_page.custom_osd_checkbox.set_checked(checked=False, force=True)
        osd_page.device_name_checkbox.set_checked(checked=False, force=True)
        osd_page.device_time_checkbox.set_checked(checked=False, force=True)
        osd_page.save_button.click(force=True)
        osd_request = CamApi().get_osd_info()
        time_osd_from_api = ET.fromstring(osd_request.content)[0][0][0][0].text
        assert time_osd_from_api == "0"
        name_osd_from_api = ET.fromstring(osd_request.content)[0][1][0][0].text
        assert name_osd_from_api == "0"
        custom_osd_from_api = ET.fromstring(osd_request.content)[0][3][0][0].text
        assert custom_osd_from_api == "0"