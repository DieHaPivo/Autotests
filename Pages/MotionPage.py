from Pages.BasePage import BasePage

class MotionPage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator('#frame_subpage')

    @property
    def motion_enable_checkbox(self):
        return self.iframe.locator("#check_motion_enable")

    @property
    def motion_sensivity_slider(self):
        return self.iframe.locator("#slider_motion_sensitivity_value")

    @property
    def motion_threshold_slider(self):
        return self.iframe.locator("#slider_motion_threshold_value")

    @property
    def remove_region_button(self):
        return self.iframe.locator("#button_region_removeall")

    @property
    def select_all_region_button(self):
        return self.iframe.locator("#button_region_allrect")

    @property
    def save_button(self):
        return self.iframe.locator("#button_region_save")

    @property
    def motion_schedule_subpage(self):
        return self.iframe.locator("#div_table_motion_schedule")

    @property
    def motion_mintime_declare_input(self):
        return self.iframe.locator("#input_motion_mintime_text")

    @property
    def motion_schedule_alldays_radio(self):
        return self.iframe.locator("#radio_schedule_alldays")

    @property
    def motion_schedule_radio(self):
        return self.iframe.locator("#radio_schedule_enable")

    @property
    def motion_disable_radio(self):
        return self.iframe.locator("#radio_schedule_disable")

    @property
    def motion_actions_subpage(self):
        return self.iframe.locator("#div_table_motion_actions")

    @property
    def ioo_actions_checkbox(self):
        return self.iframe.locator("#check_action_iooutput")

    @property
    def record_actions_checkbox(self):
        return self.iframe.locator("#check_action_record")

    @property
    def ftp_actions_checkbox(self):
        return self.iframe.locator("#check_action_ftp")

    @property
    def send_email_actions_checkbox(self):
        return self.iframe.locator("#check_action_sendemail")

    @property
    def snapshot_action_checkbox(self):
        return self.iframe.locator("#check_action_snapshot")

    @property
    def audio_action_checkbox(self):
        return self.iframe.locator("#check_action_audioout")

    @property
    def actions_save_button(self):
        return self.iframe.locator("#button_motion_actions_save")

    @property
    def schedule_save_button(self):
        return self.iframe.locator("#button_motion_schedule_save")

    @property
    def motion_sensivity_value(self):
        return self.iframe.locator("#div_motion_sensitivity_value_text")

    @property
    def motion_threshold_value(self):
        return self.iframe.locator("#div_motion_threshold_value_text")