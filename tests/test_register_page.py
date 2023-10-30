import time

from src.page_objects.account_page import AccountPage
from src.page_objects.register_page import RegisterPage


def test_new_account_register(web_drivers):
    new_user_data = {"first_name":"Jhon",
                     "last_name": "Weak",
                     "email": "thats_my_dogx@ytu.com",
                     "telephone": "1234567890",
                     "password": "continental",
                     "confirmation": "continental"}

    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.fill_register(new_user_data)
    expected_title = "Your Account Has Been Created!"
    assert expected_title == register_page.get_title(), f"Register Failed!, page title should be {expected_title}"
    register_page.take_screenshot("test_new_account_register")


def test_email_already_registered(web_drivers):
    new_user_data = {"first_name":"Jhon",
                     "last_name": "Weak",
                     "email": "thats_my_dog@ytu.com",
                     "telephone": "1234567890",
                     "password": "continental",
                     "confirmation": "continental"}
    expected_msg = "Warning: E-Mail Address is already registered!"
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.fill_register(new_user_data)

    assert expected_msg == register_page.get_alert_message(), f"Register Failed!, page title should be {expected_msg}"
    register_page.take_screenshot("test_email_already_registered")
