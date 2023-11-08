import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class miclase_unittest(unittest.TestCase):

    def setUp(self):
        s = Service("C:/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_usando_hover_action(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")

        elem = driver.find_element(By.LINK_TEXT, "Enabled")
        hover = ActionChains(driver)
        hover.move_to_element(elem).perform()
        hover.click()
        time.sleep(1)
        n = driver.find_element(By.LINK_TEXT, "Back to JQuery UI")
        # hover over element and click

        hover.move_to_element(n).click().perform()
        time.sleep(3)
        print("Page title: " + driver.title)
        # close browser

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


