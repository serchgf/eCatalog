import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(SearchPage, self).__init__(driver, wait_driver)

    def search(self, value: str):
        logging.info(f"Search {value}")
        self.element("search_input").wait_clickable().send_keys(value)
        self.element("search_btn").wait_clickable().click()

    def get_search_criteria_label_msg(self):
        logging.info("Get search Criteria message from Label")
        return self.element("search_message_label").wait_visible().text
