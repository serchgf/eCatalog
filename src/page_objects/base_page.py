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
import webbrowser
from allure_commons.types import AttachmentType



_LOCATOR_DIR_PATH = os.path.join(pathlib.Path(__file__).parent.parent.parent, "locators")
_SCREENSHOTS_DIR_PATH = os.path.join(pathlib.Path(__file__).parent.parent.parent, "screenshots")

class images:
    pic1 = "../eCatalog/image_files_/pic1.jpg"
    pic2 = "../eCatalog/image_files_/pic2.jpg"
    pic3 = "../eCatalog/image_files_/blue-nature.jpg"
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

    # def scroll_to_element(self, element):
    #     logging.info(f"Scroll Down to Element: {element}")
    #     actions = AC(self.__driver)
    #     actions.scroll_to_element(element).perform()

    def scroll_to_element(self, element):
        logging.info(f"Scroll Down to Element: {element}")
        xpath = self.element(element).get_locator_value()
        script = f'var elemento = document.evaluate("{xpath}", document, null, 9, null).singleNodeValue; elemento.scrollIntoView();'
        time.sleep(1)
        self.__driver.execute_script(script)

    def clear_img_input(self):
        logging.info(f"Clear image from file input element")
        time.sleep(1)
        self.__driver.execute_script('document.getElementById("fileInput").value = "";')


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

    def switch_to_window(self):
        logging.info("Switch to new window")
        windows = self.__driver.window_handles
        if len(windows) > 1:
            self.__driver.switch_to.window(windows[1])
            self.wait_until_page_load_complete()
            return self.get_title()
    def back_to_window(self):
        logging.info("Switch to new window")
        windows = self.__driver.window_handles
        self.__driver.switch_to.window(windows[0])
        self.wait_until_page_load_complete()
        return self.get_title()

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


    def get_brand_webelement_list_by_letter(self, element, text):
        """
        this function replace the text specified and return a webelement list
        :param element: xpath: //div[@id='x_x']/following-sibling::ul/li
        :param text: p
        :new element: //div[@id='p']/following-sibling::ul/li
        :return: webElement list
        """
        xpath_new = element.replace("x_x", text.lower())
        print(f"new XPATH: {xpath_new}")
        new_webelement_list = self.__driver.find_elements(By.XPATH, xpath_new)
        return new_webelement_list


    def press_shortcuts(self, *args):
        actions = AC(self.__driver)
        key = [key_element for key_element in args]
        if (key[0] == 'CTRL') and (key[1] == 'ALT') and (key[2] == 'n' or 'N'):
            actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('n')
            actions.key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
            logging.info(f"Press keys Ctrl + Alt + N ")
        if key[0] == 'ALT':
            actions.key_down(Keys.ALT)
            match key[1].upper():
                case 'B':
                    actions.send_keys('b')
                case 'V':
                    actions.send_keys('v')
                case 'D':
                    actions.send_keys('d')
                case 'A':
                    actions.send_keys('a')
                case 'J':
                    actions.send_keys('j')
                case 'C':
                    actions.send_keys('c')
                case 'O':
                    actions.send_keys('o')
            actions.key_up(Keys.ALT).perform()
            logging.info(f"Press keys Alt + {key[1]}")
        if key[0] == 'SHIFT':
            actions.key_down(Keys.SHIFT)
            match key[1].upper():
                case 'P':
                    actions.send_keys('p')
                case 'C':
                    actions.send_keys('v')
                case 'D':
                    actions.send_keys('d')
                case 'B':
                    actions.send_keys('b')
                case 'H':
                    actions.send_keys('h')
                case 'L':
                    actions.send_keys('l')
                case 'SPACE':
                    actions.key_down(Keys.SPACE)
                case 'DELETE':
                    actions.key_down(Keys.DELETE)
            actions.key_up(Keys.SHIFT).perform()
            logging.info(f"Press keys Shift + {key[1]}")

    # def new_tab(self, url):
    #     time.sleep(1)
    #     logging.info("New tab")
    #     webbrowser.open_new(url)

    def new_tab(self,url):
        time.sleep(1)
        logging.info("TEST")
        self.__driver.execute_script(f"window.open('{url}', '_blank');")

    def close_browser(self):
        if self.__driver:
            self.__driver.quit()
