from Pages.BasePage import BasePage

class CloudPage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator('#frame_subpage')

    @property
    def plugin_checkbox(self):
        return self.iframe.locator("#check_enable_trcloud")

    @property
    def idle_timeout_input(self):
        return self.iframe.locator("#input_trcloud_idletimeout")

    @property
    def save_button(self):
        return self.iframe.locator("#button_trcloud_save")



class NetworkPage(BasePage):

    @property
    def smtp_page(self):
        return SmtpPage(self.page)


class SmtpPage(BasePage):

    @property
    def save_button(self):
        return self.iframe.locator("#button_smtp_save")

    @property
    def iframe(self):
        return self.page.frame_locator('#frame_subpage')

    @property
    def gmail_preset_button(self):
        return self.iframe.locator("#button_preset_gmail")

    @property
    def outlook_preset_button(self):
        return self.iframe.locator("#button_preset_msmail")

    @property
    def yahoo_preset_button(self):
        return self.iframe.locator("#button_preset_yahoomail")

    @property
    def username_input(self):
        return self.iframe.locator("#input_smtp_client_username")

    @property
    def password_input(self):
        return self.iframe.locator("#input_smtp_client_password")

    @property
    def device_name_input(self):
        return self.iframe.locator("#input_smtp_client_sender")

    @property
    def recipient_one_input(self):
        return self.iframe.locator("#input_smtp_recipient_one")

    @property
    def recipient_two_input(self):
        return self.iframe.locator("#input_smtp_recipient_two")

    @property
    def recipient_three_input(self):
        return self.iframe.locator("#input_smtp_recipient_three")

    @property
    def recipient_four_input(self):
        return self.iframe.locator("#input_smtp_recipient_four")
