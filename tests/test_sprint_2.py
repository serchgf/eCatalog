import logging
import os
import pathlib
import time
import json

import pytest

from src.page_objects.home_page import HomePage

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")

# HOME PAGE-------------------------------------------------------------------------------------------------------------
# MXTEST-8263
# sprint1_regression
# @pytest.mark.homepage
# def test_Vehicle_Filtering_Functionality_Validation(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(5)
#     home_page.click_on_Picker_vehicle_btn()
#     home_page.click_on_vehicle_type_and_select()
#     year = home_page.click_on_year_and_select()
#     make = home_page.click_on_make_and_select()
#     home_page.click_on_model_and_select()
#     home_page.click_on_submodel_and_select()
#     home_page.click_on_engine_and_select()
#     home_page.click_on_add_vehicle_submit_btn()
#     expected_vehicle_selected = f"{year} {make}"
#     vehicle_selected = home_page.get_vehicle_selected()
#     assert vehicle_selected in expected_vehicle_selected, f"Button must shows:{expected_vehicle_selected}"
#     #home_page.click_on_categories_button_and_select()
#     # Realizar consulta a la base de datos
#     # home_page.connect_and_consult() consultas no requeridas

# MXTEST-8282
# sprint1_regression
# @pytest.mark.homepage
# def test_Garage_Garage_Vehicle_Limit(web_drivers):
#     # se necesita actualizar el jira, el Maximo permitido en la lista es de 15 en vez de 10
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(3)
#     logging.info(f"FIRST Iteration----------------------------------------------------------------")
#     home_page.click_on_Picker_vehicle_btn()
#
#     vehicles_list = []
#     for index in range(15):
#         logging.info(f"{index} Iteration----------------------------------------------------------------")
#         vehicle = home_page.click_on_vehicle_type_and_select(index)
#         home_page.click_on_year_and_select(index)
#         home_page.click_on_make_and_select()
#         home_page.click_on_model_and_select()
#         home_page.click_on_submodel_and_select()
#         home_page.click_on_engine_and_select()
#         home_page.click_on_add_vehicle_submit_btn()
#         default_message = "Add vehicle"
#         vehicle_selected = home_page.get_vehicle_selected()
#         assert vehicle_selected != default_message, f"The button name: {vehicle_selected} must be different of{default_message}"
#         home_page.click_on_Picker_vehicle_btn()
#         vehicles_list.append(vehicle)
#         home_page.click_on_add_new_vehicle_btn()
#
#     n_vehicles = home_page.get_recent_vehicles_list()
#     logging.info(f"{vehicles_list}")
#     assert n_vehicles <= 15, "The number of vehicles listed must be Maximum '15'"
#     logging.info(f"{n_vehicles}: are listed")
#
# MXTEST-8284
# sprint1_regression
# @pytest.mark.homepage
# def test_Garage_Edit_Vehicle(web_drivers):
#     # se necesita actualizar el tc en jira, los campos que se pueden editar son submodel y Engine
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(3)
#     home_page.click_on_Picker_vehicle_btn()
#     vehicle = "Automotive Light Duty"
#
#     home_page.send_text_vehicle_type(vehicle)
#     home_page.click_on_year_and_select()
#     home_page.click_on_make_and_select()
#     home_page.click_on_model_and_select()
#     submodel = home_page.click_on_submodel_and_select()
#     engine = home_page.click_on_engine_and_select()
#     home_page.click_on_add_vehicle_submit_btn()
#     default_message = "Add vehicle"
#     vehicle_selected = home_page.get_vehicle_selected()
#     assert vehicle_selected != default_message, f"The button name: {vehicle_selected} must be different of {default_message}"
#     home_page.click_on_Picker_vehicle_btn()
#     home_page.take_screenshot("Original vehicle details")
#     home_page.click_on_edit_info_btn()
#     expected_submodel = home_page.new_submodel_and_select(submodel)
#     expected_engine = home_page.new_engine_and_select(engine)
#     home_page.click_on_save_changes_btn()
#     label_submodel, label_engine = home_page.get_text_label_vehicle_selected()
#     time.sleep(3)
#     logging.info(f"\nvehicle:{vehicle}\nOriginal Submodel:{submodel}\nOriginal Engine:{engine}")
#     assert expected_submodel in label_submodel, f"The submodel displayed:{label_submodel} should be in: {expected_submodel}"
#     assert expected_engine == label_engine, f"The engine displayed:{label_engine} should be: {expected_engine}"
#
#     logging.info(
#         f"Vehicle Edited successful")
#     logging.info(f"\nOriginal Submodel:{submodel} -> {expected_submodel}\nOriginal Engine:{engine} -> {expected_engine}")

