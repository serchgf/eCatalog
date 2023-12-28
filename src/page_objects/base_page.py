import json
import logging
import os
import pathlib
import time

from selenium.common import JavascriptException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from src.web_elements.common import WebElementWrapper
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType



_LOCATOR_DIR_PATH = os.path.join(pathlib.Path(__file__).parent.parent.parent, "locators")
_SCREENSHOTS_DIR_PATH = os.path.join(pathlib.Path(__file__).parent.parent.parent, "screenshots")


class BasePage:
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        self.__driver = driver
        self.__wait_driver = wait_driver
        self.__load_locators_attributes()

    def open(self):
        self.__driver.get(self.url)

    def open_new_url(self, url: str):
        self.__driver.get(url)

    def open_url_mx(self):
        self.__driver.get("https://testintranet.oreillyauto.mx/ecatalog-mx/#/")

    def open_url_us(self):
        self.__driver.get("https://testintranet.oreillyauto.mx/ecatalog-us/#/")

    def open_url_produccion(self):
        self.__driver.get("https://teamnet.oreillyauto.mx/catalogo")

    def close(self):
        self.__driver.close()

    def get_title(self) -> str:
        return self.__driver.title

    def get_url(self) -> str:
        return self.__driver.current_url

    def element(self, key_name) -> WebElementWrapper:
        return self.__dict__[key_name]

    def take_screenshot(self, img_name: str):
        file_path = os.path.join(_SCREENSHOTS_DIR_PATH, f"{img_name}.png")
        self.__driver.save_screenshot(file_path)
        allure.attach(self.__driver.get_screenshot_as_png(), name=f"{img_name}.png", attachment_type=AttachmentType.PNG)

    def scroll_down(self):
        time.sleep(1)
        logging.info("SCROLL DOWN TO HEIGHT")
        self.__driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


    def back_to_previous_page(self):
        logging.info("BACK TO PREVIOUS PAGE")
        self.__driver.back()

    def actionChain(self):
        logging.info("RETURN ACTION CHAIN")
        actions = AC(self.__driver)
        return actions

    def zoom_out(self, percent: int):
        logging.info(F"ZOOM OUT: {percent}")
        self.__driver.execute_script(f"document.body.style.zoom='{percent}%'")

    def wait_until_page_load_complete(self):
        #time.sleep(4)
        logging.info(f"wait until page loads complete")
        try:
            state = self.__driver.execute_script('return document.readyState')
            assert state == 'complete', "Page does not loads correctly"
        except AssertionError:
            state = self.__driver.execute_script('return document.readyState')
            assert state == 'complete', "Page does not loads correctly"
        finally:
            state = self.__driver.execute_script('return document.readyState')
            assert state == 'complete', "Page does not loads correctly"

    def clic_javacript(self, element):
        """
        Recibe webelement
        :param element:
        :return:
        """
        e = element
        try:
            e.click()
        except JavascriptException:
            #    #https://stackoverflow.com/questions/56848671/cannot-read-property-defaultview-of-undefined
            print("Error, element not found... check your Locator")
            self.__driver.execute_script("arguments[0].click();", e)

    def javascript_clic(self, element_text):
        """
        recibe el texto del webElement
        :param element_text:
        :return:
        """
        logging.info(f"Click on: {element_text}")
        xpath = f"//span[normalize-space()='{element_text}']"
        script = f'var elemento = document.evaluate("{xpath}", document, null, 9, null).singleNodeValue; elemento.click();'
        time.sleep(1)
        self.__driver.execute_script(script)

    def move_to_element_and_click(self, element):
        """
        Recibe un webElement y posiciona el mouse sobre el elemento y da click
        :param element:
        :return:
        """
        logging.info(f"Move to Element and click")
        actions = AC(self.__driver)
        actions.move_to_element(element).click().perform()

    def move_to_element(self, element):
        """
        Recibe un webElement y posiciona el mouse sobre el elemento sin dar click
        :param element:
        :return:
        """
        logging.info(f"Move to Element and click")
        actions = AC(self.__driver)
        actions.move_to_element(element).perform()
    def move_to_element_coordinates(self, element,xoffset:int, yoffset:int):
        """
        Recibe un webElement
        :param element:
        :return:
        """
        logging.info(f"Move to Element and click")
        actions = AC(self.__driver)
        actions.move_to_element_with_offset(element, xoffset, yoffset).click().perform()

    def scroll_to_element(self, element):
        logging.info(f"Scroll Down to Element: {element}")
        actions = AC(self.__driver)
        actions.move_to_element(element).perform()

    def press_end_key(self):
        logging.info("Press END key")
        actions = AC(self.__driver)
        actions.send_keys(Keys.END)
        actions.perform()


    def press_page_down(self):
        logging.info("Press PAGE_DOWN key")
        actions = AC(self.__driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        time.sleep(1)
    def press_enter_key(self):
        logging.info("Press ENTER key")
        actions = AC(self.__driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def wait_spinner_disappears(self):
        logging.info("Wait spinner disappears")
        self.element("loading_img").wait_until_disappears()

    def press_esc_key(self):
        logging.info("Press ESCAPE key")
        actions = AC(self.__driver)
        actions.send_keys(Keys.ESCAPE)
        actions.perform()


    def press_enter_key(self):
        logging.info("Press ENTER key")
        actions = AC(self.__driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def press_PageDown_key(self):
        logging.info("Press PAGE DOWN key")
        actions = AC(self.__driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        time.sleep(1)

    def page_down_key_from_element(self, element):
        logging.info(f"Press Page Down key from Element: {element}")
        self.__driver.find_element(element).send_keys(Keys.PAGE_DOWN)

    def __load_locators_attributes(self):
        locator_config = self.__load_locators_config()
        logging.info(f"Locators config: {locator_config}")
        self.__dict__["url"] = locator_config["url"]
        logging.info(f"Adding url instance variable: {locator_config['url']}")
        for key, val in locator_config["locators"].items():
            if val["by"] not in By.__dict__.keys():
                raise ValueError(f"Locator {key} has invalid by value: {val['by']}")
            by = By.__dict__[val["by"]]
            logging.info(f"Adding {key} instance variable, by: {by}, value: {val['value']}")
            self.__dict__[key] = WebElementWrapper(self.__driver, self.__wait_driver, by, val["value"])

    def __load_locators_config(self):
        locator_file_name = type(self).__name__
        locator_absolute_path = os.path.join(_LOCATOR_DIR_PATH, locator_file_name + ".json")
        logging.info(f"Loading locators for class {locator_file_name} from {locator_absolute_path}")
        if not os.path.exists(locator_absolute_path):
            raise FileNotFoundError(f"Locator not found: {locator_absolute_path}")
        with open(locator_absolute_path) as locators_file:
            return json.load(locators_file)

