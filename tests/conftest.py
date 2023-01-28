import pytest

from Pages.AuthPage import AuthPage
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(autouse=True, scope='function')
def auth(page):
    page.set_default_timeout(10000)
    authpage = AuthPage(page)
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    ip = os.getenv("IP")
    authpage.auth({"login": login, "password": password}, ip)
    page.locator("#div_configuration").click()
    yield