# MXTEST-8285
# sprint1_regression
# @pytest.mark.homepage
# def test_Garage_Remove_Vehicle(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(3)
#     home_page.click_on_Picker_vehicle_btn()
#     vehicles_list = []
#     time.sleep(3)
#     for index in range(4):
#         logging.info(f"Iteration---------------------------------------------------------------- {index}")
#         vehicle = home_page.click_on_vehicle_type_and_select(index)
#         home_page.click_on_year_and_select(index)
#         home_page.click_on_make_and_select()
#         home_page.click_on_model_and_select()
#         home_page.click_on_submodel_and_select()
#         home_page.click_on_engine_and_select()
#         home_page.click_on_add_vehicle_submit_btn()
#         default_message = "Add vehicle"
#         vehicle_selected = home_page.get_vehicle_selected()
#         assert vehicle_selected != default_message, f"The button name: {vehicle_selected} must be different of{default_message}"
#         home_page.click_on_Picker_vehicle_btn()
#         vehicles_list.append(vehicle)
#         home_page.click_on_add_new_vehicle_btn()
#
#     n_vehicles = home_page.get_recent_vehicles_list()
#     logging.info(f"{vehicles_list}")
#     #assert n_vehicles <= 4, "The number of vehicles listed must be Maximum '15'"
#     logging.info(f"{n_vehicles}: are listed")
#     # click en el boton de clear
#     home_page.click_on_deleteAll_btn()
#     assert home_page.validate_vehicle_list_cleared(), "The vehicles are not cleared correctly, 'Add vehicle info' should be Visible"


# # MXTEST-8287
# sprint1_regression
# @pytest.mark.homepage
# def test_Garage_Category_Navigation(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     #time.sleep(3)
#     home_page.click_on_categories_button()
#     category_list = home_page.get_general_categories_list()
#     # click en categoria random
#     category_selected = home_page.select_random_element_of_list(category_list)
#
#     logging.info(f"category selected: {category_selected}")
#     # obtener lista de subcategorias
#     subcategory_list = home_page.get_subcategory_list()
#     if len(subcategory_list)<1:
#         subcategory_list = home_page.get_subcategory_list()
#     # click en subcategoria random
#     subcategory_selected = home_page.select_random_element_of_list(subcategory_list)
#     logging.info(f"Subcategory selected: {subcategory_selected}")
#     actual_parent_category = home_page.click_first_parent_category_on_breadcrumb()
#     assert category_selected == actual_parent_category, f"The actual parent category: {actual_parent_category}, should be: {category_selected}"
#     assert home_page.validate_parent_category_list_page()

