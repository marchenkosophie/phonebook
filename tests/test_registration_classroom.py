import uuid

from models.user import User
from pages.registration_page import RegistrationPage



def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()

    random_suffix = uuid.uuid4().hex[:8]
    user = User(
        f"test{random_suffix}@gmail.com",
        "Password11$"
    )

    registration_page.fill_registration_form(user)

    registration_page.submit_registration()

    assert registration_page.is_registered() is True


def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    user = User(
        "testgmail.com",
        "Password11$"
    )

    registration_page.fill_registration_form(user)
    registration_page.submit_registration()


    assert "Wrong email or password" in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    user = User(
        "test@gmail.com",
        "pas12"
    )

    registration_page.fill_registration_form(user)
    registration_page.submit_registration()

    assert "Wrong email or password" in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_registered_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()

    user = User(
        "sophie@gmail.com",
        "Qwerty123$"
    )

    registration_page.fill_registration_form(user)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()
