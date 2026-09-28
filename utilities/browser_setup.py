from playwright.sync_api import Playwright


def get_browser(playwright, browser_name):
    if browser_name == "chrome":
        return playwright.chromium.launch(headless=False, slow_mo=500)

    elif browser_name == "firefox":
        return playwright.firefox.launch(headless=False)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")