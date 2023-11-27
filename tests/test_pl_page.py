import logging
import time

from src.page_objects.pl_page import PLPage


# # MXTEST-8261
def test_Vehicle_compatibility_confirmation(web_drivers):

    pl_page = PLPage(*web_drivers)
    pl_page.open()
    pl_page.wait_until_page_load_complete()
    pl_page.element("loading_img").wait_until_disappears()

    # seleccionar vehiculo
    vehicle = pl_page.select_vehicle_specific()

    pl_page.wait_until_page_load_complete()

    pl_page.click_on_categories_button()
    # obtener lista decategorias
    category_list = pl_page.get_general_categories_list()
    if len(category_list) < 1:
        category_list = pl_page.get_general_categories_list()
    # click en categoria
    pl_page.select_specific_category_of_list(category_list, 24)

    # obtener lista de subcategorias
    subcategory_list = pl_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = pl_page.get_subcategory_list()
    # click en subcategoria
    pl_page.select_specific_category_of_list(subcategory_list, 9)

    pl_page.wait_until_page_load_complete()

    subcategory = pl_page.select_first_subcategory()

    pl_page.validate_product_list_page_vehicle(subcategory, vehicle)

def test_Pagination(web_drivers):

    pl_page = PLPage(*web_drivers)
    pl_page.open()
    pl_page.wait_until_page_load_complete()
    pl_page.element("loading_img").wait_until_disappears()
    pl_page.click_on_categories_button()
    # obtener lista decategorias
    category_list = pl_page.get_general_categories_list()
    if len(category_list) < 1:
        category_list = pl_page.get_general_categories_list()
    # click en categoria
    pl_page.select_specific_category_of_list(category_list, 0)

    # obtener lista de subcategorias
    subcategory_list = pl_page.get_subcategory_list()
    if len(subcategory_list) < 1:
        subcategory_list = pl_page.get_subcategory_list()
    # click en subcategoria
    pl_page.select_specific_category_of_list(subcategory_list, 8)
    pl_page.wait_until_page_load_complete()

    subcategory = pl_page.select_first_subcategory()
    pl_page.validate_product_list_page(subcategory)
    pl_page.validate_pagination()
