from Pages.BasePage import BasePage


class VideoPage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator("#frame_subpage")

    @property
    def hdr_checkbox(self):
        return self.iframe.locator("#check_enable_video_workmode_hdr")

    @property
    def video_subpage(self):
        return self.iframe.locator("#div_title_video")

    @property
    def workmode_subpage(self):
        return self.iframe.locator("#div_title_workmode")

    @property
    def main_codec_selector(self):
        return self.iframe.locator("#select_video_main_codec")

    @property
    def main_resolution_selector(self):
        return self.iframe.locator("#select_video_main_resolution")

    @property
    def main_profile_selector(self):
        return self.iframe.locator("#select_video_main_profile")

    @property
    def main_fps_selector(self):
        return self.iframe.locator("#select_video_main_frame_rate")

    @property
    def main_bitrate_type_selector(self):
        return self.iframe.locator("#select_video_main_bitrate_type")

    @property
    def main_birate_input(self):
        return self.iframe.locator("#input_video_main_bitrate")

    @property
    def main_encode_quality_selector(self):
        return self.iframe.locator("#select_video_main_encode_quality")

    @property
    def main_gop_selector(self):
        return self.iframe.locator("#select_video_main_key_frame")

    @property
    def sub_stream_checkbox(self):
        return self.iframe.locator("#check_enable_video_sub")

    @property
    def sub_codec_selector(self):
        return self.iframe.locator("#select_video_sub_codec")

    @property
    def sub_resolution_selector(self):
        return self.iframe.locator("#select_video_sub_resolution")
    @property
    def sub_profile_selector(self):
        return self.iframe.locator("#select_video_sub_profile")

    @property
    def sub_fps_selector(self):
        return self.iframe.locator("#select_video_sub_frame_rate")

    @property
    def sub_bitrate_type_selector(self):
        return self.iframe.locator("#select_video_sub_bitrate_type")

    @property
    def sub_bitrate_input(self):
        return self.iframe.locator("#input_video_sub_bitrate")

    @property
    def sub_encode_quality_selector(self):
        return self.iframe.locator("#select_video_sub_encode_quality")

    @property
    def sub_gop_selector(self):
        return self.iframe.locator("#select_video_sub_key_frame")

    @property
    def workmode_save_button(self):
        return self.iframe.locator("#button_video_workmode_save")

    @property
    def save_button(self):
        return self.iframe.locator("#button_video_save")

    @property
    def reboot_accept_button(self):
        return self.iframe.locator("#button_reboot_confirm")
