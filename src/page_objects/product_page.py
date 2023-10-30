import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(ProductPage, self).__init__(driver, wait_driver)

    def click_on_write_a_review_link(self):
        logging.info(f"Click on Write a Review link")
        self.element("write_review_link").wait_clickable().click()

    def rate_the_product(self, value: int):
        logging.info(f"Rating a Product {value}")
        self.element(f"rate_radio_btn_{str(value)}").wait_clickable().click()

    def write_a_review(self, name: str, review_text: str):
        logging.info("Writing a Product Review")
        self.element("name_tbx").wait_visible().send_keys(name)
        self.element("review_tbx").wait_visible().send_keys(review_text)

    def click_on_continue_btn(self):
        logging.info(f"Click on Continue button")
        self.element("continue_btn").wait_clickable().click()

    def get_alert_message(self) -> str:
        logging.info("Get alert message")
        return self.element("alert_success_msg").wait_visible().text

