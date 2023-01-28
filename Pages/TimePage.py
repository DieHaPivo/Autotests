from Pages.BasePage import BasePage


class TimePage(BasePage):

    @property
    def iframe(self):
        return self.page.frame_locator("#frame_subpage")

    @property
    def data_format(self):
        return self.iframe.locator("#sel_date_format")

    @property
    def time_format(self):
        return self.iframe.locator("#sel_time_format")

    @property
    def time_zone_selector(self):
        return self.iframe.locator("#sel_time_zone")

    @property
    def dst_check(self):
        return self.iframe.locator("#input_dst_enable")

    @property
    def ntp_check(self):
        return self.iframe.locator("#input_ntp_enable")

    @property
    def input_ntp_adres(self):
        return self.iframe.locator("#input_ntp_server_addr")

    @property
    def input_ntp_server_port(self):
        return self.iframe.locator("#input_ntp_server_port")

    @property
    def input_ntp_interval(self):
        return self.iframe.locator("#input_ntp_server_interval")

    @property
    def manual_time_check(self):
        return self.iframe.locator("#input_manual_enable")

    @property
    def input_manual_date(self):
        return self.iframe.locator("#input_manual_date")

    @property
    def input_manual_time(self):
        return self.iframe.locator("#timer_manual_settime")

    @property
    def sync_pc(self):
        return self.iframe.locator("#input_syncpc_enable")

    @property
    def dst_value(self):
        return self.iframe.locator("#sel_dst_bias")

    @property
    def dst_start_month(self):
        return self.iframe.locator("#sel_dst_start_month")

    @property
    def dst_start_day(self):
        return self.iframe.locator("#sel_dst_start_day")

    @property
    def dst_start_weekday(self):
        return self.iframe.locator("#sel_dst_start_weekday")

    @property
    def timer_dst_start(self):
        return self.iframe.locator("#timer_dst_start_time")

    @property
    def dst_end_month(self):
        return self.iframe.locator("#sel_dst_end_month")

    @property
    def dst_end_day(self):
        return self.iframe.locator("#sel_dst_end_day")

    @property
    def dst_end_weekday(self):
        return self.iframe.locator("#sel_dst_end_weekday")

    @property
    def timer_dst_end(self):
        return self.iframe.locator("#timer_dst_end_time")

    @property
    def data_picker_month(self):
        return self.iframe.locator(".ui-datepicker-month")

    @property
    def data_picker_year(self):
        return self.iframe.locator(".ui-datepicker-year")

    def get_calendar_date(self, day):
        locator = self.iframe.locator(f"a.ui-state-default:has-text('{day}')")
        for x in range(locator.count()):
            if locator.nth(x).inner_text() == day:
                return locator.nth(x)