# MXTEST-8271
# sprint1_regression
# @pytest.mark.homepage
# def test_Last_Viewed_Products(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(5)
#     expected_product_selected_list = []
#     lasted_viewed_list = []
#     # CICLO DE 3 O 5 VECES
#     home_page.wait_until_page_load_complete()
#     logging.info(f"Click categorie button*****************")
#     home_page.click_on_categories_button()
#     home_page.javascript_clic("Accessories")
#     subcat_1_list_2 = home_page.get_product_list_2()
#     home_page.click_element_text_of_list(subcat_1_list_2, "Exterior Accessories")
#     subcat_2_list_2 = home_page.get_product_list_2()
#     home_page.click_element_text_of_list(subcat_2_list_2, "Canopy And Tent")
#     home_page.wait_search_results_label()
#     product_list = home_page.get_link_product_list(0)
#     expected_product_selected = home_page.select_random_element_of_list(product_list)
#     product_selected = home_page.clean_product_selected(expected_product_selected)
#     logging.info(f"Selected: {product_selected}")
#     expected_product_selected_list.append(product_selected)
#     time.sleep(2)
#     for i in range(4):
#         home_page.back_to_previous_page()
#         product_list = home_page.get_link_product_list(0)
#         expected_product_selected = home_page.select_random_element_of_list(product_list)
#         product_selected = home_page.clean_product_selected(expected_product_selected)
#         logging.info(f"Selected: {product_selected}")
#         expected_product_selected_list.append(product_selected)
#         time.sleep(1)
#
#     home_page.click_on_logo_oreily_home()
#
#     logging.info(f"Recent Products expected list:")
#     home_page.show_product_list(expected_product_selected_list)
#
#     logging.info(f"GET actual lasted viewed products list")
#     lasted_product_viewed_list = home_page.get_lasted_viewed_products_list()
#
#     for lasted_viewed_product in lasted_product_viewed_list:
#         if lasted_viewed_product != '':
#             lasted_viewed_list.append(lasted_viewed_product)
#     #
#     logging.info(f"lasted_viewed_list: {lasted_viewed_list}")
#     logging.info(f"expected_product_selected_list: {expected_product_selected_list}")
#     assert lasted_viewed_list.sort() == expected_product_selected_list.sort()


# MXTEST-8290
# sprint1_regression
# @pytest.mark.homepage
# def test_Footer_Validation_Tool_section_elements(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.scroll_down()
#
#     data = home_page.cargar_json_data(_JSON_PATH)
#     expected_data = data['footer_href_links']
#     logging.info(f"Expected data: {expected_data}")
#
#     actual_name_href_dic = home_page.get_footer_links_name_href_dict()
#     ### logging.info(f"ACTUAL data: {actual_name_href_dic['Delivery routes Jalisco']}")
#
#     assert expected_data == actual_name_href_dic, f"Link names and url: {actual_name_href_dic},\n should be: {expected_data}"
# HOME PAGE-------------------------------------------------------------------------------------------------------------

# BRAND NAVIGATION------------------------------------------------------------------------------------------------------
# # MXTEST-8255, MXTEST-8266
# sprint1_regression
# @pytest.mark.brandNavigation
# def test_search_single_brand_without_vehicle_selected(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     # CLIC BRANDS DROPDOWN
#     home_page.click_on_brands()
#     # CLIC SHOW ALL BRANDS LINK TEXT
#     home_page.click_on_show_all_brands()
#     # click on any brand
#     home_page.get_random_brand()
#
#     # # get number of elements
#     search_results_number = home_page.get_search_results_number()
#
#     logging.info(f"Search results number: {search_results_number}")
#


# # MXTEST-8265, MXTEST-8267
# sprint1_regression
# @pytest.mark.brandNavigation
# def test_search_all_brands_vehicle_selected(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#
#     home_page.click_on_Picker_vehicle_btn()
#     time.sleep(2)
#     home_page.click_on_vehicle_type_and_select()
#
#     year = home_page.click_on_year_and_select()
#     make = home_page.click_on_make_and_select()
#     print(f"make es:{make}")
#     home_page.click_on_model_and_select()
#     home_page.click_on_submodel_and_select()
#     home_page.click_on_engine_and_select()
#     home_page.click_on_add_vehicle_submit_btn()
#     expected_vehicle_selected = f"{year} {make}"
#     vehicle_selected = home_page.get_vehicle_selected()
#     assert vehicle_selected.upper() in expected_vehicle_selected.upper(), f"The button must shows: {expected_vehicle_selected}\n in: {vehicle_selected} on the button."
#     # CLIC BRANDS DROPDOWN
#     home_page.click_on_brands()
#     # CLIC SHOW ALL BRANDS LINK TEXT
#     home_page.click_on_show_all_brands()
#     # click on any brand
#     home_page.get_random_brand()
#     # # get number of elements
#     search_results_number = home_page.get_search_results_number()
#     assert search_results_number > 0, "No elements displayed"
#
#     logging.info(f"Search results number: {search_results_number}")
#

