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
# @pytest.mark.luisao
def test_MXTEST_9027_PLP_Generic_images_from_Selected_Brand(web_drivers):
    home_page = HomePage(*web_drivers)
    #step_1 Enter to the URL.
    home_page.open()
    time.sleep(4)
    #step_2 
    home_page.click_on_brands()
    time.sleep(4)
    home_page.click_on_brands_images_btn()
    img_part_bran = home_page.get_img_part_brand()
    # home_page.get_random_brand()
    time.sleep(4)
    # span_country = home_page.get_country_span()
    # logging.info(span_country)
    # assert "MEX" in span_country or "CAN" in span_country or "USA" in span_country, f"MEX should be in: {span_country} message"


# MXTEST-9025
# YA QUEDO
#@pytest.mark.luisao
def test_MXTEST_9025_Select_entry_records_history(web_drivers):
    home_page = HomePage(*web_drivers)
    #step_1 Enter to the URL.
    home_page.open()
    time.sleep(5)
    #step_2-11 add vehicle
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select(2)
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    #step_12 Select "SEARCH HISTORY" button
    home_page.click_on_search_history()
    time.sleep(1)
    home_page.press_esc_key()
    #step_13 select a free text search entry
    home_page.search('oil')
    home_page.press_enter_key()
    time.sleep(1)
    #step_14 Select "SEARCH HISTORY" button
    home_page.click_on_search_history()
    time.sleep(1)
    home_page.click_on_last_searches()


# MXTEST-9019
# YA JALO
# @pytest.mark.luisao
def test_MXTEST_9019_Search_History_Selected_Vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(10)
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_search_history()
    time.sleep(1)
    home_page.press_esc_key()
    home_page.search('oil')
    home_page.press_enter_key()
    time.sleep(4)
    home_page.clean_search()
    time.sleep(4)
    home_page.click_on_search_history()
    time.sleep(4)
    home_page.click_on_last_searches()
    time.sleep(4)
    home_page.press_esc_key()
    time.sleep(4)
    # ADD ANOTHER VEHICLE
    home_page.click_on_Picker_vehicle_btn()
    time.sleep(4)
    home_page.click_on_add_new_vehicle_btn()
    home_page.click_on_vehicle_type_and_select(3)
    year = home_page.click_on_year_and_select(1)
    make = home_page.click_on_make_and_select(1)
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_search_history()
    time.sleep(1)
    home_page.press_esc_key()
    home_page.search('gps')
    time.sleep(2)
    home_page.press_enter_key()
    time.sleep(4)
    home_page.clean_search()
    time.sleep(4)
    home_page.click_on_search_history()
    time.sleep(4)
    home_page.click_on_last_searches()
    time.sleep(10)


