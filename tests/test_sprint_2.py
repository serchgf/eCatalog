import logging
import os
import pathlib
import time
import json


import pytest
from selenium.common import TimeoutException

from src.page_objects.home_page import HomePage

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")


# --------------------------------------------JUAN LARIOS---------------------------------------------------------------
# HOME PAGE-------------------------------------------------------------------------------------------------------------
# MXTEST-9075
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.test9075
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9075_HomePage_Vehicle_Filtering_Functionality_All_countries(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
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
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.test9074
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9074_HomePage_Vehicle_Filtering_Functionality_2_countries(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_usa_can_country()
    home_page.click_on_year_and_select(1)
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
@pytest.mark.sprint2_regression
@pytest.mark.homepages2
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9073_HomePage_Vehicle_Filtering_One_country(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_mex_country()
    home_page.click_on_year_and_select(1)
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
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.flaky(reruns=2)
@pytest.mark.test9058
def test_MXTEST_9058_OrderList_Modal_Individual_Deletion(web_drivers):
    # Initialize logging
    logging.basicConfig(level=logging.INFO)
    # Initialize home page object
    home_page = HomePage(*web_drivers)
    # Open the URL
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih'
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #Validate product list page
    home_page.validate_product_list_page('Cartek')

    # Add multiple products to order list
    print("Add to List")
    ol_products = home_page.add_multiple_products_to_order_list(2)
    print("Add to List complete")
    logging.info(f"list_products{ol_products}")
    # Delete product from order list
    product = home_page.delete_product_from_order_list()
    logging.info(f"list_products{product}")

    # Check if product is deleted or order list is empty
    if product == "You haven't added items on your order list.":
        logging.info("Order list is empty")
        assert True

    elif isinstance(product, list):
        deleted_product = list(set(ol_products) - set(product))[0]
        logging.info(f"Product {deleted_product} was deleted from list")
        assert True

    else:
        logging.error("Unknown error occurred during product deletion")
        assert False, "Unknown error occurred during product deletion"






# MXTEST-9056
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.test9056
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9056_OrderList_Modal_Product_Navigation(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    home_page.click_on_brands()
    home_page.click_on_brand('Cartek')
    home_page.wait_spinner_disappears()
    home_page.validate_product_list_page('Cartek')
    products_name = home_page.get_products_names()
    home_page.click_on_first_add_to_list_available()
    title, product = home_page.validate_orderList_display()
    assert product in products_name, "The product wasn't added to the order list"
    home_page.click_img_thumbnail()
    pdp_title = home_page.get_pdp_title()
    assert product == pdp_title, "The PDP is not the correct for the product selected"
    home_page.get_data_from_detailed_description_section()
    home_page.get_data_from_details_product_information_section()
    home_page.get_data_from_details_how_to_use_the_product_section()


# MXTEST-9055
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.test9055
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9055_OrderList_Modal_Cancel_Clear_List(web_drivers):
    home_page = HomePage(*web_drivers)
    #home_page.open()
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih'
    home_page.open_new_url(url)
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()

    #home_page.click_on_brands()
    #home_page.click_on_brand('Cartek')
    #home_page.wait_spinner_disappears()
    home_page.validate_product_list_page('Cartek')
    order_list_Bc = home_page.add_multiple_products_to_order_list(5)  # ORDER LIST BEFORE CANCEL
    order_list_Ac = home_page.delete_all_products_cancel()  # ORDER LIST AFTER CANCEL
    assert order_list_Ac == order_list_Bc, "The order list was change after cancellation"

# MXTEST-9054
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.test9054
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9054_OrderList_Modal_Clear_List(web_drivers):
    home_page = HomePage(*web_drivers)
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih'
    home_page.open_new_url(url)
    #home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    #home_page.click_on_brands()
    #home_page.click_on_brand('Cartek')
    #home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    home_page.validate_product_list_page('Cartek')
    home_page.add_multiple_products_to_order_list(5)
    order_list = home_page.delete_all_products()
    if order_list == "You haven't added items on your order list.":
        logging.info(f"Order list is empty")
        assert True




# MXTEST-9053
@pytest.mark.sprint2_regression
@pytest.mark.homepages2
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9053_OrderList_Modal_Contents_Display_Non_Application_Product(web_drivers):
    home_page = HomePage(*web_drivers)
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/body-glove-mx/mhg'
    home_page.open_new_url(url)
    time.sleep(4)
    home_page.wait_spinner_disappears()
    #home_page.click_on_brands()
    #home_page.click_on_brand('Body Glove - MX')
    #home_page.wait_spinner_disappears()
    home_page.validate_product_list_page('Body Glove')
    products_name = home_page.get_products_names()
    home_page.click_on_first_add_to_list_available()
    title, product = home_page.validate_orderList_display()
    assert title == "NON VEHICLE SPECIFIC", "The title of the panel should be 'NON VEHICLE SPECIFIC'"
    assert product in products_name, "The product wasn't added to the order list"

# MXTEST-9052
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.test9052
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9052_OrderList_Modal_Contents_Display_Vehicle_Selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_mex_country()
    #year = home_page.click_on_year_and_select(1)
    #make = home_page.click_on_make_and_select(1).split('\n')
    #model = home_page.click_on_model_and_select(1).split('\n')
    #submodel = home_page.click_on_submodel_and_select().split('\n')
    home_page.write_a_year("2020")
    home_page.write_a_make("Chevrolet")
    home_page.write_a_model("Aveo")
    home_page.write_a_submodel("LT")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_brands()
    home_page.click_on_brand('Cartek')
    home_page.wait_spinner_disappears()
    home_page.validate_product_list_page('Cartek')
    products_name = home_page.get_products_names()
    home_page.click_on_first_add_to_list_available()
    title, product = home_page.validate_orderList_display()
    assert title == "2020 CHEVROLET AVEO LT", f"The title of the panel should be 2020 CHEVROLET AVEO LT"
    assert product in products_name, f"The product {product} wasn't added to the order list"

# MXTEST-9051
@pytest.mark.sprint2_regression
@pytest.mark.homepages2
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9051_OrderList_Modal_Contents_Display(web_drivers):
    home_page = HomePage(*web_drivers)
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih'
    home_page.open_new_url(url)
    #home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    #home_page.click_on_brands()
    #home_page.click_on_brand('Cartek')
    #home_page.wait_spinner_disappears()
    home_page.validate_product_list_page('Cartek')
    products_name = home_page.get_products_names()
    home_page.click_on_first_add_to_list_available()
    title, product = home_page.validate_orderList_display()
    assert title == "UNSPECIFIED VEHICLE", "The title of the panel should be 'UNSPECIFIED VEHICLE'"
    assert product in products_name, "The product wasn't added to the order list"


# MXTEST-9076
# MXTEST-9038
@pytest.mark.sprint2_regression
@pytest.mark.homepages2
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9038_Vehicle_Fitment_notes_PLP(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.select_mex_country()
    #home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2020")
    home_page.write_a_make("Chevrolet")
    home_page.write_a_model("Aveo")
    home_page.write_a_submodel("LT")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_brands()
    home_page.click_on_brand('Cartek')
    home_page.wait_spinner_disappears()
    fit_notes = home_page.get_plp_fit_notes()
    assert len(fit_notes) > 0, "The products shown in page has not fitment notes"



# MXTEST-9030
@pytest.mark.sprint2_regression
#@pytest.mark.homepages2
@pytest.mark.test9030
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9030_PLP_Product_images_Selected_Brand(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.click_on_brands()
    home_page.click_on_brand('Body Glove')
    home_page.wait_spinner_disappears()
    home_page.validate_product_list_page('Body Glove')
    img_src = home_page.get_plp_images()
    img_error = "https://testintranet.oreillyauto.mx/ecatalog-mx/assets/images/product/coming-soon.png"
    if len(img_src) > 0:
        logging.info("The images was loaded correctly")
        print("The images was loaded correctly")
        assert True

        if len(img_src) == len(set(img_src)):
            logging.info("All images are distinct")
            print("All images are distinct")
            assert True

        if len(img_src) != len(set(img_src)) and img_error in img_src:

            logging.info("Image coming soon displayed")
            print("Image coming soon displayed")
            assert True

        if len(img_src) != len(set(img_src)) and img_error not in img_src:
            logging.info("Some images are the same")
            print("Some images are the same")
            assert False, "The images should be different"

    else:
        logging.info("The images do not load correctly")
        print("The images do not load correctly")
        assert False, "The images should be loaded"



# MXTEST-9024
@pytest.mark.sprint2_regression
@pytest.mark.homepages2
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9024_PLP_Product_images_Selected_Category(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.wait_spinner_disappears()
    home_page.click_on_categories_button()
    category_list = home_page.get_general_categories_list()
    if len(category_list) < 1:
        category_list = home_page.get_general_categories_list()
    # Click on Categories
    home_page.select_specific_category_of_list(category_list, 24)
    # Get the list of subcategories
    subcategory_list = home_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = home_page.get_subcategory_list()
    # Click on Subcategories
    home_page.select_specific_category_of_list(subcategory_list, 0)
    subcategory = home_page.select_first_subcategory()
    home_page.wait_spinner_disappears()
    home_page.validate_product_list_page(subcategory)
    img_src = home_page.get_plp_images()
    img_error = "https://testintranet.oreillyauto.mx/ecatalog-mx/assets/images/product/coming-soon.png"
    if len(img_src) > 0:
        logging.info("The images was loaded correctly")
        print("The images was loaded correctly")
        assert True

        if len(img_src) == len(set(img_src)):
            logging.info("All images are distinct")
            print("All images are distinct")
            assert True

        if len(img_src) != len(set(img_src)) and img_error in img_src:
            logging.info("Image coming soon displayed")
            print("Image coming soon displayed")
            assert True

        if len(img_src) != len(set(img_src)) and img_error not in img_src:
            logging.info("Some images are the same")
            print("Some images are the same")
            assert False, "The images should be different"

    else:
        logging.info("The images do not load correctly")
        print("The images do not load correctly")
        assert False, "The images should be loaded"



# ---------------------------------------------lUIS ESPINOSA------------------------------------------------------------
# MXTEST-9027
# *********************************YA QUEDO*********************************
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
#@pytest.mark.luisao
@pytest.mark.test9027
def test_MXTEST_9027_PLP_Generic_images_from_Selected_Brand(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/filters/cabin-air-filter/l/02700"
    # step_1_2 Enter to the URL.
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    #step_3_Click on any Brand logo.
    home_page.click_on_first_product()
    #step_4_Check if the product has a default generic image no matter what.
    home_page.validate_presence_of_default_image_src()

# MXTEST-9025
# YA QUEDO
@pytest.mark.luisao
#@pytest.mark.sprint2_regression
@pytest.mark.test9025
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9025_Select_entry_records_history(web_drivers):
    home_page = HomePage(*web_drivers)
    #step_1 Enter to the URL.
    home_page.open()
    home_page.wait_spinner_disappears()
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
    home_page.press_esc_key()
    #step_13 select a free text search entry
    home_page.search_specific_product('oil')
    home_page.press_enter_key()
    #step_14 Select "SEARCH HISTORY" button
    home_page.click_on_search_history()
    home_page.click_on_last_searches()
    home_page.validate_presence_of_oil_product()



# MXTEST-9019
# YA JALO
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9019_Search_History_Selected_Vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    search_criteria1 = 'detallado'
    search_criteria2 = 'aceite'
    #time.sleep(2)
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_search_history()
    home_page.press_esc_key()
    home_page.search_specific_product(search_criteria1)
    home_page.press_enter_key()
    home_page.clean_search()
    home_page.click_on_search_history()
    home_page.click_on_last_searches()
    home_page.press_esc_key()
    # ADD ANOTHER VEHICLE
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_add_new_vehicle_btn()
    home_page.click_on_vehicle_type_and_select(3)
    year = home_page.click_on_year_and_select(1)
    make = home_page.click_on_make_and_select(1)
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_search_history()
    home_page.press_esc_key()
    home_page.search_specific_product(search_criteria2)
    home_page.press_enter_key()
    home_page.clean_search()
    home_page.click_on_search_history()
    home_page.click_on_last_searches()
    home_page.validate_presence_of_oil_product()



# MXTEST-9023
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
# *********************************YA QUEDO*********************************
def test_MXTEST_9023_Search_in_search_history_finder(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    home_page.wait_spinner_disappears()
    # step_2_3
    home_page.search_specific_product('oil')
    # step_4
    home_page.press_enter_key()
    home_page.clean_search()
    # step_5-14 Click on the "ADD VEHICLE"
    home_page.click_on_Picker_vehicle_btn()
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2024")
    home_page.write_a_make("Acura")
    home_page.write_a_model("Integra")
    home_page.write_a_submodel("A-Spec")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    # step_16
    home_page.search_specific_product('Brakes')
    # step_17
    home_page.press_enter_key()
    # step_18
    home_page.click_on_search_history()
    # step_19-20 Enable the search bar within that modal.
    home_page.search_into_search_history('integra')
    home_page.press_enter_key()
    # step_21 Delete search
    home_page.clean_searchbar_in_search_history()
    # step_22 Now enter the search performed in step 16
    home_page.search_into_search_history('oil')
    home_page.press_enter_key()
    # step_23 Delete search
    home_page.clean_searchbar_in_search_history()


# MXTEST-9021
# *********************************YA QUEDO*********************************
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9021_Search_History_WITHOUT_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    home_page.wait_spinner_disappears()
    search_criteria1 ='Battery'
    search_criteria2 = 'Energizer - MX'
    # step_2
    home_page.click_on_search_history()
    # step_3
    home_page.press_esc_key()
    # step_4
    home_page.search_specific_product(search_criteria1)
    # step_5
    home_page.press_enter_key()
    # step_6
    home_page.clean_search()
    # step_7t
    home_page.search_specific_product(search_criteria2)
    # step_8
    home_page.press_enter_key()
    # step_9
    home_page.click_on_search_history()
    # step_10
    home_page.click_on_open_search()



# MXTEST-9022
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9022_Deleting_record_Search_History(web_drivers):
    # STEP_1 ENTER TO URL AND OPEN PAGE
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    # STEP_2 SELECT "SEARCH HISTORY BUTTON"
    home_page.click_on_search_history()
    # STEP_3 Then close modal "Search history" and Select the "Search bar"
    home_page.press_esc_key()
    # STEP_4 Enter a text for search
    home_page.search_specific_product('F-100A13')
    # STEP_5 ENTER
    home_page.press_enter_key()
    # STEP_6 Clean the text entered in the search engine
    home_page.clean_search()
    # STEP_7 Enter the name of a brand for search
    home_page.search_specific_product('Energizer - MX')
    # STEP_8 ENTER
    home_page.press_enter_key()
    # STEP_9 Clean the text entered in the search engine
    home_page.clean_search()
    # STEP_10 Enter a text for search
    home_page.search_specific_product('17738')
    # STEP_11 ENTER
    home_page.press_enter_key()
    # STEP_12 Select "SEARCH HISTORY" button
    home_page.click_on_search_history()
    # STEP_13_Then select the "FREE SEARCH" tab
    home_page.click_on_open_search()
    # STEP_14 Select the X displayed in the selected lane
    home_page.delete_element_from_open_search()
    #STEP_15 Select the "CLEAR HISTORY" button
    # STEP_16 Select the "Yes, Remove All" button
    home_page.click_clear_search_history_btn()
    home_page.press_esc_key()
    # STEP_17-18 Select the "Search bar"
    home_page.clean_search()
    home_page.search_specific_product('Detailing')
    # STEP_19 Enter
    home_page.press_enter_key()
    # STEP_20 Select "SEARCH HISTORY" button
    home_page.click_on_search_history()
    # STEP_21 Teclear shiftkey + C
    home_page.shortcut_new_client()
    # STEP_22 Select the "CONTINUE" button
    home_page.click_new_client_continue_btn()
    home_page.click_on_logo_oreily_home()
    carousel_val = home_page.validate_carousel_is_visible()
    print(carousel_val)
    assert carousel_val is True, "Carousel is not displayed"





# MXTEST-9020
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
# ************************* YA QUEDO ***********************************
def test_MXTEST_9020_Main_page_Latest_viewed_products_PDP(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    home_page.wait_spinner_disappears()
    # step_2
    home_page.click_on_logo_oreily_home()
    # step_3
    expected_product_selected_list = []
    lasted_viewed_list = []
    # CICLO DE 3 O 5 VECES
    home_page.wait_until_page_load_complete()
    logging.info(f"Click categorie button*****************")
    home_page.click_on_categories_button()
    home_page.javascript_clic("Oil, Chemicals & Fluids")
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
    time.sleep(2)
    # to do HACER  EL CLICK SOBRE EL PRIMER PRODUCTO DE LATEST VIEWED PRODUCTS
    home_page.clicks_carousel_last_viewed_products()
    home_page.clic_javacript(lasted_product_viewed_list[4])
    part_number = home_page.get_part_number()
    print(part_number)
    assert " " != part_number, f" part number is not present in the page"

# MXTEST-9079
# *********************************YA QUEDO*********************************
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9079_Analytics_Empty_Category_Search_with_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1 Enter to the URL.
    home_page.open()
    home_page.wait_spinner_disappears()
    #time.sleep(3)
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
    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9078
# *********************************YA QUEDO*********************************
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9078_Analytics_Empty_Brands_Search_with_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1 Enter to the URL.
    home_page.open()
    home_page.wait_spinner_disappears()
    # Precondition "ADD VEHICLE"
    home_page.click_on_Picker_vehicle_btn()
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2024")
    home_page.write_a_make("Ford")
    home_page.write_a_model("Mustang")
    home_page.write_a_submodel("EcoBoost")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    # step_2 Click on brands button
    home_page.click_on_brands()
    # step_3 click_on_"Show all brands" button
    home_page.click_on_show_all_brands()
    # step_4 Pick a <<Empty Brand>> and click on it.
    """
    en el listado ya no apareceran las marcas "vacias" por lo cual
    se tendra que buscar directamente en el search bar principal
    """
    home_page.search_specific_product("Dupli-color - MX")
    home_page.press_enter_key()
    #time.sleep(5)
    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9077
# *********************************YA QUEDO*********************************
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9077_Analytics_No_Results_Free_Text_Search_with_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1 Enter to the URL.
    home_page.open()
    home_page.wait_spinner_disappears()
    # Precondition "ADD VEHICLE"
    home_page.click_on_Picker_vehicle_btn()
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year("2024")
    home_page.write_a_make("Ford")
    home_page.write_a_model("Mustang")
    home_page.write_a_submodel("EcoBoost")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    # step_2_3_4 Click in the search bar field
    home_page.search_specific_product("qwerty1335")
    home_page.press_enter_key()

    # step_5 to do Go to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is saved.


# MXTEST-9069
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9069_Analytics_Empty_Category_Search_without_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    home_page.wait_spinner_disappears()
    # step_2 click on brands button
    home_page.click_on_categories_button()
    # step_3 Pick a Category and click on it.
    home_page.javascript_clic("Accessories")
    subcat_1_list_2 = home_page.get_product_list_2()
    home_page.click_element_text_of_list(subcat_1_list_2, "Electronics - MX")
    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9068
# *********************************YA QUEDO*********************************
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9068_Analytics_Empty_Brands_Search_without_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    home_page.wait_spinner_disappears()
    # step_2 click on brands button
    home_page.click_on_brands()
    # step_3 click_on_"Show all brands" button
    home_page.click_on_show_all_brands()
    # step_4 Pick a <<Empty Brand>> and click on it.
    """
    en el listado ya no apareceran las marcas "vacias" por lo cual
    se tendra que buscar directamente en el search bar principal
    """
    home_page.search_specific_product("Dupli-color - MX")
    home_page.press_enter_key()


    # step_5 to doGo to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 to do Validate that the value is false in the other boolean/flags columns.
    # step_9 to do Verify that the information of vehicle is empty/null


# MXTEST-9067

# *********************************YA QUEDO*********************************
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9067_Analytics_No_Results_Free_Text_Search_without_vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    # step_1
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.wait_until_page_load_complete()
    # step_2_3_4
    # home_page.search_wrong_product_name("☻☻☻")
    home_page.search_wrong_product_name("ae42sdñl")
    # step_5 to do Go to the database and run the query with the boolean flag.
    # step_6 to do Validate the URL in the database.
    # step_7 to do Validate the word in the database.
    # step_8 Validate that the value is false in the other boolean/flags columns.
    # step_9 Verify that the information of vehicle is empty/null


# MXTEST-9034
# *********************************YA QUEDO*********************************
@pytest.mark.luisao
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9034_PDP_UniversalProductTagPDP(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/accel/acc/detail/accel-ignition-condenser-111131/acc0/111131"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.validate_nonAplication_product_label()
    # step_5
    # to do Verify the universal compatibility of the product using the following query: <QUERY>.

# PDP ------------------------------------------------------------------------------------------------------------------
# MXTEST-9034



# ---------------------------------------------SERGIO GARCIA------------------------------------------------------------
# MXTEST-9033
#@pytest.mark.haha
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9033_PDP_ProductDetailsCompatibility(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih/detail/cartek-brake-master-cylinder-new-05019401aa/mkg0/05019401aa"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.press_PageDown_key()
    home_page.wait_spinner_disappears()
    home_page.click_compatibility_tab()
    home_page.press_PageDown_key()
    home_page.wait_until_page_load_complete()
    #compatibility_list = home_page.get_compatibility_list()
    home_page.show_compatibility_vehicle_list_tab()
    # todo Verify the information given in COMPATIBILITY tab in the database using the following query: <QUERY>.

# MXTEST-9032
#@pytest.mark.haha
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9032_PDP_ProductDetailsBeingShown(web_drivers):
    home_page = HomePage(*web_drivers)
    #url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih/detail/cartek-ceramic-front-brake-pads-ccd2052/mza0/ccd2052"
    #nueva url con todas las secciones
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/husky-spring/hsk/detail/husky-spring-suspension-leveling-kit-069409bds/hsk0/069409bds"
    #url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/gates-mx/mnv/detail/gates-mx-v-belt-1140/mnv0/1140"
    #url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/oil-chemicals-fluids/motor-oil/motor-oil-vehicle-specific/l/07065/detail/red-line-full-synthetic-motor-oil-0w-30-1-quart-11114/rl00/11114"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    expected_sections = ['Detailed description', 'Product information', 'How to use the product', 'About this brand']
    # expected_sections = ['Detailed description', 'Product information', 'How to use the product']
    home_page.validate_presence_of_details_sections(expected_sections)
    home_page.get_data_from_detailed_description_section()
    home_page.get_data_from_details_product_information_section()
    home_page.get_data_from_details_how_to_use_the_product_section()
    home_page.get_data_from_details_about_this_brand_section()

#url con datos junto con vehiculo : 2021 Alfa Romeo Giulia Lusso
#breacrumb: Home-All brands-Cartek-CCD2052
#"https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih/detail/cartek-ceramic-front-brake-pads-ccd2052/mza0/ccd2052"

# MXTEST-9060
#@pytest.mark.haha
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9060_PDP_Report_discrepances_fitment_notes(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih/detail/cartek-ceramic-front-brake-pads-ccd2052/mza0/ccd2052"
    #url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/gates-mx/mnv/detail/gates-mx-v-belt-1140/mnv0/1140"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.scroll_down()
    home_page.click_send_a_report_link()
    full_name = "Sergio Garcia"
    email = "email_fake@fake.com"
    phone = "1234567890"
    store = "Abastos"
    #issue_type = "Vehicle Fitment"
    issue_type = "Wrong Image"
    description_error_text = "Test message text, the image is Wrong"
    home_page.scroll_down()
    home_page.wait_spinner_disappears()
    home_page.fill_product_info_report(full_name, email, phone, store, issue_type, description_error_text)
    home_page.click_send_report_button_info_report_btn()
    home_page.validate_report_created_confirmation()

# MXTEST-9059
#@pytest.mark.haha
@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9059_PDP_Report_Discrepancies(web_drivers):
    #Verify you can report any discrepancy in the system and obtain a ticket number as a reference.
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih/detail/cartek-ceramic-front-brake-pads-ccd2052/mza0/ccd2052"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.scroll_down()
    home_page.click_send_a_report_link()
    nip = "5507"
    # full_name = "Grecia Lopez"
    # email = "email_fake@fake.com"
    phone = "1234567890"
    store = "Abastos"
    #issue_type = "Wrong Image"
    issue_type = "Imagen Incorrecta"
    description_error_text = "Test message text, the image is Wrong"
    home_page.scroll_down()
    #home_page.wait_spinner_disappears()
    ##########
    home_page.click_send_report_button_info_report_btn()
    home_page.validate_report_created_confirmation()
    home_page.get_report_ticket_number()

# MXTEST-9057
#@pytest.mark.haha
#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
#@pytest.mark.test9057
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9057_PDP_Add_to_List(web_drivers):
    #Verify the functionality of the "Add to List" button for adding products to the list
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.click_on_Picker_vehicle_btn()
    year = "2020"
    make = "Arctic Cat"
    model = "Alterra 700"
    submodel = "Base"
    home_page.write_a_vehicle_type("Deportes Motorizados")
    home_page.write_a_year(year)
    home_page.write_a_make(make)
    home_page.write_a_model(model)
    home_page.write_a_submodel(submodel)
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih/detail/cartek-ceramic-front-brake-pads-ccd2052/mza0/ccd2052"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.click_add_to_list_btn()
    vehicle_description = home_page.validate_presence_of_modal_order_list_elements()
    assert f"{year.upper()} {make.upper()} {model.upper()} {submodel.upper()}" in vehicle_description, f"Vehicle information does not match"

# MXTEST-9043
#@pytest.mark.haha
#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9043_PDP_ProductDetailsNotCompatibility(web_drivers):
    #Verify that the Vehicle Compatibility is not being shown when in the PDP of a universal product.
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/accel/acc/detail/accel-ignition-condenser-111131/acc0/111131"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    home_page.validate_compatibility_button_is_not_displayed()
    home_page.validate_nonAplication_product_label()

# MXTEST-9042
@pytest.mark.haha
#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9042_PDP_UniversalProductTagPLP(web_drivers):
    #Verify that the universal product tag is being shown in the PLP.
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/armor-all/mft"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    home_page.validate_nonAplication_product_label()

# MXTEST-9041
#@pytest.mark.haha
#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9041_PDP_ResourcesNotDisplaying(web_drivers):
    #Verify that there are no resources are being shown in the Product Detail Page when a product has no resources linked to it.
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/accel/acc/detail/accel-spark-plug-0526-4/acc0/05264"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.validate_resources_tab_is_not_displayed()

# MXTEST-9028
#@pytest.mark.haha
@pytest.mark.sprint2_regression
#@pytest.mark.pruebitas
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9028_PDP_Generic_images_from_Selected_Brand(web_drivers):
    #Verify that generic images are being shown in the PDP.
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/filters/cabin-air-filter/l/02700"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.validate_presence_of_default_image_src()
    product_list = home_page.get_link_product_list(0)
    home_page.select_random_element_of_list(product_list)
    home_page.validate_presence_of_default_image_src()

# MXTEST-9036
#@pytest.mark.haha
#@pytest.mark.pruebitas
#@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9036_PDP_ResourcesDisplay(web_drivers):
    #Verify that the available resources are being shown in the Product Detail Page.
    # encontrar un producto que contenga la tab "resources" -> se encontro producto y se utiliza el url para poder ejecutar el tc script con el tab recursos.
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/dupli-color/mlu/detail/dupli-color-perfect-match-8-ounce-charcoal-gray-metallic-touch-up-paint-bcc0331/dpl1/bcc0331"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.click_resources_tab()
    assert home_page.element("general_info_resources").wait_visible(), "Resources is not visible"
    assert home_page.element("general_info_resources").wait_clickable(), "Resources is not clickable"

# MXTEST-9026
#@pytest.mark.haha
#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9026_PDP_Product_image_with_available_images_Selected_Brand(web_drivers):
    #Verify that the available images are being shown in the PDP.
    home_page = HomePage(*web_drivers)
    #home_page.open_url_mx()
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/battery-accessories/battery-boxes-trays/l/n0357/detail/super-start-battery-tray-01339/ss01/01339"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    # home_page.click_on_brands()
    # home_page.click_on_brand('Body Glove')
    # home_page.wait_spinner_disappears()
    # product_list = home_page.get_description_product()
    # brand_selected = home_page.select_random_element_of_list(product_list)
    # logging.info(f"Selected: {brand_selected}")
    #Click en imagen anterior e imagen siguiente
    #Se omite seleccion de marca para utilizar un producto con numero de parte "01339" que tiene todas las opciones de imagen
    home_page.click_img_arrow_back_button()
    time.sleep(.2)
    home_page.click_img_arrow_forward_button()
    time.sleep(.2)
    #Habilitar la vision 360
    home_page.element("img_button_360").wait_clickable().click()
    time.sleep(.2)
    #Disable the 360 degree
    home_page.element("img_button").wait_clickable().click()
    #Click para abrir la imagen
    home_page.click_main_product_img()
    #Click en imagen anterior e imagen siguiente
    home_page.element("img_arrow_forward_button_2").wait_clickable().click()
    time.sleep(.2)
    home_page.element("img_arrow_back_button_2").wait_clickable().click()
    time.sleep(.2)
    #Cerrar la imagen
    home_page.element("close_modal_btn").wait_clickable().click()
    #Habilitar la vision 360
    home_page.element("img_button_360").wait_clickable().click()
    time.sleep(.2)
    #Acercar y alejar con zoom
    home_page.element("zoom_in").wait_clickable().click()
    time.sleep(.2)
    home_page.element("zoom_out").wait_clickable().click()
    time.sleep(.2)
    #Boton play para habilitar la vision 360
    home_page.element("play_360_button").wait_clickable().click()
    time.sleep(.2)
    #Pausar la vision 360
    home_page.element("pause_360_button").wait_clickable().click()
    time.sleep(.2)
    # Disable the 360 degree
    home_page.element("img_button").wait_clickable().click()
    home_page.element("zoom_in").wait_until_disappears()


# SEARCH BAR-------------------------------------------------------------------------------------------------------------
# MXTEST-9050
#@pytest.mark.pruebitas
#@pytest.mark.haha
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9050_SearchBar_Autocomplete_Select_Brand_Vehicle_selected(web_drivers):
    #Verify that the system displays relevant search results when a brand is selected from the autocomplete suggestions with vehicle selected
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.select_vehicle_specific()
    search_criteria = "Gat"
    home_page.select_first_suggestion_brand(search_criteria)
    home_page.wait_spinner_disappears()
    #BRAND GATES
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"The brand: {search_criteria.upper()} no se encontro en {producto.upper()}"
    #Go to the database and run the following <query>.

# MXTEST-9049
#@pytest.mark.haha
#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9049_SearchBar_Autocomplete_Select_Category_Vehicle_Selected(web_drivers):
    #Verify that the system displays the category landing page CLP for the category selected from the autocomplete suggestions with a vehicle selected
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.select_vehicle_specific()
    search_criteria = "Oil"
    home_page.search_product(search_criteria)
    #CATEGORY OIL
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"The category: {search_criteria.upper()} no se encontro en {producto.upper()}"
    #Go to the database and run the following <query>.

# MXTEST-9048
#@pytest.mark.haha
#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9048_SearchBar_Partial_Search_Term_Vehicle_selected(web_drivers):
    #Verify that the system displays results when a search is made with a partial <<search term>> in the search bar field with the vehicle selected
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.select_vehicle_specific()
    search_criteria = "Brak"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"
    assert len(lista_productos) > 0, f"The partial search term {search_criteria} didn't have results"

# ---------------------------------------------GRECIA LOPEZ-------------------------------------------------------------
# SEARCH BAR-------------------------------------------------------------------------------------------------------------

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
#@pytest.mark.pruebitas
def test_MXTEST_9046_SearchBar_Valid_Item_Name_Vehicle_Selected(web_drivers):
    #Verify that the system displays the result when a search is made by typing a valid item name in the search bar field with the vehicle selected
    # MXTEST-9046 SearchBar_Valid_Item Name_Vehicle_Selected
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.select_vehicle_specific()
    search_criteria = "Battery"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto.upper()}"
    #Go to the database and run the following <query>.

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9045_searchBar_valid_part_number_vehicle_selected(web_drivers):
    #Verify that the system displays the result when a search is made by typing a valid part number in the search bar field with the vehicle selected
    # MXTEST-9045 SearchBar_Valid_Part Number_Vehicle_Selected
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    part_number = "33849"
    home_page.select_vehicle_specific()
    home_page.element("search_bar").wait_clickable().send_keys(part_number)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    part_number_list = home_page.element("part_number_button").find_elements()
    #logging.info(f"El tamaño de la lista es: {len(part_number_list)}")
    #for part in part_number_list:
    #    logging.info(part.text)
    assert part_number in part_number_list[0].text, f"No se encontro el numero de parte:{part_number} en la busqueda:{part_number_list[0].text}"
    # Go to the database and run the following <query>.

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9044_searchBar_valid_category_vehicle_selected(web_drivers):
    # MXTEST-9044 SearchBar_Valid_Category_Vehicle_Selected
    # Verify that the system displays the result when a search is made by typing a valid category in the search bar field with the vehicle selected
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    home_page.select_vehicle_specific()
    search_criteria = "Brake"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"
    assert len(lista_productos) > 0, f"The category {search_criteria} didn't have results"

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=3)
def test_MXTEST_9018_searchBar_partial_search_term(web_drivers):
    #erify that the system displays results when a search is made with a partial <<search term>> in the search bar field.
    # MXTEST-9018 SearchBar_Partial_Search_Term
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    search_criteria = "Brak"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"
    assert len(lista_productos) > 0, f"The partial search term {search_criteria} didn't have results"

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9016_searchBar_valid_item_name(web_drivers):
# MXTEST-9016 SearchBar_Valid_Item Name
#Verify that the system displays the result when a search is made by typing a valid item name in the search bar field.
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    search_criteria = "Oil"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"
    assert len(lista_productos) > 0, f"The item name {search_criteria} didn't have results"
    #Go to the database and run the following <query>.

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9015_searchBar_valid_part_number(web_drivers):
# MXTEST-9015 SearchBar_Valid_Part Number
#Verify that the system displays the result when a search is made by typing a valid part number in the search bar field.
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    part_number = "33849"
    home_page.element("search_bar").wait_clickable().send_keys(part_number)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    part_number_list = home_page.element("part_number_button").find_elements()
    assert part_number in part_number_list[0].text, f"Part number:{part_number} was not found in:{part_number_list[0].text}"
    # Go to the database and run the following <query>.

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
#@pytest.mark.pruebitas
def test_MXTEST_9014_searchBar_valid_category(web_drivers):
    #Verify that the system displays the result when a search is made by typing a valid category in the search bar field
    # MXTEST-9014 SearchBar_Valid_Category
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    search_criteria = "Brake"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"
    assert len(lista_productos) > 0, f"The category {search_criteria} didn't have results"


#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9040_searchBar_autocomplete_select_brand(web_drivers):
    #MXTEST-9040 SearchBar_Autocomplete_Select_Brand
    #Verify that the system displays relevant search results when a brand is selected from the autocomplete suggestions
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    #BRAND CARTE
    search_criteria = "Carte"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.element("text_brand_search").wait_visible()
    category = home_page.element("highlight_search_result").find_element()
    home_page.clic_javacript(category)
    home_page.wait_spinner_disappears()
    lista_principal = home_page.get_description_product()
    palabra_buscada = "CARTEK"
    # Verificar si la palabra está en la lista
    encontrada = False
    for lista in lista_principal:
        if palabra_buscada in lista:
            encontrada = True
            break
    assert encontrada == True, f"The brand '{palabra_buscada}' is not in the list"
    #Go to the database and run the following <query>.

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9039_searchBar_autocomplete_select_category(web_drivers):
    # MXTEST-9039 SearchBar_Autocomplete_Select_Category
    #Verify that the system displays the category landing page CLP for the category selected from the autocomplete suggestions.
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    #CATEGORY FILTERS
    search_criteria = "Fil"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    category = home_page.element("highlight_search_result").find_element()
    home_page.clic_javacript(category)
    home_page.wait_spinner_disappears()
    lista_principal = home_page.get_description_product()
    palabra_buscada = "Filter"
    # Verificar si la palabra está en la lista
    encontrada = False
    for lista in lista_principal:
        if palabra_buscada in lista:
            encontrada = True
            break
    assert encontrada == True, f"The part type '{palabra_buscada}' is not in the list"

#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9037_searchBar_autosuggestions(web_drivers):
    # MXTEST-9037 SearchBar_Autosuggestions
    #Verify that the system provides autosuggestions as the user types in the search bar, making it easier to find relevant results.
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    search_criteria = "Balat"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    suggestion_list = home_page.get_suggestion_list()
    assert len(suggestion_list) > 0 and home_page.element("highlight_search_result").wait_visible(), f"The search {search_criteria} didn't have results or there were no highlighted elements visible"


#@pytest.mark.pruebitas
@pytest.mark.sprint2_regression
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9035_searchBar_invalid_search_term(web_drivers):
    # MXTEST-9035 SearchBar_Invalid_Search Term
    #Verify that the system handles and displays no results when an invalid search term is entered in the search bar field.
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # -----------------------------------
    search_criteria = "#$$$$"
    expected_message = "Lo sentimos, no se encontraron resultados."
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    actual_message = home_page.get_no_results_message()
    assert actual_message == expected_message, f"El mensaje actual deberia ser: {expected_message}, en vez de {actual_message}"


@pytest.mark.sprint2_regression
#@pytest.mark.pruebitas
@pytest.mark.flaky(reruns=2)
def test_MXTEST_9031_searchBar_keywords_search(web_drivers):
    #Verify that the system returns relevant search results when keywords are used in the search bar
    # MXTEST-9031 SearchBar_Keywords_search
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    search_criteria = "Air"
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"Relevant search: {search_criteria.upper()} was not found in {producto}"
    assert len(lista_productos) > 0, f"The relevant search {search_criteria} didn't have results"













