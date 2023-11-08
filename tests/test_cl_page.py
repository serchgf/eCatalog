import logging
import time

from src.page_objects.cl_page import CLPage


# # MXTEST-8261
def test_Navigation_Categories(web_drivers):
    cl_page = CLPage(*web_drivers)

    cl_page.open()
    cl_page.wait_until_page_load_complete()

    cl_page.click_on_categories_button()
    cl_page.zoom_out(80)
    time.sleep(5)

    category_list = cl_page.get_general_categories_list()
    # click en categoria random

    cl_page.wait_until_page_load_complete()
    #cl_page.element("last_category_on_list").wait_visible()
    category_selected = cl_page.select_random_element_of_list(category_list)

    logging.info(f"category selected: {category_selected}")
    # obtener lista de subcategorias
    subcategory_list = cl_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = cl_page.get_subcategory_list()
    # click en subcategoria random
    subcategory_selected = cl_page.select_random_element_of_list(subcategory_list)
    logging.info(f"Subcategory selected: {subcategory_selected}")
    #actual_parent_category = cl_page.click_first_parent_category_on_breadcrumb()
    #assert category_selected == actual_parent_category, f"The actual parent category: {actual_parent_category}, should be: {category_selected}"
    #assert cl_page.validate_parent_category_list_page()
