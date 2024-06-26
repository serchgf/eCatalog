import logging

from selenium.common import JavascriptException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

class WebElementWrapper:
    """
    Wrapper with common actions to perform in a web element.
    """
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait, by: str, value: str):
        self.__driver = driver
        self.__wait_driver = wait_driver
        self.__locator = (by, value)

    def find_element(self) -> WebElement:
        logging.info(f"Find element using: {self.__locator}")
        return self.__driver.find_element(*self.__locator)

    def find_elements(self) -> list[WebElement]:
        logging.info(f"Find elements using: {self.__locator}")
        return self.__driver.find_elements(*self.__locator)

    def wait_clickable(self) -> WebElement:
        logging.info(f"Wait clickable: {self.__locator}")
        return self.__wait_driver.until(EC.element_to_be_clickable(self.__locator))

    def wait_visible(self) -> WebElement:
        logging.info(f"Wait visible: {self.__locator}")
        return self.__wait_driver.until(EC.visibility_of_element_located(self.__locator))

    def wait_text_to_be_present(self, text: str) -> WebElement:
        logging.info(f"Wait text be present, locator: {self.__locator}, text: {text}")
        return self.__wait_driver.until(EC.text_to_be_present_in_element(self.__locator, text))

    def wait_until_disappears(self):
        logging.info(f"Wait until disappears: {self.__locator}")
        self.__wait_driver.until(EC.invisibility_of_element_located(self.__locator))

    #crea funcion luisao
    def clean_element(self) -> WebElement:
        logging.info(f"Find element using: {self.__locator}")
        return self.__driver.find_element(*self.__locator).clear()

    def accept_alert_message(self):
        logging.info(f"Accept alert : ")
        return self.__driver.switchTo().alert().accept()

    def switch_to_iframe(self) -> WebElement:
        logging.info(f"switch_to_iframe: {self.__locator}")

        return self.__driver.switch_to.frame(self.__locator[1])

    def get_locator_value(self):
        return self.__locator[1]


    def element_is_enable(self) -> bool:
        logging.info(f"This function is to verify if element is enabled {self.__locator}")
        element = self.__driver.find_element(*self.__locator).is_enabled()
        return element #Regresa true si esta habilitado.

    def element_is_displayed(self) -> bool:
        logging.info(f"This function is to verify if element is displayed {self.__locator}")
        element = self.__driver.find_element(*self.__locator).is_displayed()
        return element #Regresa true si esta habilitado.