# MODAL NAVIGATION------------------------------------------------------------------------------------------------------

# # MXTEST-8257
# sprint1_regression
# @pytest.mark.modalNavigation
# def test_Popular_Categories(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     home_page.click_on_categories_button()
#     popular_category_list = home_page.get_popular_category_list()
#     expected_len_popopular_category_list = 12
#     logging.info("Validation the number of categories in the 'Categorias populares' section")
#     assert len(popular_category_list) == expected_len_popopular_category_list, f"Number of popular categories must be: '{expected_len_popopular_category_list}' instead of '{len(popular_category_list)}'."
#

# # MXTEST-8273
# sprint1_regression
# @pytest.mark.modalNavigation
# def test_GoBackButton(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     home_page.click_on_categories_button()
#     general_category_list = home_page.get_general_categories_list()
#     home_page.select_random_element_of_list(general_category_list)
#     home_page.click_on_goBack_btn()
#
#     logging.info("Validate presence of 'POPULAR CATEGORIES' label in modal")
#     assert home_page.presenceOf_popular_categories_label(), f"'POPULAR CATEGORIES' label has not been displayed."
#

# # MXTEST-8274
# sprint1_regression
# @pytest.mark.modalNavigation
# def test_PopupClose_Button(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(3)
#     home_page.wait_until_page_load_complete()
#     home_page.click_on_categories_button()
#     home_page.close_categories()


# EQUIVALENTS-----------------------------------------------------------------------------------------------------------

# # MXTEST-8256
# sprint1_regression
# @pytest.mark.equivalents
# def test_Search_Compatible(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     home_page.click_on_part_interchange_btn()
#     part_1 = "25455"
#     home_page.write_part_in_interchange_tbx(part_1)
#     home_page.click_part_interchange_search_btn()
#
#     # get part type list of step 2
#     step_2_part_type_list_1 = home_page.get_part_interchange_step_2_list()
#     home_page.show_product_list(step_2_part_type_list_1)
#


# # MXTEST-8276
# sprint1_regression
# @pytest.mark.equivalents
# def test_ChangeSearchedNumber(web_drivers):

#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     home_page.click_on_part_interchange_btn()
#     part_1 = "25455"
#     home_page.write_part_in_interchange_tbx(part_1)
#     home_page.click_part_interchange_search_btn()
#     # get part type list of step 2
#     step_2_part_type_list_1 = home_page.get_part_interchange_step_2_list()
#     # click a part type of the list
#     part_type_selected = home_page.select_random_element_of_list(step_2_part_type_list_1)
#     logging.info(f"Part Type selected: {part_type_selected}")
#
#     home_page.clear_part_interchange_input_tbx()
#
#     part_2 = "12587"
#     home_page.write_part_in_interchange_tbx(part_2)
#     home_page.click_part_interchange_search_btn()
#     step_2_part_type_list_2 = home_page.get_part_interchange_step_2_list()
#
#     assert step_2_part_type_list_1 != step_2_part_type_list_2, "List 1 displayed must be different of list 2"
#

# # MXTEST-8277
# sprint1_regression
# @pytest.mark.equivalents
# def test_Search_WrongNumber(web_drivers):

#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     home_page.click_on_part_interchange_btn()
#     part = "999999999999"
#     home_page.write_part_in_interchange_tbx(part)
#
#     home_page.click_part_interchange_search_btn()
#     expected_message1 = "NO RESULTS FOUND"
#     expected_message2 = "Please, type in a new part number."
#     actual_message = home_page.get_no_results_found_message()
#     logging.info(f"VALIDATING CORRECT MESSAGE RESULT")
#     assert expected_message1 in actual_message, f"The message should contains: {expected_message1}"
#     assert expected_message2 in actual_message, f"The message should contains: {expected_message2}"

