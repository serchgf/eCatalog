import logging
import os
import pathlib
import time
import json

import pytest

from src.page_objects.home_page import HomePage

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")


# --------------------------------------------JUAN LARIOS---------------------------------------------------------------
# HOME PAGE-------------------------------------------------------------------------------------------------------------
# MXTEST-9075
@pytest.mark.homepages2
def test_MXTEST_9075_HomePage_Vehicle_Filtering_Functionality_All_countries(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    #home_page.element("loading_img").wait_until_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_year_dropdown(1)
    home_page.click_on_make_and_select(1)
    home_page.click_on_model_and_select(1)
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.take_screenshot("'USA'-'MEX'-'CAN' selected")
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_Picker_vehicle_btn()
    span_country = home_page.get_country_chips()
    logging.info(span_country)
    assert "MEX" and "CAN" and "USA" in span_country, f"MEX and USA an CAN should be in: {span_country} message"

# MXTEST-9074
#@pytest.mark.homepages2
def test_MXTEST_9074_HomePage_Vehicle_Filtering_Functionality_2_countries(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    #home_page.element("loading_img").wait_until_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_usa_can_country()
    home_page.click_on_year_dropdown(1)
    home_page.click_on_make_and_select(1)
    home_page.click_on_model_and_select(1)
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.take_screenshot("'USA'-'MEX' selected")
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_Picker_vehicle_btn()
    span_country = home_page.get_country_chips()
    logging.info(span_country)
    assert "CAN" or "USA" in span_country, f"USA or CAN should be in: {span_country} message"

# MXTEST-9073
#@pytest.mark.homepages2
def test_MXTEST_9073_HomePage_Vehicle_Filtering_One_country(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    #home_page.element("loading_img").wait_until_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_mex_country()
    home_page.click_on_year_dropdown(1)
    home_page.click_on_make_and_select(1)
    home_page.click_on_model_and_select(1)
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.take_screenshot("'MEX' selected")
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_Picker_vehicle_btn()
    span_country = home_page.get_country_span()
    logging.info(span_country)
    assert "MEX" in span_country, f"MEX should be in: {span_country} message"


# MXTEST-9058
# MXTEST-9056
# MXTEST-9055
# MXTEST-9054
# MXTEST-9053
# MXTEST-9052
# MXTEST-9051
# MXTEST-9076
# MXTEST-9038
# MXTEST-9030
# MXTEST-9024


# ---------------------------------------------lUIS ESPINOSA------------------------------------------------------------
# MXTEST-9027
# MXTEST-9025
# MXTEST-9019
# MXTEST-9023
# MXTEST-9021
# MXTEST-9022
# MXTEST-9020
# MXTEST-9079
# MXTEST-9078
# MXTEST-9077
# MXTEST-9069
# MXTEST-9068
# MXTEST-9067
# MXTEST-9034



# ---------------------------------------------SERGIO GARCIA------------------------------------------------------------
# MXTEST-9033
# MXTEST-9032
# MXTEST-9060
# MXTEST-9059
# MXTEST-9057
# MXTEST-9043
# MXTEST-9042
# MXTEST-9041
# MXTEST-9028
# MXTEST-9036
# MXTEST-9026
# MXTEST-9050
# MXTEST-9049
# MXTEST-9048




# ---------------------------------------------GRECIA LOPEZ-------------------------------------------------------------
# MXTEST-9047
# MXTEST-9046
# MXTEST-9045
# MXTEST-9044
# MXTEST-9018
# MXTEST-9017
# MXTEST-9016
# MXTEST-9015
# MXTEST-9014
# MXTEST-9040
# MXTEST-9039
# MXTEST-9037
# MXTEST-9035
# MXTEST-9031
