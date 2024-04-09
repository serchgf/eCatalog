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
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10920_Spanish_Dashboard(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10921_Spanish_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10922_Spanish_Sub_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10923_Spanish_Brands(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()


@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10924_Spanish_Deals(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()


@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10925_Spanish_Parts_interchange(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10926_Spanish_Shortcut(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10927_Spanish_Search_History(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10928_Spanish_Order_List(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10929_Spanish_Add_Vehicle_and_Garage(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10930_Spanish_PLP(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10931_Spanish_PLP_Filters(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10932_Spanish_PDP(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10933_Spanish_PDP_report_issue(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10934_PDP_Report_an_incident_search_store(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10935_Spanish_Help_Center(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10936_Spanish_SearchBar(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()