# # MXTEST-8280
# sprint1_regression
# @pytest.mark.equivalents
# def test_Search_PopupClose_Button(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     home_page.click_on_part_interchange_btn()
#     part = "20123"
#     home_page.write_part_in_interchange_tbx(part)
#     home_page.clic_outside_of_modal_window()
#     home_page.click_on_part_interchange_btn()
#     home_page.close_part_interchange()
#     home_page.click_on_part_interchange_btn()
#

# # MXTEST-8283
# sprint1_regression
# @pytest.mark.equivalents
# def test_Search_FromProductPage(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.wait_until_page_load_complete()
#     product = "wheel adapter"
#     home_page.search_product(product)
#     #get product list
#
#     home_page.wait_search_results_label()
#     product_list = home_page.get_link_product_list()
#     product_selected = home_page.select_random_element_of_list(product_list)
#     logging.info(f"Product Selected: {product_selected}")
#     part_number = home_page.get_part_number()
#     home_page.click_on_part_interchange_btn()
#     logging.info(f"Validate Part number: {part_number}")
#     actual_text = home_page.get_text_part_interchange_input()
#     logging.info(f"Validate ACTUAL Part number: {actual_text}")
#     assert actual_text == part_number, f"The part number should be: {part_number} instead of {actual_text}"


# PDP-------------------------------------------------------------------------------------------------------------------

# # MXTEST-8275
# sprint1_regression# sprint1_regression
# @pytest.mark.pdp
# def test_Compatibility_Vehicle_selected(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.click_on_brands()
#     # CLIC SHOW ALL BRANDS LINK TEXT
#     home_page.click_on_show_all_brands()
#     # click on any brand
#     home_page.get_random_brand()
#     product_list = home_page.get_link_product_list()
#     product_selected = home_page.select_random_element_of_list(product_list)
#     logging.info(f"Product Selected: {product_selected}")
#     home_page.click_on_Picker_vehicle_btn()
#     year = home_page.click_on_year_and_select()
#     make = home_page.click_on_make_and_select()
#     home_page.click_on_model_and_select()
#     home_page.click_on_submodel_and_select()
#     home_page.click_on_engine_and_select()
#
#     home_page.click_on_add_vehicle_submit_btn()
#     expected_message = "Does NOT Fit"
#     expected_message_2 = "Non application"
#     expected_message_2 = "Fits"
#     actual_message = home_page.get_does_not_fit_meessage()
#     assert expected_message in actual_message or expected_message_2 in actual_message, f"The message {actual_message} should be: {expected_message} or {expected_message_2}"

# # MXTEST-8286
# sprint1_regression
# @pytest.mark.pdp
# def test_DirectLink_CompatibilityError_SelectVehicle(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     url = "https://testintranet.oreillyauto.mx/ecatalog-us/#/catalog/c/oil-chemicals-fluids/motor-oil/motor-oil-vehicle-specific/l/07065/detail/red-line-full-synthetic-motor-oil-0w-30-1-quart-11114/rl00/11114"
#     home_page.open_new_url(url)
#     home_page.click_check_vehicle_fit_btn()
#     home_page.write_a_vehicle_type("Agricultural Equipment")
#     home_page.write_a_year("2019")
#     home_page.write_a_make("AGCO")
#     home_page.write_a_model("5650")
#     home_page.write_a_submodel("Base")
#     home_page.write_a_engine("GENERIC")
#     home_page.click_on_add_vehicle_submit_btn()
#     expected_message = "Does NOT Fit"
#     actual_message = home_page.get_does_not_fit_meessage()
#     assert expected_message in actual_message, f"The message {actual_message} should be: {expected_message}"
#


