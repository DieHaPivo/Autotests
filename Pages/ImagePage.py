from Pages.BasePage import BasePage


class ImagePage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator("#frame_subpage")

    @property
    def video_standart_selector(self):
        return self.iframe.locator("#select_video_standard")

    @property
    def video_mirror_selector(self):
        return self.iframe.locator("#select_video_mirror")

    @property
    def coridor_mode_selector(self):
        return self.iframe.locator("#select_video_corridor")

    @property
    def image_templates_selector(self):
        return self.iframe.locator("#select_video_image_templates")

    @property
    def image_output_mode_selector(self):
        return self.iframe.locator("#select_image_output_mode")

    @property
    def image_saturation_slider(self):
        return self.iframe.locator("#slider_image_saturation_value")

    @property
    def image_brightness_slider(self):
        return self.iframe.locator("#slider_image_brightness_value")

    @property
    def image_sharpness_slider(self):
        return self.iframe.locator("#slider_image_sharpness_value")

    @property
    def image_contrast_slider(self):
        return self.iframe.locator("#slider_image_contrast_value")

    @property
    def blc_value_selector(self):
        return self.iframe.locator("#select_image_blc_value")

    @property
    def hlc_value_selector(self):
        return self.iframe.locator("#select_image_hlc_value")

    @property
    def wdr_value_selector(self):
        return self.iframe.locator("#select_image_wdr_value")

    @property
    def whitebalance_value_selector(self):
        return self.iframe.locator("#select_image_whitebalance_value")

    @property
    def exposure_submenu(self):
        return self.iframe.locator("#div_image_exposure_title_text")

    @property
    def exposure_value(self):
        return self.iframe.locator("#select_image_exposure_value")

    @property
    def shutter_value(self):
        return self.iframe.locator("#select_image_shutter_value")

    @property
    def enhancement_submenu(self):
        return self.iframe.locator("#div_image_enhancement_title_text")

    @property
    def lightmetering_value_selector(self):
        return self.iframe.locator("#select_image_lightmetering_value")

    @property
    def autoiris_value_selector(self):
        return self.iframe.locator("#select_image_autoiris_value")

    @property
    def defog_value_selector(self):
        return self.iframe.locator("#select_image_defog_value")

    @property
    def dnr3d_slider(self):
        return self.iframe.locator("#slider_image_3dnr_value")

    @property
    def dnr2d_value_selector(self):
        return self.iframe.locator("#select_image_dnr2d_value")

    @property
    def dnr3d_value_selector(self):
        return self.iframe.locator("#select_image_dnr3d_value")

    @property
    def image_advanced_submenu(self):
        return self.iframe.locator("#div_image_advanced_title")

    @property
    def ldc_slider(self):
        return self.iframe.locator("#slider_image_ldc_value")

    @property
    def smart_ir_value_selector(self):
        return self.iframe.locator("#select_image_smartir_value")

    @property
    def save_button(self):
        return self.iframe.locator("#button_image_baseinfo_save")

    @property
    def saturation_slider(self):
        return self.iframe.locator("#slider_image_saturation_value")

    @property
    def brightness_slider(self):
        return self.iframe.locator("#slider_image_brightness_value")

    @property
    def sharpness_slider(self):
        return self.iframe.locator("#slider_image_sharpness_value")

    @property
    def contrast_slider(self):
        return self.iframe.locator("#slider_image_contrast_value")

    @property
    def redgain_slider(self):
        return self.iframe.locator("#slider_image_redgain_value")

    @property
    def greengain_slider(self):
        return self.iframe.locator("#slider_image_greengain_value")

    @property
    def bluegain_slider(self):
        return self.iframe.locator("#slider_image_bluegain_value")

    @property
    def saturation_value(self):
        return self.iframe.locator('#div_image_saturation_value_text')

    @property
    def brightness_value(self):
        return self.iframe.locator("#div_image_brightness_value_text")

    @property
    def sharpness_value(self):
        return self.iframe.locator("#div_image_sharpness_value_text")

    @property
    def contrast_value(self):
        return self.iframe.locator("#div_image_contrast_value_text")

    @property
    def redgain_value(self):
        return self.iframe.locator("#div_image_redgain_value_text")

    @property
    def greengain_value(self):
        return self.iframe.locator("#div_image_greengain_value_text")

    @property
    def bluegain_value(self):
        return self.iframe.locator("#div_image_bluegain_value_text")

    @property
    def dnr_value(self):
        return self.iframe.locator("#div_image_3dnr_value_text")

    @property
    def ldc_value(self):
        return self.iframe.locator("#div_image_ldc_value_text")

    @property
    def schedule_subpage_button(self):
        return self.iframe.locator("#div_table_image_schedule")

    @property
    def schedule_work_mode_selector(self):
        return self.iframe.locator("#select_image_schedule_day_value")

    @property
    def schedule_start_slider(self):
        return self.iframe.locator('span[style*="left: 25%;"]')

    @property
    def schedule_end_slider(self):
        return self.iframe.locator('span[style*="left: 75%;"]')

    @property
    def schedule_save_button(self):
        return self.iframe.locator("#button_image_schedule_save")

    @property
    def day_night_subpage_button(self):
        return self.iframe.locator("#div_table_image_daynight")

    @property
    def day_night_mode_selector(self):
        return self.iframe.locator("#select_image_daynight_mode_value")

    @property
    def day_night_light_value_selector(self):
        return self.iframe.locator("#select_image_daynight_light_value")

    @property
    def day_night_save_button(self):
        return self.iframe.locator("#button_image_daynight_save")
