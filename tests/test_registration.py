from pages.login_page import LoginPage

import random
import string


# random email generation
def generate_random_email(domain="example.com"):
    random_str = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=10)
    )
    return f"test_{random_str}@{domain}"


VALID_PASSWORD = "Qwerty123$"



def test_registration_success(driver):
    email = generate_random_email()
    login_page = LoginPage(driver)

    login_page.open_login_form()

    login_page.fill_email(email)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_registration()

    assert login_page.is_logged() is True


def test_registration_with_wrong_password(driver):
    email = generate_random_email()
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(email)
    login_page.fill_password("123D")
    login_page.submit_registration()

    assert "Wrong email or password" in login_page.get_alert_text()
    login_page.accept_alert()


def test_registration_with_wrong_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email("testemail.com")
    login_page.fill_password("Qwerty123$")
    login_page.submit_registration()

    assert "Wrong email or password" in login_page.get_alert_text()
    login_page.accept_alert()


def test_registration_registered_user(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email("sophie@gmail.com")
    login_page.fill_password("Qwerty123$")
    login_page.submit_registration()

    assert login_page.get_alert_text() == "User already exist"
    login_page.accept_alert()