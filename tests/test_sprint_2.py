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
# MXTEST-9074

# MXTEST-9073
@pytest.mark.haha
def test_MXTEST_9073_HomePage_Vehicle_Filtering_One_country(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_Picker_vehicle_btn()
    span_country = home_page.get_country_span()
    logging.info(span_country)
    assert "MEX" in span_country or "CAN" in span_country or "USA" in span_country, f"MEX should be in: {span_country} message"


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
# SEARCH BAR-------------------------------------------------------------------------------------------------------------

# MXTEST-9046 SearchBar_Valid_Item Name_Vehicle_Selected
@pytest.mark.pruebitas
def test_MXTEST_9046_SearchBar_Valid_Item_Name_Vehicle_Selected(web_drivers):
    print("PRUEBA")
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    time.sleep(4)

    #home_page.element("search_bar").wait_clickable().send_keys("restore")
    time.sleep(10)
    # home_page.element("search_bar").press_enter_key()
    # time.sleep(4)

    #Go to the database and run the following <query>.

# MXTEST-9045 SearchBar_Valid_Part Number_Vehicle_Selected

# MXTEST-9044 SearchBar_Valid_Category_Vehicle_Selected

# MXTEST-9018 SearchBar_Partial_Search_Term

# MXTEST-9016 SearchBar_Valid_Item Name

# MXTEST-9015 SearchBar_Valid_Part Number

# MXTEST-9014 SearchBar_Valid_Category

    #@pytest.mark.pruebitas
# MXTEST-9040 SearchBar_Autocomplete_Select_Brand
#     print("PRUEBA")
#     home_page = HomePage(*web_drivers)
#     # url= "www.google.com"
#     # home_page.open_new_url(url)
#     home_page.open()
#     time.sleep(4)
#     #home_page.search_product("Motor Oil") #Busqueda por valor
#     home_page.element("search_bar").wait_clickable().send_keys("bos")
#     bosch_brand = home_page.element("highlight_search_result").find_element()
#     home_page.clic_javacript(bosch_brand)
    #Go to the database and run the following <query>.

# MXTEST-9039 SearchBar_Autocomplete_Select_Category

# MXTEST-9037 SearchBar_Autosuggestions

# MXTEST-9035 SearchBar_Invalid_Search Term

# MXTEST-9031 SearchBar_Keywords_search














