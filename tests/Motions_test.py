import xml.etree.ElementTree as ET

from Pages.ConfPage import ConfPage
from Pages.MotionPage import MotionPage
from api.cam import CamApi


class TestMotions:

    def test_motion_detector_zone_sliders(self,page):
        conf_page = ConfPage(page)
        motion_page = MotionPage(page)
        conf_page.ivent_button.click()
        conf_page.motion_detector_button.click()
        page.wait_for_timeout(2500)
        motion_page.motion_enable_checkbox.set_checked(checked=True, force=True)
        sensivity_value_max = "10"
        sensivity_value_min = "1"
        threshold_value_max = "100"
        threshold_value_min = "0"
        motion_page.motion_sensivity_slider.click(force=True)
        while motion_page.motion_sensivity_value.inner_text() != sensivity_value_max:
            motion_page.motion_sensivity_slider.press("ArrowRight")
        assert motion_page.motion_sensivity_value.inner_text() == sensivity_value_max
        motion_page.motion_sensivity_slider.click(force=True)
        while motion_page.motion_sensivity_value.inner_text() != sensivity_value_min:
            motion_page.motion_sensivity_slider.press("ArrowLeft")
        assert motion_page.motion_sensivity_value.inner_text() == sensivity_value_min
        motion_page.motion_threshold_slider.click(force=True)
        while motion_page.motion_threshold_value.inner_text() != threshold_value_max:
            motion_page.motion_threshold_slider.press("ArrowRight")
        assert motion_page.motion_threshold_value.inner_text() == threshold_value_max
        while motion_page.motion_threshold_value.inner_text() != threshold_value_min:
            motion_page.motion_threshold_slider.press("ArrowLeft")
        assert motion_page.motion_threshold_value.inner_text() == threshold_value_min

    def test_motion_schedule_all_days_setting(self,page):
        conf_page = ConfPage(page)
        motion_page = MotionPage(page)
        conf_page.ivent_button.click()
        conf_page.motion_detector_button.click()
        page.wait_for_timeout(2500)
        motion_page.motion_schedule_subpage.click(force=True)
        motion_page.motion_mintime_declare_input.fill("200")
        motion_page.motion_schedule_alldays_radio.click(force=True)
        motion_page.schedule_save_button.click(force=True)
        motion_info_request = CamApi().get_motion_detector_info()
        motion_active_from_api = ET.fromstring(motion_info_request.content)[0][0].text
        assert motion_active_from_api == "1"
        motion_timeout_from_api = ET.fromstring(motion_info_request.content)[0][1].text
        assert motion_timeout_from_api == "200"

    def test_motion_schedule_setting(self,page):
        conf_page = ConfPage(page)
        motion_page = MotionPage(page)
        conf_page.ivent_button.click()
        conf_page.motion_detector_button.click()
        page.wait_for_timeout(2500)
        motion_page.motion_schedule_subpage.click(force=True)
        motion_page.motion_mintime_declare_input.fill("100")
        motion_page.motion_schedule_radio.click(force=True)
        motion_page.schedule_save_button.click(force=True)
        motion_info_request = CamApi().get_motion_detector_info()
        motion_active_from_api = ET.fromstring(motion_info_request.content)[0][0].text
        assert motion_active_from_api == "2"
        motion_timeout_from_api = ET.fromstring(motion_info_request.content)[0][1].text
        assert motion_timeout_from_api == "100"

    def test_motion_schedule_disable(self,page):
        conf_page = ConfPage(page)
        motion_page = MotionPage(page)
        conf_page.ivent_button.click()
        conf_page.motion_detector_button.click()
        page.wait_for_timeout(2500)
        motion_page.motion_schedule_subpage.click(force=True)
        motion_page.motion_disable_radio.click(force=True)
        motion_page.schedule_save_button.click(force=True)
        motion_info_request = CamApi().get_motion_detector_info()
        motion_active_from_api = ET.fromstring(motion_info_request.content)[0][0].text
        assert motion_active_from_api == "0"

    def test_motions_actions_enable(self,page):
        conf_page = ConfPage(page)
        motion_page = MotionPage(page)
        conf_page.ivent_button.click()
        conf_page.motion_detector_button.click()
        page.wait_for_timeout(2500)
        motion_page.motion_actions_subpage.click(force=True)
        motion_page.audio_action_checkbox.set_checked(checked=True, force=True)
        motion_page.ftp_actions_checkbox.set_checked(checked=True,force=True)
        motion_page.ioo_actions_checkbox.set_checked(checked=True,force=True)
        motion_page.record_actions_checkbox.set_checked(checked=True,force=True)
        motion_page.send_email_actions_checkbox.set_checked(checked=True,force=True)
        motion_page.snapshot_action_checkbox.set_checked(checked=True,force=True)
        motion_page.actions_save_button.click(force=True)
        motion_info_request = CamApi().get_motion_detector_info()
        motion_actions_from_api = ET.fromstring(motion_info_request.content)[0][3].text
        assert motion_actions_from_api == "225281"

    def test_motions_actions_disable(self,page):
        conf_page = ConfPage(page)
        motion_page = MotionPage(page)
        conf_page.ivent_button.click()
        conf_page.motion_detector_button.click()
        page.wait_for_timeout(2500)
        motion_page.motion_actions_subpage.click(force=True)
        motion_page.audio_action_checkbox.set_checked(checked=False, force=True)
        motion_page.ftp_actions_checkbox.set_checked(checked=False,force=True)
        motion_page.ioo_actions_checkbox.set_checked(checked=False,force=True)
        motion_page.record_actions_checkbox.set_checked(checked=False,force=True)
        motion_page.send_email_actions_checkbox.set_checked(checked=False,force=True)
        motion_page.snapshot_action_checkbox.set_checked(checked=False,force=True)
        motion_page.actions_save_button.click(force=True)
        motion_info_request = CamApi().get_motion_detector_info()
        motion_actions_from_api = ET.fromstring(motion_info_request.content)[0][3].text
        assert motion_actions_from_api == "0"

