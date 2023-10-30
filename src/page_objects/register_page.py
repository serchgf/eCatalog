import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    def fill_register(self, data_dict=dict):

        logging.info(f"Fill Register")
        self.element("first_name_input").wait_clickable().send_keys(data_dict["first_name"])
        self.element("last_name_input").wait_clickable().send_keys(data_dict["last_name"])
        self.element("email_input").wait_clickable().send_keys(data_dict["email"])
        self.element("telephone_input").wait_clickable().send_keys(data_dict["telephone"])
        self.element("password_input").wait_clickable().send_keys(data_dict["password"])
        self.element("password_confirm_input").wait_clickable().send_keys(data_dict["confirmation"])
        self.element("radio_btn_no").wait_clickable().click()
        self.element("privacy_btn").wait_clickable().click()
        self.element("continue_btn").wait_clickable().click()

    def get_alert_message(self) -> str:
        logging.info("Get alert message")
        return self.element("alert_msg").wait_visible().text