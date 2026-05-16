
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against: qa, staging"
    )

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)