#
# # # MXTEST-8289
# sprint1_regression
# @pytest.mark.pdp
# def test_DirectLink_CompatibilityError_PreselectedVehicle(web_drivers):
#     # falta dato URL: https://testintranet.oreillyauto.mx/ecatalog/<<ID DEL ARTICULO >>
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     home_page.click_on_Picker_vehicle_btn()
#     home_page.write_a_vehicle_type("Agricultural Equipment")
#     home_page.write_a_year("2019")
#     home_page.write_a_make("AGCO")
#     home_page.write_a_model("5650")
#     home_page.write_a_submodel("Base")
#     home_page.write_a_engine("GENERIC")
#     home_page.click_on_add_vehicle_submit_btn()
#     url = "https://testintranet.oreillyauto.mx/ecatalog-us/#/catalog/c/oil-chemicals-fluids/motor-oil/motor-oil-vehicle-specific/l/07065/detail/red-line-full-synthetic-motor-oil-0w-30-1-quart-11114/rl00/11114"
#     home_page.open_new_url(url)
#     expected_message = "Does NOT Fit"
#
#     actual_message = home_page.get_does_not_fit_meessage()
#
#     assert expected_message in actual_message, f"The message {actual_message} should be: {expected_message}"


# AUTO FILL OPTION------------------------------------------------------------------------------------------------------

# # MXTEST-8292
# sprint1_regression
# @pytest.mark.autofilloption
# def test_AutofillOption_FreeTextSearchBar(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     word = "eng"
#     print(f"Search word: {word} and select a suggest result")
#     home_page.search_product(word)
#     home_page.take_screenshot("test_AutofillOption_FreeTextSearchBar")
#


# NEW CLIENT------------------------------------------------------------------------------------------------------------

# # MXTEST-8291
# sprint1_regression
# @pytest.mark.newclient
# def test_NewClient_CallWindow(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(4)
#     home_page.shortcut_new_client()
#     home_page.click_new_client_continue_btn()
#     home_page.click_on_categories_button()
#
#     home_page.click_on_category_by_text("Oil, Chemicals & Fluids")
#     home_page.click_on_subcategory_by_text("Motor Oil")
#
#     home_page.shortcut_new_client()
#     home_page.click_new_client_cancel_btn()
#     product_list = home_page.get_link_product_list(1)
#     product = "Motor Oil - Full Synthetic"
#     for prod in product_list:
#         if prod.text == product:
#             prod.click()
#             break
#
#     home_page.shortcut_new_client()
#     #step 11
#     home_page.click_new_client_cancel_btn()
#     # 12 click first element on the list
#     product_list = home_page.get_link_product_list()
#     home_page.click_on_specific_index_on_list_element(product_list, 0)
#     # step 13
#     home_page.shortcut_new_client()
#     # step 14
#     home_page.click_new_client_cancel_btn()
#     # step 15 click on brands
#     home_page.click_on_brands()
#     # step 16 click en show all brands
#     home_page.click_on_show_all_brands()
#     #step 17
#     home_page.shortcut_new_client()
#     # step 18
#     home_page.click_new_client_cancel_btn()
#
#     home_page.wait_until_page_load_complete()

# PLP-------------------------------------------------------------------------------------------------------------------

# # MXTEST-8258
# sprint1_regression
# @pytest.mark.plp
# def test_PLP_Search_with_Selected_Vehicle(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#
#     home_page.click_on_Picker_vehicle_btn()
#     time.sleep(4)
#     vehicle_type_list = home_page.click_on_vehicle_type_dropdown()
#     vehicle_type = "Automotive Light Duty"
#     home_page.click_element_text_of_list(vehicle_type_list, vehicle_type)
#     home_page.click_on_year_and_select()
#     home_page.click_on_make_and_select()
#     home_page.click_on_model_and_select()
#     home_page.click_on_submodel_and_select()
#     home_page.click_on_engine_and_select()
#     home_page.click_on_add_vehicle_submit_btn()
#     home_page.click_on_brands()
#     home_page.click_on_show_all_brands()
#     home_page.get_random_brand()
#     product_list = home_page.get_link_product_list(0)
#     home_page.show_product_list(product_list)
#     home_page.take_screenshot("test_PLP_Search_with_Selected_Vehicle")

