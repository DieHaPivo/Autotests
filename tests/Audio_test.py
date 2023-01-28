import xml.etree.ElementTree as ET

import pytest

from Pages.AudioPage import AudioPage
from Pages.ConfPage import ConfPage
from api.cam import CamApi


class TestAudio:

    def test_audio_checkbox_disable(self, page):
        confpage = ConfPage(page)
        audiopage = AudioPage(page)
        confpage.av_button.click()
        confpage.audio_button.click()
        page.wait_for_load_state("networkidle")
        audiopage.audio_checkbox.set_checked(checked=False, force=True)
        audiopage.save_button.click(force=True)
        assert page.wait_for_selector("#div_tips_dialog_content").inner_text() == "Настройки приняты!"
        assert audiopage.codec_selector.is_disabled()
        assert audiopage.input_type_selector.is_disabled()
        audio_request = CamApi().get_audio_info()
        audio_active_from_api = ET.fromstring(audio_request.content)[0][0].text
        assert audio_active_from_api == "0"

    @pytest.mark.parametrize("codec", ["G711A", "G711U", "AAC", "PCM"])
    def test_audio_params(self, page, codec):
        conf_page = ConfPage(page)
        audio_page = AudioPage(page)
        conf_page.av_button.click()
        conf_page.audio_button.click()
        page.wait_for_load_state("networkidle")
        audio_page.audio_checkbox.set_checked(checked=True, force=True)
        assert audio_page.codec_selector.is_enabled()
        assert audio_page.input_type_selector.is_enabled()
        audio_page.codec_selector.select_option(codec)
        audio_page.sample_ratio_selector.select_option(value="1")
        audio_page.input_type_selector.select_option(value="0")
        audio_page.save_button.click(force=True)
        audio_request = CamApi().get_audio_info()
        codec_from_api = ET.fromstring(audio_request.content)[0][1].text
        codec_api = None
        if codec_from_api == '0':
            codec_api = "G711U"
        elif codec_from_api == "1":
            codec_api = "G711A"
        elif codec_from_api == "2":
            codec_api = "AAC"
        elif codec_from_api == "4":
            codec_api = "PCM"
        assert codec_api == codec
        ratio_from_api = ET.fromstring(audio_request.content)[0][2].text
        assert ratio_from_api == "16000"
        input_type_from_api = ET.fromstring(audio_request.content)[0][6].text
        assert input_type_from_api == "0"

    def test_audio_sliders(self, page):
        conf_page = ConfPage(page)
        audio_page = AudioPage(page)
        conf_page.av_button.click()
        conf_page.audio_button.click()
        page.wait_for_load_state("networkidle")
        audio_page.audio_checkbox.set_checked(checked=True, force=True)
        assert audio_page.codec_selector.is_enabled()
        assert audio_page.input_type_selector.is_enabled()
        audio_page.input_volume_slider.click(force=True)
        input_volume_max = "100"
        input_volume_min = "0"
        while audio_page.input_volume_value.inner_text() != input_volume_max:
            audio_page.input_volume_slider.press("ArrowRight")
        assert audio_page.input_volume_value.inner_text() == input_volume_max
        while audio_page.input_volume_value.inner_text() != input_volume_min:
            audio_page.input_volume_slider.press("ArrowLeft")
        assert audio_page.input_volume_value.inner_text() == input_volume_min
        audio_page.output_volume_slider.click(force=True)
        output_volume_max = "100"
        output_volume_min = "0"
        while audio_page.output_volume_value.inner_text() != output_volume_max:
            audio_page.output_volume_slider.press("ArrowRight")
        assert audio_page.output_volume_value.inner_text() == output_volume_max
        while audio_page.output_volume_value.inner_text() != output_volume_min:
            audio_page.output_volume_slider.press("ArrowLeft")
        assert audio_page.output_volume_value.inner_text() == output_volume_min
