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
    home_page.element("loading_img").wait_until_disappears()
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
    assert "MEX" or "CAN" or "USA" in span_country, f"MEX, USA or CAN should be in: {span_country} message"

# MXTEST-9074
@pytest.mark.homepages2
def test_MXTEST_9074_HomePage_Vehicle_Filtering_Functionality_2_countries(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.element("loading_img").wait_until_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_usa_can_country()
    home_page.click_on_year_dropdown(1)
    home_page.click_on_make_and_select(1)
    home_page.click_on_model_and_select(1)
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.take_screenshot("'USA'-'CAN' selected")
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_Picker_vehicle_btn()
    span_country = home_page.get_country_chips()
    logging.info(span_country)
    assert "CAN" or "USA" in span_country, f"USA or CAN should be in: {span_country} message"

# MXTEST-9073
@pytest.mark.homepages2
def test_MXTEST_9073_HomePage_Vehicle_Filtering_One_country(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.element("loading_img").wait_until_disappears()
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
@pytest.mark.homepages2
def test_MXTEST_9051_OrderList_Modal_Contents_Display_Vehicle_Selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.element("loading_img").wait_until_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_mex_country()
    year = home_page.click_on_year_dropdown(1)
    make = home_page.click_on_make_and_select(1).split('\n')
    model = home_page.click_on_model_and_select(1).split('\n')
    submodel = home_page.click_on_submodel_and_select().split('\n')
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_brands()
    home_page.click_on_cartek_brand()
    home_page.element("loading_img").wait_until_disappears()
    home_page.validate_product_list_page('Cartek')
    products_name = home_page.get_products_names()
    home_page.click_on_first_add_to_list_available()
    title, product = home_page.validate_orderList_display()
    assert title == f"{year} {make[0].upper()} {model[0].upper()} {submodel[0].upper()}", f"The title of the panel should be {year} {make[0]} {model[0]} {submodel[0]}"
    assert product in products_name, f"The product {product}wasn't added to the order list"

# MXTEST-9051
@pytest.mark.homepages2
def test_MXTEST_9051_OrderList_Modal_Contents_Display(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.element("loading_img").wait_until_disappears()
    home_page.click_on_brands()
    home_page.click_on_cartek_brand()
    home_page.element("loading_img").wait_until_disappears()
    home_page.validate_product_list_page('Cartek')
    products_name = home_page.get_products_names()
    home_page.click_on_first_add_to_list_available()
    title, product = home_page.validate_orderList_display()
    assert title == "UNSPECIFIED VEHICLE", "The title of the panel should be 'UNSPECIFIED VEHICLE'"
    assert product in products_name, "The product wasn't added to the order list"


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
