import logging
import os
import pathlib
import time
import json

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys

from src.page_objects.home_page import HomePage
from src.page_objects.base_page import images

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")


@pytest.mark.phase2_sp2
#@pytest.mark.flaky(reruns=3)
def test_MXTEST_11023_Shortcuts_NIPEnterSearch(web_drivers):
    home_page = HomePage(*web_drivers)
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/brakes/brake-pads-shoes/brake-pads/l/03351/detail/cartek-disc-brake-pad-set-ctk7013a-d50/mij0/ctk7013ad50'
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    home_page.validate_help_center_page()
    home_page.element("hcp_issue_report").find_element().click()
    home_page.validate_issue_report_modal()
    home_page.element("irm_employId").wait_visible().send_keys("3805", Keys.ENTER)
    home_page.element("nip_verified").wait_visible()
    name = home_page.element("irm_employName").find_element().get_attribute('value')
    email = home_page.element("irm_employEmail").find_element().get_attribute('value')
    assert name == 'LARIOS MARISCAL JUAN LUIS' and email == 'juan.larios@oreillyauto.mx', "Fields not filled"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.element("send_report_btn").find_element().click()
    home_page.element("input_nip").wait_visible().send_keys("3805", Keys.ENTER)
    home_page.element("nip_verified").wait_visible()
    name2 = home_page.element("irm_employName").find_element().get_attribute('value')
    email2 = home_page.element("input_email").find_element().get_attribute('value')
    assert name2 == 'Larios Mariscal Juan Luis' and email2 == 'juan.larios@oreillyauto.mx', "Fields not filled"

@pytest.mark.phase2_sp2
#@pytest.mark.flaky(reruns=3)
def test_MXTEST_11015_Shortcuts_GoBackBreadcrumb(web_drivers):
    home_page = HomePage(*web_drivers)
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/accessories/truck-towing-jeep/truck-accessories/alarms/alarm/l/n0165'
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.enable_disable_shortcuts()
    breadcrumb_original = [element.text for element in home_page.element("breadcrumb_elements").find_elements()]
    logging.info(breadcrumb_original)
    home_page.press_shortcuts('SHIFT', 'DELETE')
    home_page.wait_spinner_disappears()
    breadcrumb_actual = [element.text for element in home_page.element("breadcrumb_elements").find_elements()]
    assert len(breadcrumb_actual) < len(breadcrumb_original)
    for x in range(len(breadcrumb_actual)-1):
        home_page.press_shortcuts('SHIFT', 'DELETE')
        home_page.wait_spinner_disappears()
    breadcrumb_final = [element.text for element in home_page.element("breadcrumb_elements").find_elements()]
    assert len(breadcrumb_final) == 0, "The page displayed is not Home Page"
