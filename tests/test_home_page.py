import logging
import os
import pathlib
import time
import json

import pytest
from selenium.common.exceptions import NoSuchElementException


from src.page_objects.home_page import HomePage


_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")

# HOME PAGE-------------------------------------------------------------------------------------------------------------
# MXTEST-8263
@pytest.mark.sprint1_regression
@pytest.mark.pruebitas
#@pytest.mark.homepage
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8263_Vehicle_Filtering_Functionality_Validation(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_Picker_vehicle_btn()
    time.sleep(.2)
    print("Paso agregar vehiculo")
    #Seleccionar tipo de vehiculo
    home_page.click_on_vehicle_type_and_select()
    #Seleccionar año
    year = home_page.click_on_year_and_select()
    #Seleccionar marca
    make = home_page.click_on_make_and_select()
    #Seleccionar modelo
    home_page.click_on_model_and_select()
    #Seleccionar submodelo
    home_page.click_on_submodel_and_select()
    #Seleccionar motor
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    expected_vehicle_selected = f"{year} {make}"
    vehicle_selected = home_page.get_vehicle_selected()
    assert vehicle_selected in expected_vehicle_selected, f"Button must shows:{expected_vehicle_selected}"
    #home_page.click_on_categories_button_and_select()
    # Realizar consulta a la base de datos
    # home_page.connect_and_consult() consultas no requeridas
# #
# # MXTEST-8282
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.homepage
@pytest.mark.flaky(reruns=1)
#@pytest.mark.fallo
def test_MXTEST_8282_Garage_Garage_Vehicle_Limit(web_drivers):
    # se necesita actualizar el jira, el Maximo permitido en la lista es de 15 en vez de 10
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    logging.info(f"FIRST Iteration----------------------------------------------------------------")
    home_page.click_on_Picker_vehicle_btn()
    time.sleep(3)
    vehicles_list = []
    for index in range(15):
        logging.info(f"{index} Iteration----------------------------------------------------------------")
        vehicle = home_page.click_on_vehicle_type_and_select(index)# tenia 0
        home_page.click_on_year_and_select(1)
        home_page.click_on_make_and_select()
        home_page.click_on_model_and_select()
        home_page.click_on_submodel_and_select()
        home_page.click_on_engine_and_select()
        home_page.click_on_add_vehicle_submit_btn()
        default_message = "Add vehicle"
        vehicle_selected = home_page.get_vehicle_selected()
        assert vehicle_selected != default_message, f"The button name: {vehicle_selected} must be different of{default_message}"
        home_page.click_on_Picker_vehicle_btn()
        time.sleep(3)
        vehicles_list.append(vehicle)
        home_page.click_on_add_new_vehicle_btn()
        time.sleep(3)

    n_vehicles = home_page.get_recent_vehicles_list()
    logging.info(f"{vehicles_list}")
    assert n_vehicles <= 15, "The number of vehicles listed must be Maximum '15'"
    logging.info(f"{n_vehicles}: are listed")
#
# MXTEST-8284
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.homepage
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8284_Garage_Edit_Vehicle(web_drivers):
    # se necesita actualizar el tc en jira, los campos que se pueden editar son submodel y Engine
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_Picker_vehicle_btn()
    time.sleep(3)
    vehicle = "Deportes Motorizados"
    #
    # home_page.send_text_vehicle_type(vehicle)
    home_page.write_a_vehicle_type(vehicle)
    home_page.write_a_year("2020")
    home_page.write_a_make("Arctic Cat")
    home_page.write_a_model("Alterra 300")
    submodel = "Base"
    home_page.write_a_submodel(submodel)
    engine = home_page.click_on_engine_and_select()
    # # vehicle = "Automotive Light Duty"
    # #
    # # home_page.send_text_vehicle_type(vehicle)
    # vehicle = home_page.click_on_vehicle_type_and_select()
    # home_page.click_on_year_and_select()
    # home_page.click_on_make_and_select()
    # home_page.click_on_model_and_select()
    # submodel = home_page.click_on_submodel_and_select()
    # engine = home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    default_message = "Add vehicle"
    vehicle_selected = home_page.get_vehicle_selected()
    assert vehicle_selected != default_message, f"The button name: {vehicle_selected} must be different of {default_message}"
    home_page.click_on_Picker_vehicle_btn()
    home_page.take_screenshot("Original vehicle details")
    home_page.click_on_edit_info_btn()
    expected_submodel = home_page.new_submodel_and_select(submodel)

    expected_engine = home_page.new_engine_and_select(engine)
    home_page.click_on_save_changes_btn()
    label_submodel, label_engine = home_page.get_text_label_vehicle_selected()
    expected_submodel = label_submodel.replace("\nUSA","")
    print(f"Este es el label {label_submodel}")
    time.sleep(.2)
    logging.info(f"\nvehicle:{vehicle}\nOriginal Submodel:{submodel}\nOriginal Engine:{engine}")
    assert expected_submodel in label_submodel or expected_submodel in label_engine, f"{expected_submodel} debe encontarse en {label_submodel} o en {label_engine}"
    assert expected_engine in label_engine or expected_engine in label_submodel, f"{expected_engine} debe encontarse en {label_engine} o en {label_submodel}"
    logging.info(
       f"Vehicle Edited successful")
    logging.info(f"\nOriginal Submodel:{submodel} -> {expected_submodel}\nOriginal Engine:{engine} -> {expected_engine}")
    print("Hola")

# MXTEST-8285
@pytest.mark.sprint1_regression
@pytest.mark.test_8285
@pytest.mark.homepage
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8285_Garage_Remove_Vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_Picker_vehicle_btn()
    vehicles_list = []
    #home_page.wait_spinner_disappears()
    for index in range(3):
        logging.info(f"Iteration---------------------------------------------------------------- {index}")
        vehicle = home_page.click_on_vehicle_type_and_select(1)# tenia index
        home_page.click_on_year_and_select(1)# tenia index
        home_page.click_on_make_and_select()
        home_page.click_on_model_and_select()
        home_page.click_on_submodel_and_select()
        home_page.click_on_engine_and_select()
        home_page.click_on_add_vehicle_submit_btn()
        home_page.wait_spinner_disappears()
        default_message= " Agregar vehículo "
        vehicle_selected = home_page.get_vehicle_selected()
        assert vehicle_selected != default_message, f"The button name: {vehicle_selected} must be different of{default_message}"
        home_page.click_on_Picker_vehicle_btn()
        vehicles_list.append(vehicle)
        home_page.click_on_add_new_vehicle_btn()
        #home_page.wait_spinner_disappears()

    n_vehicles = home_page.get_recent_vehicles_list()
    logging.info(f"{vehicles_list}")
    #assert n_vehicles <= 4, "The number of vehicles listed must be Maximum '15'"
    logging.info(f"{n_vehicles}: are listed")
    # click en el boton de clear
    home_page.click_on_deleteAll_btn()
    assert not home_page.validate_vehicle_list_cleared(), "The vehicles are not cleared correctly, 'recent_vehicles' should not be Visible"

#
# # # MXTEST-8287
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.homepage
@pytest.mark.flaky(reruns=1)
#@pytest.mark.fallo
def test_MXTEST_8287_Garage_Category_Navigation(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_categories_button()
    home_page.wait_until_page_load_complete()
    category_list = home_page.get_general_categories_list()
    # click en categoria random
    category_selected = home_page.select_random_element_of_list(category_list)
    print(f"Se selecciono {category_selected}")
    time.sleep(.2)
    logging.info(f"category selected: {category_selected}")
    # obtener lista de subcategorias
    subcategory_list = home_page.get_subcategory_list()
    if len(subcategory_list)<1:
        subcategory_list = home_page.get_subcategory_list()
    # click en subcategoria random
    subcategory_selected = home_page.select_random_element_of_list(subcategory_list)
    logging.info(f"Subcategory selected: {subcategory_selected}")
    print(f"Se selecciono {subcategory_selected}")
    actual_parent_category = home_page.click_first_parent_category_on_breadcrumb()
    assert category_selected.upper() == actual_parent_category, f"The actual parent category: {actual_parent_category}, should be: {category_selected}"
    assert home_page.validate_parent_category_list_page()
#
# # MXTEST-8271
@pytest.mark.sprint1_regression
@pytest.mark.homepage
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8271_Last_Viewed_Products(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    expected_product_selected_list = []
    lasted_viewed_list = []
    # CICLO DE 3 O 5 VECES
    home_page.wait_until_page_load_complete()
    logging.info(f"Click categorie button*****************")
    home_page.click_on_categories_button()
    time.sleep(1)
    home_page.javascript_clic("Accessories")
    subcat_1_list_2 = home_page.get_product_list_2()
    home_page.click_element_text_of_list(subcat_1_list_2, "Interior Accessories")
    subcat_2_list_2 = home_page.get_product_list_2()
    home_page.click_element_text_of_list(subcat_2_list_2, "Air Fresheners")
    home_page.wait_search_results_label()
    product_list = home_page.get_link_product_list(0)
    expected_product_selected = home_page.select_random_element_of_list(product_list)
    product_selected = home_page.clean_product_selected(expected_product_selected)
    logging.info(f"Selected: {product_selected}")
    expected_product_selected_list.append(product_selected)
    time.sleep(2)
    for i in range(4):
        home_page.back_to_previous_page()
        product_list = home_page.get_link_product_list(0)
        expected_product_selected = home_page.select_random_element_of_list(product_list)
        product_selected = home_page.clean_product_selected(expected_product_selected)
        logging.info(f"Selected: {product_selected}")
        expected_product_selected_list.append(product_selected)
        time.sleep(3)

    home_page.click_on_logo_oreily_home()

    logging.info(f"Recent Products expected list:")
    home_page.show_product_list(expected_product_selected_list)

    logging.info(f"GET actual lasted viewed products list")
    lasted_product_viewed_list = home_page.get_lasted_viewed_products_list()

    for lasted_viewed_product in lasted_product_viewed_list:
        if lasted_viewed_product != '':
            lasted_viewed_list.append(lasted_viewed_product)
    #
    logging.info(f"lasted_viewed_list: {lasted_viewed_list}")
    logging.info(f"expected_product_selected_list: {expected_product_selected_list}")
    assert lasted_viewed_list.sort() == expected_product_selected_list.sort()

#
# # MXTEST-8290
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.homepage
@pytest.mark.flaky(reruns=1)
@pytest.mark.fallo
def test_MXTEST_8290_Footer_Validation_Tool_section_elements(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.scroll_down()

    data = home_page.cargar_json_data(_JSON_PATH)
    expected_data = data['footer_href_links']
    logging.info(f"Expected data: {expected_data}")

    actual_name_href_dic = home_page.get_footer_links_name_href_dict()
    ### logging.info(f"ACTUAL data: {actual_name_href_dic['Delivery routes Jalisco']}")

    assert expected_data == actual_name_href_dic, f"Link names and url: {actual_name_href_dic},\n should be: {expected_data}"
# # HOME PAGE-------------------------------------------------------------------------------------------------------------
#
# # BRAND NAVIGATION------------------------------------------------------------------------------------------------------
# # MXTEST-8255, MXTEST-8266
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.brandNavigation
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8255_MXTEST_8266_search_single_brand_without_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    # CLIC BRANDS DROPDOWN
    home_page.click_on_brands()
    time.sleep(2)
    # CLIC SHOW ALL BRANDS LINK TEXT
    home_page.click_on_show_all_brands()
    # click on any brand
    home_page.get_random_brand()
    # # get number of elements
    search_results_number = home_page.get_search_results_number()
    logging.info(f"Search results number: {search_results_number}")

# #
#
# # # MXTEST-8265, MXTEST-8267
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.brandNavigation
@pytest.mark.flaky(reruns=1)
#@pytest.mark.fallo
def test_MXTEST_8265_MXTEST_8267_search_all_brands_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    print(f"make es:{make}")
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    expected_vehicle_selected = f"{year} {make}"
    vehicle_selected = home_page.get_vehicle_selected()
    assert vehicle_selected.upper() in expected_vehicle_selected.upper(), f"The button must shows: {expected_vehicle_selected}\n in: {vehicle_selected} on the button."
    # CLIC BRANDS DROPDOWN
    home_page.click_on_brands()
    # CLIC SHOW ALL BRANDS LINK TEXT
    home_page.click_on_show_all_brands()
    home_page.wait_spinner_disappears()
    # click on any brand
    home_page.get_random_brand()
    # # get number of elements
    search_results_number = home_page.get_search_results_number()
    assert search_results_number > 0, "No elements displayed"

    logging.info(f"Search results number: {search_results_number}")

#
# # MODAL NAVIGATION------------------------------------------------------------------------------------------------------
#
# # # MXTEST-8257
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.modalNavigation
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8257_Popular_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_categories_button()
    time.sleep(3)
    popular_category_list = home_page.get_popular_category_list()
    expected_len_popopular_category_list = 12
    logging.info("Validation the number of categories in the 'Categorias populares' section")
    assert len(popular_category_list) == expected_len_popopular_category_list, f"Number of popular categories must be: '{expected_len_popopular_category_list}' instead of '{len(popular_category_list)}'."

#
# # # MXTEST-8273
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.modalNavigation
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8273_GoBackButton(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    home_page.click_on_categories_button()
    time.sleep(3)
    general_category_list = home_page.get_general_categories_list()
    home_page.select_random_element_of_list(general_category_list)
    time.sleep(3)
    home_page.click_on_goBack_btn()

    logging.info("Validate presence of 'POPULAR CATEGORIES' label in modal")
    assert home_page.presenceOf_popular_categories_label(), f"'POPULAR CATEGORIES' label has not been displayed."

#
# # # MXTEST-8274
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.modalNavigation
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8274_PopupClose_Button(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    home_page.click_on_categories_button()
    time.sleep(3)
    home_page.close_categories()

#
# # EQUIVALENTS-----------------------------------------------------------------------------------------------------------
#
# # # MXTEST-8256
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.equivalents
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8256_Search_Compatible(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    home_page.click_on_part_interchange_btn()
    part_1 = "4598"
    home_page.write_part_in_interchange_tbx(part_1)
    home_page.click_part_interchange_search_btn()
    # get part type list of step 2
    step_2_part_type_list_1 = home_page.get_part_interchange_step_2_list()
    home_page.show_product_list(step_2_part_type_list_1)

# # # MXTEST-8276
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.equivalents
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8276_ChangeSearchedNumber(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_part_interchange_btn()
    part_1 = "2545"
    home_page.write_part_in_interchange_tbx(part_1)
    home_page.click_part_interchange_search_btn()
    # get part type list of step 2
    step_2_part_type_list_1 = home_page.get_part_interchange_step_2_list()
    # click a part type of the list
    part_type_selected = home_page.select_random_element_of_list(step_2_part_type_list_1)
    logging.info(f"Part Type selected: {part_type_selected}")
    home_page.clear_part_interchange_input_tbx()

    part_2 = "1258"
    home_page.write_part_in_interchange_tbx(part_2)
    home_page.click_part_interchange_search_btn()
    step_2_part_type_list_2 = home_page.get_part_interchange_step_2_list()
    assert step_2_part_type_list_1 != step_2_part_type_list_2, "List 1 displayed must be different of list 2"

#
# # # MXTEST-8277
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.equivalents
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8277_Search_WrongNumber(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    home_page.click_on_part_interchange_btn()
    part = "999999999999"
    home_page.write_part_in_interchange_tbx(part)

    home_page.click_part_interchange_search_btn()
    expected_message1 = "NO HAY RESULTADOS"
    expected_message2 = "Por favor, busca un nuevo número de parte."
    actual_message = home_page.get_no_results_container_message()
    # actual_message = home_page.get_no_results_found_message()
    logging.info(f"VALIDATING CORRECT MESSAGE RESULT")
    assert expected_message1 in actual_message, f"The message should contains: {expected_message1}"
    assert expected_message2 in actual_message, f"The message should contains: {expected_message2}"
#
# # # MXTEST-8280
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.equivalents
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8280_Search_PopupClose_Button(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_part_interchange_btn()
    part = "20123"
    home_page.write_part_in_interchange_tbx(part)
    home_page.clic_outside_of_modal_window()
    home_page.click_on_part_interchange_btn()
    home_page.close_part_interchange()
    home_page.click_on_part_interchange_btn()

#
# # # MXTEST-8283
@pytest.mark.sprint1_regression
@pytest.mark.equivalents
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8283_Search_FromProductPage(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    url = "https://teamnet.oreillyauto.mx/catalogo/#/catalog/c/oil-chemicals-fluids/motor-oil/motor-oil-vehicle-specific/l/07065/detail/valvoline-mx-synthetic-motor-oil-5w-20-1-quart-875238/m4l0/875238"
    #url = "https://testintranet.oreillyauto.mx/ecatalog-us/#/catalog/brands/accusharp/aus"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    # product = "Motor Oil"
    # home_page.search_product(product)
    # #get product list
    #
    # #home_page.wait_search_results_label()
    # home_page.wait_spinner_disappears()
    # product_list = home_page.get_link_product_list(1)
    # product_selected = home_page.select_random_element_of_list(product_list)
    # logging.info(f"Product Selected: {product_selected}")
    part_number = home_page.get_part_number()
    home_page.click_on_part_interchange_btn()
    logging.info(f"Validate Part number: {part_number}")
    actual_text = home_page.get_text_part_interchange_input()
    logging.info(f"Validate ACTUAL Part number: {actual_text}")
    assert actual_text == part_number, f"The part number should be: {part_number} instead of {actual_text}"
#
#
# # PDP-------------------------------------------------------------------------------------------------------------------
#
# # # MXTEST-8275
@pytest.mark.sprint1_regression# sprint1_regression
@pytest.mark.pdp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8275_Compatibility_Vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://teamnet.oreillyauto.mx/catalogo/#/catalog/brands/accusharp-mx/mfe"
    #url = "https://testintranet.oreillyauto.mx/ecatalog-us/#/catalog/brands/accusharp/aus"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    # home_page.click_on_brands()
    # time.sleep(.5)
    # # CLIC SHOW ALL BRANDS LINK TEXT
    # home_page.click_on_show_all_brands()
    # # click on any brand
    # home_page.get_random_brand()
    # home_page.wait_until_page_load_complete()
    # product_list = home_page.get_link_product_list()
    #
    # product_selected = home_page.select_random_element_of_list(product_list)
    # logging.info(f"Product Selected: {product_selected}")
    home_page.wait_until_page_load_complete()
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()

    home_page.click_on_add_vehicle_submit_btn()
    expected_message = "Does NOT Fit"
    expected_message_2 = "Non application"
    expected_message_3 = "Fits"
    actual_message = home_page.get_compatibility_meessage()
    assert expected_message in actual_message or expected_message_2 in actual_message, f"The message {actual_message} should be: {expected_message} or {expected_message_2}"

# # # MXTEST-8286
@pytest.mark.sprint1_regression
@pytest.mark.test8286
@pytest.mark.flaky(reruns=1)
#@pytest.mark.fallo
def test_MXTEST_8286_DirectLink_CompatibilityError_SelectVehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/oil-chemicals-fluids/motor-oil/motor-oil-full-synthetic/l/n2728/detail/valvoline-synthetic-motor-oil-5w-30-1-quart-884527/m4l0/884527"
    #url = "https://teamnet.oreillyauto.mx/catalogo/#/catalog/search?q=11114"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    # Change language to español
    home_page.change_language_En_to_Es()
    home_page.click_check_vehicle_fit_btn_producction()
    time.sleep(2)
    home_page.wait_until_page_load_complete()
    home_page.write_a_vehicle_type("Uso Liviano Automotriz")
    home_page.write_a_year("2024")
    home_page.write_a_make("Acura")
    home_page.write_a_model("Integra")
    home_page.write_a_submodel("A-Spec")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()

    expected_message = "No compatible"
    non_application_message = "Non application"
    actual_message = home_page.get_compatibility_meessage()
    if non_application_message == actual_message:
        logging.info(actual_message)
    else:
        assert expected_message in actual_message, f"The message {actual_message} should be: {expected_message}"

#
#
# #
# # # # MXTEST-8289
@pytest.mark.sprint1_regression
@pytest.mark.pdp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8289_DirectLink_CompatibilityError_PreselectedVehicle(web_drivers):
    # falta dato URL: https://testintranet.oreillyauto.mx/ecatalog/<<ID DEL ARTICULO >>
    page = HomePage(*web_drivers)
    home_page = page
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/gates/mnv"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    #Change language to español
    home_page.change_language_En_to_Es()
    home_page.click_on_Picker_vehicle_btn()
    time.sleep(2)
    home_page.wait_until_page_load_complete()
    #Choosing specific vehicle
    home_page.write_a_vehicle_type("Uso Liviano Automotriz")
    home_page.write_a_year("2023")
    home_page.write_a_make("Alfa Romeo")
    home_page.write_a_model("Giulia")
    home_page.write_a_submodel("Estrema")
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()

    home_page.wait_spinner_disappears()
    expected_message = "No compatible"

    actual_message = home_page.get_compatibility_meessage()

    assert expected_message in actual_message, f"The message {actual_message} should be: {expected_message}"
#
#
# # AUTO FILL OPTION------------------------------------------------------------------------------------------------------
#
# # # MXTEST-8292
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.autofilloption
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8292_AutofillOption_FreeTextSearchBar(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    word = "mot"
    print(f"Search word: {word} and select a suggest result")
    home_page.search_product(word)
    home_page.wait_until_page_load_complete()
    home_page.take_screenshot("test_AutofillOption_FreeTextSearchBar")

#
#
# # NEW CLIENT------------------------------------------------------------------------------------------------------------
#
# # # MXTEST-8291
##PASSED
@pytest.mark.sprint1_regression
@pytest.mark.newclient
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8291_NewClient_CallWindow(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.enable_keyboard_shortcuts()
    home_page.shortcut_new_client()
    home_page.click_new_client_continue_btn()
    time.sleep(2)
    home_page.click_on_categories_button()
    home_page.wait_until_page_load_complete()
    time.sleep(1)
    home_page.click_on_category_by_text("Aceite, Productos Quimicos y Liquidos")
    home_page.click_on_subcategory_by_text("aceite de motor")
    home_page.shortcut_new_client()
    home_page.click_new_client_cancel_btn()
    product_list = home_page.get_link_product_list(1)
    product = "Aceite de Motor - Completamente Sintetico"
    for prod in product_list:
        if prod.text == product:
            prod.click()
            break

    home_page.shortcut_new_client()
    #step 11
    home_page.click_new_client_cancel_btn()
    # 12 click first element on the list
    product_list = home_page.get_link_product_list()
    home_page.click_on_specific_index_on_list_element(product_list, 0)
    # step 13
    home_page.shortcut_new_client()
    # step 14
    home_page.click_new_client_cancel_btn()
    # step 15 click on brands
    home_page.click_on_brands()
    # step 16 click en show all brands
    home_page.click_on_show_all_brands()
    # step 17
    home_page.shortcut_new_client()
    # step 18
    home_page.click_new_client_cancel_btn()

    home_page.wait_until_page_load_complete()

# # PLP-------------------------------------------------------------------------------------------------------------------
#
# # # MXTEST-8258
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=3)
#@pytest.mark.fallo
def test_MXTEST_8258_PLP_Search_with_Selected_Vehicle(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_Picker_vehicle_btn()
    time.sleep(3)
    vehicle_type_list = home_page.click_on_vehicle_type_dropdown()
    vehicle_type = "Deportes Motorizados"
    home_page.click_element_text_of_list(vehicle_type_list, vehicle_type)
    home_page.click_on_year_and_select()
    home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_brands()
    home_page.click_on_show_all_brands()
    home_page.get_random_brand()
    product_list = home_page.get_link_product_list(0)
    home_page.show_product_list(product_list)
    home_page.take_screenshot("test_PLP_Search_with_Selected_Vehicle")

# # # MXTEST-8259
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8259_PLP_Search_filter_No_results_found(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    wrong_product_name = "jsjsjsjs"
    home_page.wait_until_page_load_complete()
    #home_page.element("loading_img").wait_until_disappears()
    home_page.wait_spinner_disappears()
    home_page.search_wrong_product_name(wrong_product_name)
    expected_message = "Lo sentimos, no se encontraron resultados."
    actual_message = home_page.get_no_results_message()
    assert actual_message == expected_message, f"the message displayed shoeld be: {expected_message} instead of: {actual_message}"
    home_page.take_screenshot("test_PLP_Search_filter_No_results_found")

# # # MXTEST-8260
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8260_PLP_Search_without_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    product_name = "Cartek"
    home_page.search_product(product_name)
    home_page.wait_spinner_disappears()
    product_list = home_page.get_link_product_list(0)
    for product in product_list:
        assert product_name.upper() in product.text.upper(), f"'{product_name.upper()}' must appears in description product, but has: {product.text.upper()}"

#
# # # MXTEST-8262
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8262_PLP_Navigation_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_categories_button()
    time.sleep(2)
    category_list = home_page.get_general_categories_list()
    # click en categoria random
    category_selected = home_page.select_random_element_of_list(category_list)

    logging.info(f"category selected: {category_selected}")
    # obtener lista de subcategorias
    subcategory_list = home_page.get_subcategory_list()
    home_page.select_random_element_of_list(subcategory_list)
    home_page.wait_until_page_load_complete()
    home_page.take_screenshot("test_PLP_Navigation_Categories")
#
# # # MXTEST-8264 mod1 without vehicle selected
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8264_PLP_Sort_by_option_az(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    product_name = "aceite"
    home_page.search_product(product_name)
    # obtener lista original
    product_list = home_page.get_link_product_list(0)
    product_list_text = []
    original_first_char = ''
    for product in product_list:
        description = product.text.split('\n')
        print(description)
        product_description = description[1].split("-")
        print(product_description)
        product_list_text.append(product_description[0])
        print(product_list_text)
        original_first_char = product_description[0][0]
        print(original_first_char)
        break
    print("Primer caracter original")
    print(original_first_char)
    # ordenar con filter by de a-z
    home_page.click_order_by_dropdown_and_select_option("A - Z")
    time.sleep(2)
    home_page.wait_until_page_load_complete()
    # obtener lista ordenada de a-z
    az_product_list = home_page.get_link_product_list(0)
    az_product_list_text = []
    az_first_char=''
    for product in az_product_list:
        description = product.text.split('\n')
        product_description = description[1].split("-")
        az_product_list_text.append(product_description[0])
        az_first_char = product_description[0][0]
        break
    print("primer caracter obtenido")
    print(az_first_char)
    assert az_first_char <= original_first_char, f"{az_first_char} should be <= {original_first_char}"
    home_page.take_screenshot("test_PLP_Sort_by_option_az")

# # MXTEST-8264 mod1 with vehicle selected
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8264_PLP_Sort_by_option_az_vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    #url = "https://testintranet.oreillyauto.mx/ecatalog-us/#/catalog/c/oil-chemicals-fluids/motor-oil/motor-oil-full-synthetic/l/n2728"
    #url2 = "https://testintranet.oreillyauto.mx/ecatalog-us/#/catalog/c/oil-chemicals-fluids/grease-lube/hydraulic-fluid/l/n0419"
    #url ="https://teamnet.oreillyauto.mx/catalogo/#/catalog/c/oil-chemicals-fluids/grease-lube/hydraulic-fluid/l/n0419"
    home_page.wait_until_page_load_complete()
    product_name = "Frenos"
    home_page.search_product(product_name)
    # obtener lista original
    product_list = home_page.get_link_product_list(0)
    product_list_text = []
    original_first_char = ''
    for product in product_list:
        description = product.text.split('\n')
        product_description = description[1].split("-")
        product_list_text.append(product_description[0])
        original_first_char = product_description[0][0]
        break
    print("Primer caracter original")
    print(original_first_char)
    # ordenar con filter by de a-z
    home_page.click_order_by_dropdown_and_select_option("A - Z")
    time.sleep(2)
    home_page.wait_until_page_load_complete()
    # obtener lista ordenada de a-z
    az_product_list = home_page.get_link_product_list(0)
    az_product_list_text = []
    az_first_char=''
    for product in az_product_list:
        description = product.text.split('\n')
        product_description = description[1].split("-")
        az_product_list_text.append(product_description[0])
        az_first_char = product_description[0][0]
        break
    print("primer caracter obtenido")
    print(az_first_char)
    assert az_first_char <= original_first_char, f"{az_first_char} should be <= {original_first_char}"
    home_page.take_screenshot("test_PLP_Sort_by_option_az")

#
# # # MXTEST-8264 mod2
@pytest.mark.sprint1_regression
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8264_PLP_Sort_by_option_za(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    product_name = "Skid Plate"
    home_page.search_product(product_name)
    # obtener lista original
    product_list = home_page.get_link_product_list(0)
    product_list_text = []
    original_first_char = ''
    for product in product_list:
        description = product.text.split('\n')
        product_description = description[1].split("-")
        product_list_text.append(product_description[0])
        original_first_char = product_description[0][0]
        break
    print("Primer caracter original")
    print(original_first_char)

    # ordenar con filter by de a-z
    home_page.click_order_by_dropdown_and_select_option("Z - A")
    home_page.wait_until_page_load_complete()
    time.sleep(2)
    # obtener lista ordenada de a-z
    za_product_list = home_page.get_link_product_list(0)
    za_product_list_text = []
    za_first_char = ''
    for product in za_product_list:
        description = product.text.split('\n')
        product_description = description[1].split("-")
        za_product_list_text.append(product_description[0])
        za_first_char = product_description[0][0]
        break
    print("primer caracter obtenido")
    print(za_first_char)
    assert za_first_char >= original_first_char, f"{za_first_char} should be <= {original_first_char}"
    home_page.take_screenshot("test_PLP_Sort_by_option_za")

# # # MXTEST-8264 mod3
@pytest.mark.sprint1_regression
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
#@pytest.mark.fallo
def test_MXTEST_8264_PLP_Sort_by_option_relevance(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    product_name = "Battery chargers"
    home_page.search_product(product_name)
    original_part_number_list = home_page.get_part_number_list()
    # ordenar con filter by relevance
    home_page.click_order_by_dropdown_and_select_option("Relevance")
    home_page.wait_spinner_disappears()
    home_page.wait_until_page_load_complete()

    # obtener lista ordenada por relevance

    home_page.take_screenshot("before of order by relevance")
    part_number_list_relevance = home_page.get_part_number_list()


    assert part_number_list_relevance == original_part_number_list, f"part number in ascending order: {original_part_number_list} \nshould be: {part_number_list_relevance}"

    home_page.take_screenshot("after of order by relevance")



#
# # # MXTEST-8288
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
# @pytest.mark.fallo
def test_MXTEST_8288_PLP_Vehicle_compatibility_confirmation(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    home_page.wait_spinner_disappears()

    #-----------------------------------
    # seleccionar vehiculo
    vehicle = home_page.select_vehicle_specific()
    home_page.wait_until_page_load_complete()
    time.sleep(1)
    home_page.click_on_categories_button()
    time.sleep(1)
    # obtener lista de categorias
    category_list = home_page.get_general_categories_list()
    if len(category_list) < 1:
        category_list = home_page.get_general_categories_list()
    # click en categoria
    home_page.select_specific_category_of_list(category_list, 2)
    # obtener lista de subcategorias
    subcategory_list = home_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = home_page.get_subcategory_list()
    # click en subcategoria
    subcategory = home_page.select_specific_category_of_list(subcategory_list, 0)
    home_page.wait_until_page_load_complete()
    home_page.wait_spinner_disappears()
    home_page.validate_product_list_page_vehicle(subcategory, vehicle)
    home_page.select_first_subcategory()
# #
# # # MXTEST-8272
@pytest.mark.sprint1_regression
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
def test_MXTEST_8272_Pagination(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.click_on_categories_button()
    time.sleep(1)
    # obtener lista decategorias
    category_list = home_page.get_general_categories_list()
    if len(category_list) < 1:
        category_list = home_page.get_general_categories_list()
    # click en categoria
    home_page.select_specific_category_of_list(category_list, 4)

    # obtener lista de subcategorias
    subcategory_list = home_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = home_page.get_subcategory_list()
    # click en subcategoria
    home_page.select_specific_category_of_list(subcategory_list, 0)
    home_page.wait_until_page_load_complete()

    subcategory = home_page.select_first_subcategory()
    home_page.validate_product_list_page(subcategory)
    home_page.validate_pagination()

# # # MXTEST-8270
@pytest.mark.sprint1_regression
@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=1)
#@pytest.mark.fallo
def test_MXTEST_8270_Navigation_searchby_brand_category_filter(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    #home_page.element("loading_img").wait_until_disappears()
    # click en brands
    home_page.click_on_brands()
    # # click en all brands link
    home_page.click_on_show_all_brands()
    # click on any brand
    brand = home_page.get_random_brand()
    home_page.element("loading_img").wait_until_disappears()
    total_products = home_page.validate_product_list_page(brand.title())
    category_selected = home_page.select_random_category_filter()
    total_products_filtered = home_page.validate_product_list_page(brand.title())
    home_page.validate_page_filtered(category_selected, total_products, total_products_filtered)
#
# # # MXTEST-8269
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.plp
@pytest.mark.flaky(reruns=5)
#@pytest.mark.fallo
def test_MXTEST_8269_Navigation_searchby_category_brand_filter(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    #clic en categorias
    home_page.click_on_categories_button()
    time.sleep(2)
    # obtener lista decategorias
    category_list = home_page.get_general_categories_list()
    #if len(category_list) < 1:
    #    category_list = pl_page.get_general_categories_list()
    # click en categoria
    home_page.select_specific_category_of_list(category_list, 14)
    # obtener lista de subcategorias
    subcategory_list = home_page.get_subcategory_list()
    #if len(subcategory_list) < 1:
    #    subcategory_list = pl_page.get_subcategory_list()
    # click en subcategoria
    subcategory = home_page.select_specific_category_of_list(subcategory_list, 1)
    total_products = home_page.validate_product_list_page(subcategory)
    brand = home_page.select_brand_filter()
    attribute = home_page.select_random_attribute_del_zero_position()
    total_products_filtered = home_page.validate_product_list_page(subcategory.title())
    home_page.wait_spinner_disappears()
    home_page.validate_filtered_page(brand, attribute, total_products, total_products_filtered)

#
# # CLP-------------------------------------------------------------------------------------------------------------------
# # # MXTEST-8261
@pytest.mark.sprint1_regression
#@pytest.mark.pruebitas
@pytest.mark.clp
#@pytest.mark.fallo
@pytest.mark.flaky(reruns=3)
def test_MXTEST_8261_Navigation_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    #-----------------------------------
    home_page.wait_until_page_load_complete()
    home_page.click_on_categories_button()
    time.sleep(2)
    # obtener lista decategorias
    category_list = home_page.get_general_categories_list()
    if len(category_list) < 1:
        time.sleep(1)
        category_list = home_page.get_general_categories_list()
    # click en categoria random
    category_selected = home_page.select_random_element_of_list(category_list)
    logging.info(f"Category selected: {category_selected}")

    # obtener lista de subcategorias
    subcategory_list = home_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = home_page.get_subcategory_list()
    # click en subcategoria random
    subcategory_selected = home_page.select_random_element_of_list(subcategory_list)
    logging.info(f"Subcategory selected: {subcategory_selected}")

   # cl_page.element("loading_img").wait_until_disappears()
    #cl_page.wait_until_page_load_complete()
    home_page.wait_spinner_disappears()
    if home_page.validate_category_landing_page(subcategory_selected):
        logging.info("The Category Landing Page is displayed")
        assert True
    elif home_page.validate_no_products_found():
        logging.info("The subcategory has not items")
        assert True
    elif home_page.validate_product_list_page(subcategory_selected):
        logging.info("The Product list page is displayed")
        assert True
    else:
        logging.info("Error loading the page")
        assert False, "Error loading the page"

#
# # MXTEST-8279 - MXTEST-8278
@pytest.mark.sprint1_regression
@pytest.mark.clp
@pytest.mark.flaky(reruns=3)
#@pytest.mark.fallo
def test_MXTEST_8278_MXTEST_8279_Navigation_Vehicle_Selected(web_drivers):

    home_page = HomePage(*web_drivers)
    url = "https://teamnet.oreillyauto.mx/catalogo/#/catalog/c/brakes/brake-hardware/c0064"
    home_page.open_new_url(url)

    #home_page.open()
    # home_page.open_url_us()

    home_page.wait_spinner_disappears()
    #home_page.element("loading_img").wait_until_disappears()

    # seleccionar vehiculo
    home_page.click_on_Picker_vehicle_btn()
    time.sleep(3)
    vehicle = "Automotive Light Duty"
    #
    # home_page.send_text_vehicle_type(vehicle)
    home_page.write_a_vehicle_type(vehicle)
    home_page.write_a_year("2023")
    home_page.write_a_make("Alfa Romeo")
    home_page.write_a_model("Giulia")
    submodel = "Estrema"
    home_page.write_a_submodel(submodel)
    engine = home_page.click_on_engine_and_select()
    # home_page.click_on_vehicle_type_and_select()
    # home_page.click_on_year_and_select()
    # home_page.click_on_make_and_select()
    # home_page.click_on_model_and_select()
    # home_page.click_on_submodel_and_select()
    # home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()

    home_page.wait_until_page_load_complete()
     #time.sleep(1)
     #home_page.click_on_categories_button()
     #time.sleep(1)
     # obtener lista decategorias
    #category_list = home_page.get_general_categories_list()
     #if len(category_list) < 1:
         #category_list = home_page.get_general_categories_list()
      #click en categoria random
    # category_selected = home_page.select_random_element_of_list(category_list)
     #logging.info(f"Category selected: {category_selected}")
    #
    # # obtener lista de subcategorias
    #subcategory_list = home_page.get_subcategory_list()
     #if len(subcategory_list) < 1:
         #subcategory_list = home_page.get_subcategory_list()
    # # click en subcategoria random
     #subcategory_selected = home_page.select_random_element_of_list(subcategory_list)
     #logging.info(f"Subcategory selected: {subcategory_selected}")
    #home_page.wait_spinner_disappears()
    #subcategory_selected = "BRAKE HARDWARE"
    #if home_page.validate_category_landing_page(subcategory_selected):
        #logging.info("The Category Landing Page is displayed")
        #assert True
    #elif home_page.validate_product_list_page(subcategory_selected):
        #logging.info("The Product list page is displayed")
        #assert True
    #elif home_page.validate_no_products_found():
        #logging.info("The subcategory has not items")
        #assert True
    #elif home_page.validate_no_results_were_found():
        #logging.info("No Results Were Found")
        #assert True
    #else:
        #logging.info("Error loading the page")
        #assert False, "Error loading the page"
