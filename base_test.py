import pytest
from playwright.sync_api import Page
from config.environments import get_env

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup (self, page: Page):
        self.page = page
        self.env = get_env()
        self.base_url = self.env["base_url"]
        self.username = self.env["username"]
        self.password = self.env["password"]

        # Go to base URL before every test
        self.page.goto(self.base_url)

        yield

        #Cleanup after every test
        self.page.close()