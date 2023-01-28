from Pages.BasePage import BasePage


class OsdPage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator("#frame_subpage")

    @property
    def device_name_checkbox(self):
       return self.iframe.locator("#check_enable_sysinfo")

    @property
    def device_time_checkbox(self):
        return self.iframe.locator("#check_enable_systime")

    @property
    def custom_osd_checkbox(self):
        return self.iframe.locator("#check_enable_custom")

    @property
    def save_button(self):
        return self.iframe.locator("#button_osd_save")