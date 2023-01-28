from playwright.sync_api import Page


def test(page: Page, browser):
    context = browser.new_context(http_credentials={"username": "admin", "password": "admin191"})
    page = context.new_page()
    page.goto("http://10.13.101.92/")
    assert page.url == "http://10.13.101.92/cn/viewer_index.asp"
    assert page.locator(".top-logo").is_visible()
    page.locator("a:has-text('Настройки')").click()
    page.wait_for_load_state("networkidle")
    assert page.url == "http://10.13.101.92/cn/home.asp"
    iframe = page.frame_locator("#frames")
    time_button = iframe.locator(".time >> a")
    assert time_button.is_visible()
    assert time_button.get_attribute("href") == "/cn/admin/date.asp"
    with page.expect_response("http://10.13.101.92/cn/xml/ru/system.xml"):
        time_button.click()
    assert iframe.locator(".xinxi-con").nth(0).is_visible()
    page.wait_for_timeout(3000)
    gmt = iframe.locator("[name='root_Time_POSIXTimeZone']")
    gmt.select_option(value='MSK-3MSD,M3.5.0,M10.5.0/3')
    with page.expect_response("http://10.13.101.92/cn/xml/ru/system.xml"):
        iframe.locator(".but-submit").click()
