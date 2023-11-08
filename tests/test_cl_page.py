import logging
import time

from src.page_objects.cl_page import CLPage


# # MXTEST-8261
def test_Navigation_Categories(web_drivers):
    cl_page = CLPage(*web_drivers)

    cl_page.open()

    #cl_page.wait_until_page_load_complete()
    cl_page.element("loading_img").wait_until_disappears()
    cl_page.click_on_categories_button()
    # obtener lista decategorias
    category_list = cl_page.get_general_categories_list()
    if len(category_list) < 1:
        category_list = cl_page.get_general_categories_list()
    # click en categoria random
    category_selected = cl_page.select_random_element_of_list(category_list)
    logging.info(f"Category selected: {category_selected}")

    # obtener lista de subcategorias
    subcategory_list = cl_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = cl_page.get_subcategory_list()
    # click en subcategoria random
    subcategory_selected = cl_page.select_random_element_of_list(subcategory_list)
    logging.info(f"Subcategory selected: {subcategory_selected}")

    cl_page.wait_until_page_load_complete()

    if cl_page.validate_category_landing_page() == subcategory_selected:
        logging.info("The Category Landing Page is displayed")
        assert True
    elif cl_page.validate_product_list_page() == subcategory_selected:
        logging.info("The Product list page is displayed")
        assert True
    # elif cl_page.element("plp_error").find_element():
    #     logging.info("The subcategory has not items")
    else:
        assert False, "Error loading the page"


# def test_Navigation_Vehicle_Selected(web_drivers):
#
#     cl_page = CLPage(*web_drivers)
#     cl_page.open()
#     cl_page.wait_until_page_load_complete()
#     cl_page.element("loading_img").wait_until_disappears()
#     cl_page.click_on_Picker_vehicle_btn()
#     cl_page.click_on_vehicle_type_and_select()
#     year = cl_page.click_on_year_and_select()
#     make = cl_page.click_on_make_and_select()
#     cl_page.click_on_model_and_select()
#     cl_page.click_on_submodel_and_select()
#     cl_page.click_on_engine_and_select()
#     cl_page.click_on_add_vehicle_submit_btn()
#     expected_vehicle_selected = f"{year} {make}"
#     vehicle_selected = cl_page.get_vehicle_selected()
#     assert vehicle_selected == expected_vehicle_selected, f"The button must shows: '{expected_vehicle_selected}' instead of '{vehicle_selected}' on the button."

