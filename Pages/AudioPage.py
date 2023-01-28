from Pages.BasePage import BasePage


class AudioPage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator('#frame_subpage')

    @property
    def audio_checkbox(self):
        return self.iframe.locator("#check_audio_enable")

    @property
    def codec_selector(self):
        return self.iframe.locator("#select_audio_codec")

    @property
    def sample_ratio_selector(self):
        return self.iframe.locator("#select_audio_sample_ratio")

    @property
    def input_type_selector(self):
        return self.iframe.locator("#select_audio_input_type")

    @property
    def input_volume_slider(self):
        return self.iframe.locator("#div_audio_input_volume_slider")

    @property
    def input_volume_value(self):
        return self.iframe.locator("#div_audio_input_volume_value")

    @property
    def output_volume_slider(self):
        return self.iframe.locator("#div_audio_output_volume_slider")

    @property
    def output_volume_value(self):
        return self.iframe.locator("#div_audio_output_volume_value")

    @property
    def save_button(self):
        return self.iframe.locator("#button_audio_save")

    @property
    def audio_input_declare(self):
        return self.iframe.locator("#div_audio_input_volume_declare")

    @property
    def audio_output_declare(self):
        return self.iframe.locator("#div_audio_output_volume_declare")
