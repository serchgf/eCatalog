import logging
import time

from src.page_objects.home_page import HomePage


# # # #MXTEST-8263
# def test_Vehicle_Filtering_Functionality_Validation(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(3)
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
#     assert vehicle_selected == expected_vehicle_selected, f"The button must shows: '{expected_vehicle_selected}' instead of '{vehicle_selected}' on the button."
#     home_page.click_on_categories_button_and_select()
#     # Realizar consulta a la base de datos
#     home_page.connect_and_consult()
# #
# #
# # #MXTEST-8282
# def test_Garage_Garage_Vehicle_Limit(web_drivers):
#     # se necesita actualizar el jira, el Maximo permitido en la lista es de 15 en vez de 10
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(3)
#     logging.info(f"FIRST Iteration----------------------------------------------------------------")
#     home_page.click_on_Picker_vehicle_btn()
#     vehicles_list = []
#     for index in range(16):
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
# # #MXTEST-8284
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


# # #MXTEST-8285
# def test_Garage_Remove_Vehicle(web_drivers):
#
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     time.sleep(3)
#     home_page.click_on_Picker_vehicle_btn()
#     vehicles_list = []
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


# #MXTEST-8287
def test_Garage_Category_Navigation(web_drivers):

    home_page = HomePage(*web_drivers)
    home_page.open()
    # time.sleep(3)
    home_page.click_on_categories_button()

    category_selected = home_page.select_random_element_of_list(home_page.get_general_categories_list())
    logging.info(f"Category selected: {category_selected}")
    subcategory_selected = home_page.select_random_element_of_list(home_page.get_subcategory_list())
    logging.info(f"Subcategory selected: {subcategory_selected}")
    text_subcategory_selected = home_page.get_text_label_subcategory_selected()
    assert text_subcategory_selected == subcategory_selected, f"Text displayed: {text_subcategory_selected}, should be: {subcategory_selected}"

    assert home_page.validate_vehicle_list_cleared(), "The vehicles are not cleared correctly, 'Add vehicle info' should be Visible"


# def test_validate_menu_bar_elements(web_drivers):
#     home_page = HomePage(*web_drivers)
#     home_page.open()
#     expected_menu_elements = ['Desktops', 'Laptops & Notebooks', 'Components', 'Tablets', 'Software', 'Phones & PDAs',
#                               'Cameras', 'MP3 Players']
#     actual_menu_elements = home_page.obtain_menu_elements()
#     assert expected_menu_elements in actual_menu_elements, f"Elements in menu bar should be: {expected_menu_elements}"
#     home_page.take_screenshot("test_validate_menu_bar_elements")
