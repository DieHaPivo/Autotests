import xml.etree.ElementTree as ET

from Pages.ConfPage import ConfPage
from Pages.VideoPage import VideoPage
from api.cam import CamApi


class TestVideo:

    def test_hdr_disabled(self, page):
        conf_page = ConfPage(page)
        video_page = VideoPage(page)
        conf_page.av_button.click()
        conf_page.video_button.click()
        video_page.hdr_checkbox.set_checked(checked=False, force=True)
        video_page.workmode_save_button.click(force=True)
        video_page.reboot_accept_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        page.wait_for_timeout(5000)
        work_mode_request = CamApi().get_video_work_info()
        work_mode_from_api = ET.fromstring(work_mode_request.content)[0][0].text
        assert work_mode_from_api == "0"

    def test_hdr_checkbox(self, page):
        conf_page = ConfPage(page)
        video_page = VideoPage(page)
        conf_page.av_button.click()
        conf_page.video_button.click()
        video_page.hdr_checkbox.set_checked(checked=True, force=True)
        video_page.workmode_save_button.click(force=True)
        video_page.reboot_accept_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        page.wait_for_timeout(5000)
        work_mode_request = CamApi().get_video_work_info()
        work_mode_from_api = ET.fromstring(work_mode_request.content)[0][0].text
        assert work_mode_from_api == "1"

    def test_main_video_params(self, page):
        conf_page = ConfPage(page)
        video_page = VideoPage(page)
        conf_page.av_button.click()
        conf_page.video_button.click()
        video_page.video_subpage.click(force=True)
        page.wait_for_load_state("networkidle")
        video_page.main_profile_selector.select_option(value="High Profile")
        video_page.main_bitrate_type_selector.select_option(value="VBR")
        video_page.main_birate_input.fill("1234")
        video_page.main_encode_quality_selector.select_option(value="6")
        video_page.main_gop_selector.select_option(value="22")
        video_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        video_info_request = CamApi().get_main_video_info()
        main_profile_from_api = ET.fromstring(video_info_request.content)[0][8].text
        assert main_profile_from_api == "2"
        main_bitrate_from_api = ET.fromstring(video_info_request.content)[0][6].text
        assert main_bitrate_from_api == "1234"
        main_bitrate_type_from_api = ET.fromstring(video_info_request.content)[0][4].text
        assert main_bitrate_type_from_api == "0"
        main_encode_from_api = ET.fromstring(video_info_request.content)[0][7].text
        assert main_encode_from_api == "6"
        main_gop_from_api = ET.fromstring(video_info_request.content)[0][5].text
        assert main_gop_from_api == "22"

    def test_main_bitrate_type(self, page):
        conf_page = ConfPage(page)
        video_page = VideoPage(page)
        conf_page.av_button.click()
        conf_page.video_button.click()
        video_page.video_subpage.click(force=True)
        page.wait_for_load_state("networkidle")
        video_page.main_bitrate_type_selector.select_option(value="CBR")
        assert video_page.main_encode_quality_selector.is_disabled()
        video_page.save_button.click(force=True)
        video_info_request = CamApi().get_main_video_info()
        main_bitrate_type_from_api = ET.fromstring(video_info_request.content)[0][4].text
        assert main_bitrate_type_from_api == "1"

    def test_sub_video_params(self, page):
        conf_page = ConfPage(page)
        video_page = VideoPage(page)
        conf_page.av_button.click()
        conf_page.video_button.click()
        video_page.video_subpage.click(force=True)
        page.wait_for_load_state("networkidle")
        video_page.sub_profile_selector.select_option(value="High Profile")
        video_page.sub_bitrate_type_selector.select_option(value="VBR")
        video_page.sub_bitrate_input.fill("123")
        video_page.sub_encode_quality_selector.select_option(value="6")
        video_page.sub_gop_selector.select_option(value="22")
        video_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        video_info_request = CamApi().get_sub_video_info()
        sub_profile_from_api = ET.fromstring(video_info_request.content)[0][8].text
        assert sub_profile_from_api == "2"
        sub_bitrate_from_api = ET.fromstring(video_info_request.content)[0][6].text
        assert sub_bitrate_from_api == "123"
        sub_bitrate_type_from_api = ET.fromstring(video_info_request.content)[0][4].text
        assert sub_bitrate_type_from_api == "0"
        sub_encode_from_api = ET.fromstring(video_info_request.content)[0][7].text
        assert sub_encode_from_api == "6"
        sub_gop_from_api = ET.fromstring(video_info_request.content)[0][5].text
        assert sub_gop_from_api == "22"

    def test_sub_bitrate_type(self, page):
        conf_page = ConfPage(page)
        video_page = VideoPage(page)
        conf_page.av_button.click()
        conf_page.video_button.click()
        video_page.video_subpage.click(force=True)
        page.wait_for_load_state("networkidle")
        video_page.sub_bitrate_type_selector.select_option(value="CBR")
        assert video_page.sub_encode_quality_selector.is_disabled()
        video_page.save_button.click(force=True)
        video_info_request = CamApi().get_sub_video_info()
        main_bitrate_type_from_api = ET.fromstring(video_info_request.content)[0][4].text
        assert main_bitrate_type_from_api == "1"