# # MXTEST-8259
@pytest.mark.ecatalog_demo
# sprint1_regression
# @pytest.mark.plp
def test_PLP_Search_filter_No_results_found(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    wrong_product_name = "MOTTOR OIL"
    home_page.search_wrong_product_name(wrong_product_name)
    expected_message = "We're sorry, no results were found"
    actual_message = home_page.get_no_results_message()
    assert actual_message == expected_message, f"the message displayed shoeld be: {expected_message} instead of: {actual_message}"
    home_page.take_screenshot("test_PLP_Search_filter_No_results_found")

# # MXTEST-8260
# sprint1_regression
# @pytest.mark.ecatalog_demo
# @pytest.mark.plp
# def test_PLP_Search_without_vehicle_selected(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     product_name = "Motor Oil"
#     home_page.search_product(product_name)
#     product_list = home_page.get_link_product_list(1)
#     for product in product_list:
#         assert product_name.upper() in product.text.upper(), f"'{product_name.upper()}' must appears in description product, but has: {product.text.upper()}"
#

# # MXTEST-8262
# sprint1_regression
# @pytest.mark.plp
# @pytest.mark.ecatalog_demo
# def test_PLP_Navigation_Categories(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(5)
#     home_page.click_on_categories_button()
#     category_list = home_page.get_general_categories_list()
#     # click en categoria random
#     category_selected = home_page.select_random_element_of_list(category_list)
#
#     logging.info(f"category selected: {category_selected}")
#     # obtener lista de subcategorias
#     subcategory_list = home_page.get_subcategory_list()
#     home_page.select_random_element_of_list(subcategory_list)
#     home_page.wait_until_page_load_complete()
#     home_page.take_screenshot("test_PLP_Navigation_Categories")

# # MXTEST-8264 mod1 without vehicle selected
# sprint1_regression
# @pytest.mark.plp
# def test_PLP_Sort_by_option_az(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#
#     home_page.wait_until_page_load_complete()
#     product_name = "Skid Plate"
#     home_page.search_product(product_name)
#     # obtener lista original
#     product_list = home_page.get_link_product_list(0)
#     product_list_text = []
#     original_first_char = ''
#     for product in product_list:
#         description = product.text.split('\n')
#         product_description = description[1].split("-")
#         product_list_text.append(product_description[0])
#         original_first_char = product_description[0][0]
#         break
#     print("Primer caracter original")
#     print(original_first_char)
#
#
#     # ordenar con filter by de a-z
#     home_page.click_order_by_dropdown_and_select_option("A - Z")
#     home_page.wait_until_page_load_complete()
#     # obtener lista ordenada de a-z
#     az_product_list = home_page.get_link_product_list(0)
#     az_product_list_text = []
#     az_first_char=''
#     for product in az_product_list:
#         description = product.text.split('\n')
#         product_description = description[1].split("-")
#         az_product_list_text.append(product_description[0])
#         az_first_char = product_description[0][0]
#         break
#     print("primer caracter obtenido")
#     print(az_first_char)
#     assert az_first_char <= original_first_char, f"{az_first_char} should be <= {original_first_char}"
#     home_page.take_screenshot("test_PLP_Sort_by_option_az")


# MXTEST-8264 mod1 with vehicle selected
# sprint1_regression
# @pytest.mark.plp
# def test_PLP_Sort_by_option_az_vehicle_selected(web_drivers):
#     home_page = HomePage(*web_drivers)
#     url = "https://testintranet.oreillyauto.mx/ecatalog-us/#/catalog/c/oil-chemicals-fluids/motor-oil/motor-oil-full-synthetic/l/n2728"
#     home_page.open_new_url(url)
#
#     home_page.wait_until_page_load_complete()
#     product_name = "Skid Plate"
#     home_page.search_product(product_name)
#     # obtener lista original
#     product_list = home_page.get_link_product_list(0)
#     product_list_text = []
#     original_first_char = ''
#     for product in product_list:
#         description = product.text.split('\n')
#         product_description = description[1].split("-")
#         product_list_text.append(product_description[0])
#         original_first_char = product_description[0][0]
#         break
#     print("Primer caracter original")
#     print(original_first_char)
#
#
#     # ordenar con filter by de a-z
#     home_page.click_order_by_dropdown_and_select_option("A - Z")
#     home_page.wait_until_page_load_complete()
#     # obtener lista ordenada de a-z
#     az_product_list = home_page.get_link_product_list(0)
#     az_product_list_text = []
#     az_first_char=''
#     for product in az_product_list:
#         description = product.text.split('\n')
#         product_description = description[1].split("-")
#         az_product_list_text.append(product_description[0])
#         az_first_char = product_description[0][0]
#         break
#     print("primer caracter obtenido")
#     print(az_first_char)
#     assert az_first_char <= original_first_char, f"{az_first_char} should be <= {original_first_char}"
#     home_page.take_screenshot("test_PLP_Sort_by_option_az")


# # MXTEST-8264 mod2
# sprint1_regression
# @pytest.mark.plp
# def test_PLP_Sort_by_option_za(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#
#     home_page.wait_until_page_load_complete()
#     product_name = "Skid Plate"
#     home_page.search_product(product_name)
#     # obtener lista original
#     product_list = home_page.get_link_product_list(0)
#     product_list_text = []
#     original_first_char = ''
#     for product in product_list:
#         description = product.text.split('\n')
#         product_description = description[1].split("-")
#         product_list_text.append(product_description[0])
#         original_first_char = product_description[0][0]
#         break
#     print("Primer caracter original")
#     print(original_first_char)
#
#     # ordenar con filter by de a-z
#     home_page.click_order_by_dropdown_and_select_option("Z - A")
#     home_page.wait_until_page_load_complete()
#     # obtener lista ordenada de a-z
#     za_product_list = home_page.get_link_product_list(0)
#     za_product_list_text = []
#     za_first_char = ''
#     for product in za_product_list:
#         description = product.text.split('\n')
#         product_description = description[1].split("-")
#         za_product_list_text.append(product_description[0])
#         za_first_char = product_description[0][0]
#         break
#     print("primer caracter obtenido")
#     print(za_first_char)
#     assert za_first_char >= original_first_char, f"{za_first_char} should be <= {original_first_char}"
#     home_page.take_screenshot("test_PLP_Sort_by_option_za")

# # MXTEST-8264 mod3
# sprint1_regression
# @pytest.mark.plp
# def test_PLP_Sort_by_option_relevance(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#
#     home_page.wait_until_page_load_complete()
#     product_name = "Skid Plate"
#     home_page.search_product(product_name)
#
#     # ordenar con filter by relevance
#     home_page.click_order_by_dropdown_and_select_option("Relevance")
#     home_page.wait_until_page_load_complete()
#
#     # obtener lista ordenada por relevance
#     relevance_product_list = home_page.get_link_product_list(0)
#     home_page.take_screenshot("before of order by relevance")
#     relevance_product_list_text = []
#     relevance_first_part_number = ''
#     for product in relevance_product_list:
#         description = product.text.split('\n')
#         # print(f"DESCRIPTION 0: {description[1]}")
#         description_aux = description[1].split('-')
#         # print(f"DESCRIPTION AUX: {description_aux}")
#         # print(f"DESCRIPTION AUX[0]: {description_aux[0]}")
#         # print(f"DESCRIPTION AUX[1]: {description_aux[1]}")
#         relevance_first_part_number = description_aux[1].lstrip()
#         relevance_product_list_text.append(int(relevance_first_part_number))
#     # print("relevance")
#     # print(relevance_product_list_text)
#     # print("sorted")
#     # print(sorted(relevance_product_list_text))
#     assert relevance_product_list_text == sorted(relevance_product_list_text), f"part number in ascending order: {relevance_product_list_text} \nshould be: {sorted(relevance_product_list_text)}"
#
#     home_page.take_screenshot("after of order by relevance")