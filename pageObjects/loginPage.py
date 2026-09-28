import allure
from pageObjects.accountSummaryPage import AccountSummaryPage
from utilities.logger import get_logger


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(__name__)

        self.username = page.locator('input[name="username"]')
        self.password = page.locator('input[name="password"]')
        self.login_button = page.locator('input[value="Log In"]')

    def enter_username(self, username):
        with allure.step("Enter username"):
            self.logger.info("Entering username")
            self.username.fill(username)
            self.logger.info("Username entered successfully")

    def enter_password(self, password):
        with allure.step("Enter password"):
            self.logger.info("Entering password")
            self.password.fill(password)
            self.logger.info("Password entered successfully")

    def click_login(self):
        with allure.step("Clicking login button"):
            self.logger.info("Clicking Login button")
            self.login_button.click()
            self.logger.info("Login button clicked successfully")

        return AccountSummaryPage(self.page)