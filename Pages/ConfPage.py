from Pages.BasePage import BasePage


class ConfPage(BasePage):

    @property
    def time_button(self):
        return self.page.locator("#div_submenu_item_datetime")

    @property
    def users_button(self):
        return self.page.locator("#div_guide_button_users")

    @property
    def tcpip_button(self):
        return self.page.locator("#div_guide_button_tcpip")


    @property
    def system_button(self):
        return self.page.locator("#div_menuitem_system_parent")

    @property
    def general_button(self):
        return self.page.locator("#div_submenu_item_general")

    @property
    def network_button(self):
        return self.page.locator("#div_menuitem_network_parent")

    @property
    def smtp_button(self):
        return self.page.locator("#div_submenu_item_smtp")

    @property
    def cloud_button(self):
        return self.page.locator("#div_submenu_item_trcloud")

    @property
    def av_button(self):
        return self.page.locator("#div_menuitem_avcodec_parent")

    @property
    def audio_button(self):
        return self.page.locator("#div_submenu_item_audio")

    @property
    def snapshot_button(self):
        return self.page.locator("#div_submenu_item_snapshot")

    @property
    def video_button(self):
        return self.page.locator("#div_submenu_item_video")

    @property
    def osd_button(self):
        return self.page.locator("#div_submenu_item_osd")

    @property
    def image_button(self):
        return self.page.locator("#div_submenu_item_imagesettings")

    @property
    def ivent_button(self):
        return self.page.locator("#div_menuitem_event_parent")

    @property
    def motion_detector_button(self):
        return self.page.locator("#div_submenu_item_motiondetect")

