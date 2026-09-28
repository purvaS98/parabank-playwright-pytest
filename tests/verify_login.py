from time import sleep

import allure


# allure reporting
@allure.title("Verifying successful login")

def test_login(loginPage, credentials):

    username, password = credentials

    loginPage.enter_username(username)
    loginPage.enter_password(password)
    account_summary_page = loginPage.click_login()
    account_summary_page.verify_logged_in_user("LESLY FUENTES")


