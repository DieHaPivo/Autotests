from playwright.sync_api import Page

from Pages.BasePage import BasePage


class AuthPage(BasePage):
    @property
    def login_input(self):
        return self.page.locator("#input_login_username")

    @property
    def pass_input(self):
        return self.page.locator("#input_login_password")

    @property
    def login_button(self):
        return self.page.locator("#button_login")

    def logining(self):
        self.login_button.click()

    def auth(self, credentials: dict, cam_url: str):
        self.page.goto(cam_url)
        self.login_input.fill(credentials["login"])
        self.pass_input.fill(credentials['password'])
        self.page.locator("#div_language_items").click()
        self.page.locator(".ui-combobox-item").get_by_text("Русский").click()
        self.logining()

    @property
    def lang_selector(self):
        return self.page.locator("#div_language_items")