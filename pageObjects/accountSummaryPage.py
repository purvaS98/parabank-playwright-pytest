from utilities.logger import get_logger
import allure


class AccountSummaryPage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(__name__)

        self.welcome_message = page.locator("p.smallText")

    def verify_logged_in_user(self, expected_name):
        with allure.step("Verify welcome message is visible"):
            self.logger.info("Verifying welcome message is visible")
            assert self.welcome_message.is_visible()
            self.logger.info("Welcome message is visible")

        with allure.step(f"Verify logged-in user is '{expected_name}'"):
            actual_message = self.welcome_message.inner_text()
            expected_message = f"Welcome {expected_name}"

            self.logger.info(f"Actual welcome message: '{actual_message}'")
            self.logger.info(f"Expected welcome message: '{expected_message}'")

            assert actual_message == expected_message

            self.logger.info("Logged-in user verification successful")