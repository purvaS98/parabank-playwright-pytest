from playwright.sync_api import Playwright

def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    page.locator('input[name="username"]').fill("purva")
    page.locator('input[name="password"]').fill("purva")
    page.locator('input[value="Log In"]').click()

