import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(CheckoutPage, self).__init__(driver, wait_driver)

    def search(self, value: str):
        logging.info(f"Search {value}")
        self.element("search_input").wait_clickable().send_keys(value)
        self.element("search_btn").wait_clickable().click()

    def click_on_iphone_link(self):
        logging.info(f"Click on Write a Review link")
        self.element("Iphone_link").wait_clickable().click()

    def click_add_to_cart(self):
        logging.info(f"Add Product to cart")
        self.element(f"add_to_cart_btn").wait_clickable().click()


    def click_on_checkout_btn(self):
        logging.info(f"Click on Checkout button")
        self.element("checkout_btn").wait_clickable().click()

    def click_on_guest_radio_btn(self):
        logging.info(f"Click on Guest Radio button")
        self.element("guest_radio_btn").wait_clickable().click()

    def click_on_continue_btn(self):
        logging.info(f"Click on Continue button")
        self.element("continue_btn").wait_clickable().click()


    def get_alert_message(self) -> str:
        logging.info("Get alert message")
        return self.element("alert_success_msg").wait_visible().text

    def select_country(self, value: str):
        logging.info(f"Select city: {value}")
        cities = self.element("select_country_dropdown").find_elements()
        for city in cities:
            if value in city.text:
                city.click()

    def select_state(self, value: str):
        logging.info(f"Select State: {value}")
        states = self.element("select_state_dropdown").find_elements()
        for state in states:
            if value in state.text:
                state.click()

    def fill_register(self, data_dict=dict):
        logging.info(f"Fill Register")
        self.element("firstname").wait_clickable().send_keys(data_dict["first_name"])
        self.element("lastname").wait_clickable().send_keys(data_dict["last_name"])
        self.element("email").wait_clickable().send_keys(data_dict["email"])
        self.element("telephone").wait_clickable().send_keys(data_dict["telephone"])
        self.element("city").wait_clickable().send_keys(data_dict["city"])
        self.element("address_1").wait_clickable().send_keys(data_dict["address"])
        self.element("postcode").wait_clickable().send_keys(data_dict["postcode"])
        self.select_country(data_dict["country"])
        self.select_state(data_dict["state"])
        self.element("continue_btn_guest").wait_clickable().click()
        self.element("textarea").wait_visible().send_keys(data_dict["comment"])
        self.element("continue_btn_step_4").wait_clickable().click()
        self.element("terms_and_conditions_chkbx").wait_clickable().click()
        self.element("continue_btn_step_5").wait_clickable().click()
        self.element("confirm_btn").wait_clickable().click()

    def get_h1_success_message(self, text: str) -> bool:
        logging.info(f"validating if is present the text: {text}")
        return self.element("success_h1_message").wait_text_to_be_preset(text)