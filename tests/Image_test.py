import xml.etree.ElementTree as ET

from Pages.ConfPage import ConfPage
from Pages.ImagePage import ImagePage
from api.cam import CamApi


class TestImage:

    def test_video_params(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        image_page.video_standart_selector.select_option(value="0")
        image_page.video_mirror_selector.select_option(value="2")
        image_page.coridor_mode_selector.select_option(value="1")
        image_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        image_request = CamApi().get_image_info()
        cam_image_info_request = CamApi().get_cam_image_info()
        image_standart_from_api = ET.fromstring(image_request.content)[0][0].text
        assert image_standart_from_api == "0"
        image_mirror_from_api = ET.fromstring(image_request.content)[0][6].text
        assert image_mirror_from_api == "2"
        corridor_mode_from_api = ET.fromstring(cam_image_info_request.content)[0][1].text
        assert corridor_mode_from_api == "1"

    def test_image_settings(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        image_page.image_output_mode_selector.select_option(value="3")
        image_page.blc_value_selector.select_option(value="1")
        image_page.hlc_value_selector.select_option(value="1")
        image_page.wdr_value_selector.select_option(value="1")
        image_page.whitebalance_value_selector.select_option(value="2")
        image_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        cam_image_info_request = CamApi().get_image_info()
        image_params_request = CamApi().get_cam_image_info()
        blc_from_api = ET.fromstring(cam_image_info_request.content)[0][13][1].text
        assert blc_from_api == "1"
        hlc_from_api = ET.fromstring(image_params_request.content)[0][6][11][2].text
        assert hlc_from_api == "1"
        wdr_from_api = ET.fromstring(cam_image_info_request.content)[0][13][0].text
        assert wdr_from_api == "1"
        white_balance_from_api = ET.fromstring(image_params_request.content)[0][6][13][0].text
        assert white_balance_from_api == "2"
        image_mode_from_api = ET.fromstring(image_params_request.content)[0][6][0].text
        assert image_mode_from_api == "3"

    def test_image_saturation_sliders(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        page.wait_for_timeout(1000)
        image_page.image_output_mode_selector.select_option(value="4")
        assert image_page.saturation_slider.is_visible()
        assert image_page.sharpness_slider.is_visible()
        assert image_page.brightness_slider.is_visible()
        assert image_page.contrast_slider.is_visible()
        saturation_value_max = "100"
        saturation_value_min = "0"
        page.wait_for_timeout(1000)
        image_page.saturation_slider.click(force=True)
        while image_page.saturation_value.inner_text() != saturation_value_max:
            image_page.saturation_slider.press("ArrowRight")
        assert image_page.saturation_value.inner_text() == saturation_value_max
        image_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        image_params_request2 = CamApi().get_cam_image_info()
        saturation_value_from_api = ET.fromstring(image_params_request2.content)[0][6][1].text
        assert saturation_value_from_api == saturation_value_max
        image_mode_from_api = ET.fromstring(image_params_request2.content)[0][6][0].text
        assert image_mode_from_api == "4"
        image_page.saturation_slider.click(force=True)
        while image_page.saturation_value.inner_text() != saturation_value_min:
            image_page.saturation_slider.press("ArrowLeft")
        assert image_page.saturation_value.inner_text() == saturation_value_min
        page.locator("#div_tips_dialog_content").wait_for(state="hidden")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        saturation_value_from_api = ET.fromstring(image_params_request.content)[0][6][1].text
        assert saturation_value_from_api == saturation_value_min

    def test_image_brightness_slider(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        page.wait_for_timeout(1000)
        image_page.image_output_mode_selector.select_option(value="4")
        assert image_page.saturation_slider.is_visible()
        assert image_page.sharpness_slider.is_visible()
        assert image_page.brightness_slider.is_visible()
        assert image_page.contrast_slider.is_visible()
        brightness_value_max = "100"
        brightness_value_min = "0"
        page.wait_for_timeout(1000)
        image_page.brightness_slider.click(force=True)
        while image_page.brightness_value.inner_text() != brightness_value_max:
            image_page.brightness_slider.press("ArrowRight")
        assert image_page.brightness_value.inner_text() == brightness_value_max
        image_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        image_params_request = CamApi().get_cam_image_info()
        brightness_value_from_api = ET.fromstring(image_params_request.content)[0][6][4].text
        assert brightness_value_from_api == brightness_value_max
        image_mode_from_api = ET.fromstring(image_params_request.content)[0][6][0].text
        assert image_mode_from_api == "4"
        image_page.brightness_slider.click(force=True)
        while image_page.brightness_value.inner_text() != brightness_value_min:
            image_page.brightness_slider.press("ArrowLeft")
        assert image_page.brightness_value.inner_text() == brightness_value_min
        page.locator("#div_tips_dialog_content").wait_for(state="hidden")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        brightness_value_from_api = ET.fromstring(image_params_request.content)[0][6][4].text
        assert brightness_value_from_api == brightness_value_min

    def test_image_sharpness_slider(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        page.wait_for_timeout(1000)
        image_page.image_output_mode_selector.select_option(value="4")
        assert image_page.saturation_slider.is_visible()
        assert image_page.sharpness_slider.is_visible()
        assert image_page.brightness_slider.is_visible()
        assert image_page.contrast_slider.is_visible()
        sharpness_value_max = "100"
        sharpness_value_min = "0"
        page.wait_for_timeout(1000)
        image_page.sharpness_slider.click(force=True)
        while image_page.sharpness_value.inner_text() != sharpness_value_max:
            image_page.sharpness_slider.press("ArrowRight")
        assert image_page.sharpness_value.inner_text() == sharpness_value_max
        image_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        image_params_request = CamApi().get_cam_image_info()
        sharpness_value_from_api = ET.fromstring(image_params_request.content)[0][6][2].text
        assert sharpness_value_from_api == sharpness_value_max
        image_mode_from_api = ET.fromstring(image_params_request.content)[0][6][0].text
        assert image_mode_from_api == "4"
        image_page.sharpness_slider.click(force=True)
        while image_page.sharpness_value.inner_text() != sharpness_value_min:
            image_page.sharpness_slider.press("ArrowLeft")
        assert image_page.sharpness_value.inner_text() == sharpness_value_min
        page.locator("#div_tips_dialog_content").wait_for(state="hidden")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        sharpness_value_from_api = ET.fromstring(image_params_request.content)[0][6][2].text
        assert sharpness_value_from_api == sharpness_value_min

    def test_image_contrast_slider(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        page.wait_for_timeout(1000)
        image_page.image_output_mode_selector.select_option(value="4")
        assert image_page.saturation_slider.is_visible()
        assert image_page.sharpness_slider.is_visible()
        assert image_page.brightness_slider.is_visible()
        assert image_page.contrast_slider.is_visible()
        contrast_value_max = "100"
        contrast_value_min = "0"
        page.wait_for_timeout(1000)
        image_page.contrast_slider.click(force=True)
        while image_page.contrast_value.inner_text() != contrast_value_max:
            image_page.contrast_slider.press("ArrowRight")
        assert image_page.contrast_value.inner_text() == contrast_value_max
        image_page.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        image_params_request = CamApi().get_cam_image_info()
        contrast_value_from_api = ET.fromstring(image_params_request.content)[0][6][3].text
        assert contrast_value_from_api == contrast_value_max
        image_mode_from_api = ET.fromstring(image_params_request.content)[0][6][0].text
        assert image_mode_from_api == "4"
        image_page.contrast_slider.click(force=True)
        while image_page.contrast_value.inner_text() != contrast_value_min:
            image_page.contrast_slider.press("ArrowLeft")
        assert image_page.contrast_value.inner_text() == contrast_value_min
        page.locator("#div_tips_dialog_content").wait_for(state="hidden")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        contrast_value_from_api = ET.fromstring(image_params_request.content)[0][6][3].text
        assert contrast_value_from_api == contrast_value_min

    def test_whitebalance_slider_max_value(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        page.wait_for_timeout(1000)
        image_page.whitebalance_value_selector.select_option(value="4")
        assert image_page.redgain_slider.is_visible()
        assert image_page.greengain_slider.is_visible()
        assert image_page.bluegain_slider.is_visible()
        color_value_max = "100"
        image_page.redgain_slider.click(force=True)
        while image_page.redgain_value.inner_text() != color_value_max:
            image_page.redgain_slider.press("ArrowRight")
        assert image_page.redgain_value.inner_text() == color_value_max
        image_page.greengain_slider.click(force=True)
        while image_page.greengain_value.inner_text() != color_value_max:
            image_page.greengain_slider.press("ArrowRight")
        assert image_page.greengain_value.inner_text() == color_value_max
        image_page.bluegain_slider.click(force=True)
        while image_page.bluegain_value.inner_text() != color_value_max:
            image_page.bluegain_slider.press("ArrowRight")
        assert image_page.bluegain_value.inner_text() == color_value_max
        image_page.save_button.click(force=True)
        white_balance_request = CamApi().get_cam_image_info()
        white_balance_mode_from_api = ET.fromstring(white_balance_request.content)[0][6][13][0].text
        assert white_balance_mode_from_api == "4"
        red_value_from_api = ET.fromstring(white_balance_request.content)[0][6][13][1].text
        assert red_value_from_api == color_value_max
        green_value_from_api = ET.fromstring(white_balance_request.content)[0][6][13][2].text
        assert green_value_from_api == color_value_max
        blue_value_from_api = ET.fromstring(white_balance_request.content)[0][6][13][3].text
        assert blue_value_from_api == color_value_max

    def test_whitebalance_slider_min_value(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        page.wait_for_timeout(1000)
        image_page.whitebalance_value_selector.select_option(value="4")
        assert image_page.redgain_slider.is_visible()
        assert image_page.greengain_slider.is_visible()
        assert image_page.bluegain_slider.is_visible()
        color_value_min = "0"
        image_page.redgain_slider.click(force=True)
        while image_page.redgain_value.inner_text() != color_value_min:
            image_page.redgain_slider.press("ArrowLeft")
        assert image_page.redgain_value.inner_text() == color_value_min
        image_page.greengain_slider.click(force=True)
        while image_page.greengain_value.inner_text() != color_value_min:
            image_page.greengain_slider.press("ArrowLeft")
        assert image_page.greengain_value.inner_text() == color_value_min
        image_page.bluegain_slider.click(force=True)
        while image_page.bluegain_value.inner_text() != color_value_min:
            image_page.bluegain_slider.press("ArrowLeft")
        assert image_page.bluegain_value.inner_text() == color_value_min
        image_page.save_button.click(force=True)
        white_balance_request = CamApi().get_cam_image_info()
        white_balance_mode_from_api = ET.fromstring(white_balance_request.content)[0][6][13][0].text
        assert white_balance_mode_from_api == "4"
        red_value_from_api = ET.fromstring(white_balance_request.content)[0][6][13][1].text
        assert red_value_from_api == color_value_min
        green_value_from_api = ET.fromstring(white_balance_request.content)[0][6][13][2].text
        assert green_value_from_api == color_value_min
        blue_value_from_api = ET.fromstring(white_balance_request.content)[0][6][13][3].text
        assert blue_value_from_api == color_value_min

    def test_exposure_params(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        image_page.exposure_submenu.click(force=True)
        page.wait_for_timeout(1000)
        assert image_page.wdr_value_selector.is_hidden()
        image_page.exposure_value.select_option(value="1")
        image_page.shutter_value.select_option(value="7")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        exposure_value_from_api = ET.fromstring(image_params_request.content)[0][6][12][0].text
        assert exposure_value_from_api == "1"
        shutter_value_from_api = ET.fromstring(image_params_request.content)[0][6][12][2].text
        assert shutter_value_from_api == "7"

    def test_enchancement_params(self, page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        image_page.enhancement_submenu.click(force=True)
        page.wait_for_timeout(1000)
        image_page.lightmetering_value_selector.select_option(value="1")
        image_page.autoiris_value_selector.select_option(value="1")
        image_page.defog_value_selector.select_option(value="1")
        image_page.dnr3d_value_selector.select_option(value="1")
        image_page.dnr2d_value_selector.select_option(value="1")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        lightmetering_from_api = ET.fromstring(image_params_request.content)[0][6][12][1].text
        assert lightmetering_from_api == "1"
        autoiris_from_api = ET.fromstring(image_params_request.content)[0][6][12][3].text
        assert autoiris_from_api == "1"
        defog_from_api = ET.fromstring(image_params_request.content)[0][6][7].text
        assert defog_from_api == "1"
        dnr3d_from_api = ET.fromstring(image_params_request.content)[0][6][10].text
        assert dnr3d_from_api == "1"
        dnr2d_from_api = ET.fromstring(image_params_request.content)[0][6][9].text
        assert dnr2d_from_api == "1"
        dnr_max_value = "100"
        dnr_min_value = "0"
        image_page.dnr3d_slider.click(force=True)
        while image_page.dnr_value.inner_text() != dnr_max_value:
            image_page.dnr3d_slider.press("ArrowRight")
        assert image_page.dnr_value.inner_text() == dnr_max_value
        while image_page.dnr_value.inner_text() != dnr_min_value:
            image_page.dnr3d_slider.press("ArrowLeft")
        assert image_page.dnr_value.inner_text() == dnr_min_value

    def test_image_advanced_params(self,page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        image_page.image_advanced_submenu.click(force=True)
        page.wait_for_timeout(1000)
        image_page.smart_ir_value_selector.select_option(value="1")
        ldc_max_value = "100"
        ldc_min_value = "0"
        image_page.ldc_slider.click(force=True)
        while image_page.ldc_value.inner_text() != ldc_max_value:
            image_page.ldc_slider.press("ArrowRight")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        smart_ir_from_api = ET.fromstring(image_params_request.content)[0][6][8].text
        assert smart_ir_from_api == "1"
        ldc_value_from_api = ET.fromstring(image_params_request.content)[0][6][6].text
        assert ldc_value_from_api == ldc_max_value
        page.locator("#div_tips_dialog_content").wait_for(state="hidden")
        image_page.ldc_slider.click(force=True)
        while image_page.ldc_value.inner_text() != ldc_min_value:
            image_page.ldc_slider.press("ArrowLeft")
        image_page.save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        ldc_value_from_api = ET.fromstring(image_params_request.content)[0][6][6].text
        assert ldc_value_from_api == ldc_min_value

    def test_day_night_schedule(self,page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        image_page.schedule_subpage_button.click(force=True)
        image_page.schedule_work_mode_selector.select_option(value="3")
        image_page.schedule_save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        image_params_request = CamApi().get_cam_image_info()
        schedule_from_api = ET.fromstring(image_params_request.content)[0][3].text
        assert schedule_from_api == "3"
        schedule_time_from_api = ET.fromstring(image_params_request.content)[0][5].text
        assert schedule_time_from_api == "21600-64800"

    def test_day_night_settings(self,page):
        conf_page = ConfPage(page)
        image_page = ImagePage(page)
        conf_page.av_button.click()
        conf_page.image_button.click()
        image_page.day_night_subpage_button.click(force=True)
        image_page.day_night_mode_selector.select_option(value="3")
        image_page.day_night_light_value_selector.select_option(value="2")
        image_page.day_night_save_button.click(force=True)
        image_params_request = CamApi().get_cam_image_info()
        light_value_from_api = ET.fromstring(image_params_request.content)[0][9][4].text
        assert light_value_from_api == "2"
        day_night_mode_from_api = ET.fromstring(image_params_request.content)[0][9][0].text
        assert day_night_mode_from_api == "3"

