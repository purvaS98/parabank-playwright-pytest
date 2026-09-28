import os
import shutil
import pytest

from utilities.browser_setup import get_browser
from pageObjects.loginPage import LoginPage
from utilities.config_reader import get_credentials


# Delete screenshots from previous test run
def pytest_sessionstart(session):
    screenshot_dir = "screenshots"

    if os.path.exists(screenshot_dir):
        shutil.rmtree(screenshot_dir)

    os.makedirs(screenshot_dir)


# Capture test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def browserInstance(playwright, request):

    browser = get_browser(playwright, "chrome")

    context = browser.new_context()
    page = context.new_page()

    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    yield page

    # Take screenshot only if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        screenshot_name = f"{request.node.name}.png"
        screenshot_path = os.path.join(
            "screenshots",
            screenshot_name
        )

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )

        print(f"\nScreenshot saved: {screenshot_path}")

    context.close()
    browser.close()


@pytest.fixture
def loginPage(browserInstance):
    return LoginPage(browserInstance)


@pytest.fixture
def credentials():
    username, password = get_credentials()
    return username, password