import logging
import time

from src.page_objects.cl_page import CLPage


# # MXTEST-8261
def test_Navigation_Categories(web_drivers):
    cl_page = CLPage(*web_drivers)

    cl_page.open()

    cl_page.element("loading_img").wait_until_disappears()
    cl_page.wait_until_page_load_complete()

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

   # cl_page.element("loading_img").wait_until_disappears()
    #cl_page.wait_until_page_load_complete()

    if cl_page.validate_category_landing_page(subcategory_selected):
        logging.info("The Category Landing Page is displayed")
        assert True
    elif cl_page.validate_product_list_page(subcategory_selected):
        logging.info("The Product list page is displayed")
        assert True
    elif cl_page.validate_no_products_found():
        logging.info("The subcategory has not items")
        assert True
    else:
        logging.info("Error loading the page")
        assert False, "Error loading the page"


# MXTEST-8279 - MXTEST-8278
def test_Navigation_Vehicle_Selected(web_drivers):

    cl_page = CLPage(*web_drivers)
    cl_page.open()
    cl_page.wait_until_page_load_complete()
    cl_page.element("loading_img").wait_until_disappears()

    # seleccionar vehiculo
    cl_page.click_on_Picker_vehicle_btn()
    cl_page.click_on_vehicle_type_and_select(0)      # send "1" to random type, "0" or none to select default type
    cl_page.click_on_year_and_select(1)
    cl_page.click_on_make_and_select(1)
    cl_page.click_on_model_and_select(1)
    cl_page.click_on_submodel_and_select(1)
    cl_page.click_on_engine_and_select(1)
    cl_page.click_on_add_vehicle_submit_btn()

    cl_page.wait_until_page_load_complete()
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

    if cl_page.validate_category_landing_page(subcategory_selected):
        logging.info("The Category Landing Page is displayed")
        assert True
    elif cl_page.validate_product_list_page(subcategory_selected):
        logging.info("The Product list page is displayed")
        assert True
    elif cl_page.validate_no_products_found():
        logging.info("The subcategory has not items")
        assert True
    else:
        logging.info("Error loading the page")
        assert False, "Error loading the page"