# MXTEST-9023
# @pytest.mark.luisao
# *********************************YA QUEDO*********************************
def test_MXTEST_9023_Search_in_search_history_finder(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    # step_2_3
    home_page.search('oil')
    time.sleep(1)
    # step_4
    home_page.press_enter_key()
    time.sleep(5)
    home_page.clean_search()
    time.sleep(4)
    # step_5-14 Click on the "ADD VEHICLE"
    home_page.click_on_Picker_vehicle_btn()
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2024")
    home_page.write_a_make("Acura")
    home_page.write_a_model("Integra")
    home_page.write_a_submodel("A-Spec")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    time.sleep(2)
    # step_16
    home_page.search('Brakes')
    time.sleep(1)
    # step_17
    home_page.press_enter_key()
    time.sleep(5)
    # step_18
    home_page.click_on_search_history()
    time.sleep(4)
    # step_19-20 Enable the search bar within that modal.
    home_page.search_into_search_history('integra')
    home_page.press_enter_key()
    time.sleep(5)
    # step_21 Delete search
    home_page.clean_searchbar_in_search_history()
    time.sleep(1)
    # step_22 Now enter the search performed in step 16
    home_page.search_into_search_history('oil')
    time.sleep(1)
    home_page.press_enter_key()
    time.sleep(1)
    # step_23 Delete search
    home_page.clean_searchbar_in_search_history()
    time.sleep(1)


# MXTEST-9021
# *********************************YA QUEDO*********************************
# @pytest.mark.luisao
def test_MXTEST_9021_Search_History_WITHOUT_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    # step_2
    home_page.click_on_search_history()
    time.sleep(1)
    # step_3
    home_page.press_esc_key()
    time.sleep(1)
    # step_4
    home_page.search('Battery')
    time.sleep(1)
    # step_5
    home_page.press_enter_key()
    time.sleep(1)
    # step_6
    home_page.clean_search()
    time.sleep(3)
    # step_7
    home_page.search('Energizer - MX')
    time.sleep(1)
    # step_8
    home_page.press_enter_key()
    time.sleep(2)
    # step_9
    home_page.click_on_search_history()
    time.sleep(2)
    # step_10
    home_page.click_on_open_search()
    time.sleep(2)

    # time.sleep(30)


# MXTEST-9022
#@pytest.mark.luisao
def test_MXTEST_9022_Deleting_record_Search_History(web_drivers):
    # STEP_1 ENTER TO URL AND OPEN PAGE
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(2)
    # STEP_2 SELECT "SEARCH HISTORY BUTTON"
    home_page.click_on_search_history()
    time.sleep(1)
    # STEP_3 Then close modal "Search history" and Select the "Search bar"
    home_page.press_esc_key()
    time.sleep(1)
    # STEP_4 Enter a text for search
    home_page.search('F-100A13')
    time.sleep(1)
    # STEP_5 ENTER
    home_page.press_enter_key()
    time.sleep(1)
    # # STEP_6 Clean the text entered in the search engine
    # home_page.clean_search()
    # time.sleep(3)
    # # STEP_7 Enter the name of a brand for search
    # home_page.search('Energizer - MX')
    # time.sleep(1)
    # # STEP_8 ENTER
    # home_page.press_enter_key()
    # time.sleep(1)
    # # STEP_9 Clean the text entered in the search engine
    # home_page.clean_search()
    # time.sleep(3)
    # # STEP_10 Enter a text for search
    # home_page.search('17738')
    # time.sleep(1)
    # # STEP_11 ENTER
    # home_page.press_enter_key()
    # time.sleep(1)
    # # STEP_12 Select "SEARCH HISTORY" button
    home_page.click_on_search_history()
    time.sleep(1)
    # STEP_13_Then select the "FREE SEARCH" tab
    home_page.click_on_open_search()
    time.sleep(5)
    #home_page.javascript_clic("F-100A13")
    # STEP_14 Select the X displayed in the selected lane
    # to do INVESTIGAR COMO HACER CLICK SOBRE LA X CON JAVASCPRIT
    home_page.delete_element_from_open_search()
    time.sleep(10)


# MXTEST-9020
@pytest.mark.luisao
# ************************* PENDIENTE ***********************************
def test_MXTEST_9020_Main_page_Latest_viewed_products_PDP(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    time.sleep(3)
    # step_2
    home_page.click_on_logo_oreily_home()
    time.sleep(3)
    # step_3
    expected_product_selected_list = []
    lasted_viewed_list = []
    # CICLO DE 3 O 5 VECES
    home_page.wait_until_page_load_complete()
    logging.info(f"Click categorie button*****************")
    home_page.click_on_categories_button()
    time.sleep(5)
    home_page.javascript_clic("Oil, Chemicals & Fluids")
    time.sleep(3)
    subcat_1_list_2 = home_page.get_product_list_2()
    home_page.click_element_text_of_list(subcat_1_list_2, "Motor Oil")
    subcat_2_list_2 = home_page.get_product_list_2()
    home_page.click_element_text_of_list(subcat_2_list_2, "Motor Oil - Full Synthetic")
    home_page.wait_search_results_label()
    product_list = home_page.get_link_product_list(0)
    expected_product_selected = home_page.select_random_element_of_list(product_list)
    product_selected = home_page.clean_product_selected(expected_product_selected)
    logging.info(f"Selected: {product_selected}")
    expected_product_selected_list.append(product_selected)
    time.sleep(2)
    for i in range(6):
        home_page.back_to_previous_page()
        product_list = home_page.get_link_product_list(0)
        expected_product_selected = home_page.select_random_element_of_list(product_list)
        product_selected = home_page.clean_product_selected(expected_product_selected)
        logging.info(f"Selected: {product_selected}")
        expected_product_selected_list.append(product_selected)
        time.sleep(1)

    home_page.click_on_logo_oreily_home()

    logging.info(f"Recent Products expected list:")
    home_page.show_product_list(expected_product_selected_list)

    logging.info(f"GET actual lasted viewed products list")
    lasted_product_viewed_list = home_page.get_lasted_viewed_products_list2()

    time.sleep(4)
    # to do HACER  EL CLICK SOBRE EL PRIMER PRODUCTO DE LATEST VIEWED PRODUCTS
    #
    home_page.clicks_carousel_last_viewed_products()
    time.sleep(3)
    home_page.clic_javacript(lasted_product_viewed_list[4])

    time.sleep(10)
    # assert lasted_viewed_list.sort() == expected_product_selected_list.sort()


# MXTEST-9079
# *********************************YA QUEDO*********************************
# @pytest.mark.luisao
def test_MXTEST_9079_Analytics_Empty_Category_Search_with_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1 Enter to the URL.
    home_page.open()
    time.sleep(3)
    # Precondition "ADD VEHICLE"
    home_page.click_on_Picker_vehicle_btn()
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2024")
    home_page.write_a_make("Ford")
    home_page.write_a_model("Mustang")
    home_page.write_a_submodel("EcoBoost")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    time.sleep(2)
    # step_2 Click on "Categories" button
    home_page.click_on_categories_button()
    # step_3 Pick a Category and click on it.
    home_page.javascript_clic("Accessories")
    subcat_1_list_2 = home_page.get_product_list_2()
    home_page.click_element_text_of_list(subcat_1_list_2, "Electronics - MX")
    time.sleep(5)
    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9078
# *********************************YA QUEDO*********************************
# @pytest.mark.luisao
def test_MXTEST_9078_Analytics_Empty_Brands_Search_with_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1 Enter to the URL.
    home_page.open()
    time.sleep(3)
    # Precondition "ADD VEHICLE"
    home_page.click_on_Picker_vehicle_btn()
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2024")
    home_page.write_a_make("Ford")
    home_page.write_a_model("Mustang")
    home_page.write_a_submodel("EcoBoost")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    time.sleep(2)
    # step_2 Click on brands button
    home_page.click_on_brands()
    time.sleep(2)
    # step_3 click_on_"Show all brands" button
    home_page.click_on_show_all_brands()
    time.sleep(5)
    # step_4 Pick a <<Empty Brand>> and click on it.
    """
    en el listado ya no apareceran las marcas "vacias" por lo cual
    se tendra que buscar directamente en el search bar principal
    """
    home_page.search("Dupli-color - MX")
    time.sleep(2)
    home_page.press_enter_key()
    time.sleep(13)
    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9077
# *********************************YA QUEDO*********************************
# @pytest.mark.luisao
def test_MXTEST_9077_Analytics_No_Results_Free_Text_Search_with_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1 Enter to the URL.
    home_page.open()
    time.sleep(3)
    # Precondition "ADD VEHICLE"
    home_page.click_on_Picker_vehicle_btn()
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2024")
    home_page.write_a_make("Ford")
    home_page.write_a_model("Mustang")
    home_page.write_a_submodel("EcoBoost")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    time.sleep(2)
    # step_2_3_4 Click in the search bar field
    home_page.search('qwerty1335')
    time.sleep(1)
    home_page.press_enter_key()
    time.sleep(10)

    # step_5 to do Go to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is saved.


# MXTEST-9069
# @pytest.mark.luisao
def test_MXTEST_9069_Analytics_Empty_Category_Search_without_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    time.sleep(3)
    # step_2 click on brands button
    home_page.click_on_categories_button()
    # step_3 Pick a Category and click on it.
    home_page.javascript_clic("Accessories")
    subcat_1_list_2 = home_page.get_product_list_2()
    home_page.click_element_text_of_list(subcat_1_list_2, "Electronics - MX")
    time.sleep(5)
    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9068
# *********************************YA QUEDO*********************************
# @pytest.mark.luisao
def test_MXTEST_9068_Analytics_Empty_Brands_Search_without_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    time.sleep(3)
    # step_2 click on brands button
    home_page.click_on_brands()
    time.sleep(3)
    # step_3 click_on_"Show all brands" button
    home_page.click_on_show_all_brands()
    time.sleep(5)
    # step_4 Pick a <<Empty Brand>> and click on it.
    """
    en el listado ya no apareceran las marcas "vacias" por lo cual
    se tendra que buscar directamente en el search bar principal
    """
    home_page.search("Dupli-color - MX")
    time.sleep(2)
    home_page.press_enter_key()
    time.sleep(4)
    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9067
# *********************************YA QUEDO*********************************
# @pytest.mark.luisao
def test_MXTEST_9067_Analytics_No_Results_Free_Text_Search_without_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    # step_2_3_4
    # home_page.search_wrong_product_name("☻☻☻")
    home_page.search_wrong_product_name("ae42sdñl")
    time.sleep(4)
    # step_5 to do Go to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 Validate that the value is false in the other boolean/flags columns.
    # step_9 Verify that the information of vehicle is empty/null


# MXTEST-9034
# *********************************YA QUEDO*********************************
# @pytest.mark.luisao
def test_MXTEST_9034_PDP_UniversalProductTagPDP(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/accel/acc/detail/accel-ignition-condenser-111131/acc0/111131"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    # step_5
    # to do Verify the universal compatibility of the product using the following query: <QUERY>.

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
