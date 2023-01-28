from Pages.BasePage import BasePage


class SnapshotPage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator('#frame_subpage')

    @property
    def quality_selector(self):
        return self.iframe.locator("#select_snapshot_quality")

    @property
    def interval_input(self):
        return self.iframe.locator("#input_snapshot_interval")

    @property
    def save_button(self):
        return self.iframe.locator("#button_snapshot_save")
