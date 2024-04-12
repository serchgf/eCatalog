import logging
import os
import pathlib
import time
import json

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys

from src.page_objects.home_page import HomePage
from src.page_objects.base_page import images

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")


@pytest.mark.phase2_sp2
#@pytest.mark.flaky(reruns=3)
def test_MXTEST_11023_Shortcuts_NIPEnterSearch(web_drivers):
    home_page = HomePage(*web_drivers)
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/brakes/brake-pads-shoes/brake-pads/l/03351/detail/cartek-disc-brake-pad-set-ctk7013a-d50/mij0/ctk7013ad50'
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_help_center()
    home_page.validate_help_center_page()
    home_page.element("hcp_issue_report").find_element().click()
    home_page.validate_issue_report_modal()
    home_page.element("irm_employId").wait_visible().send_keys("3805", Keys.ENTER)
    home_page.element("nip_verified").wait_visible()
    name = home_page.element("irm_employName").find_element().get_attribute('value')
    email = home_page.element("irm_employEmail").find_element().get_attribute('value')
    assert name == 'LARIOS MARISCAL JUAN LUIS' and email == 'juan.larios@oreillyauto.mx', "Fields not filled"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.element("send_report_btn").find_element().click()
    home_page.element("input_nip").wait_visible().send_keys("3805", Keys.ENTER)
    home_page.element("nip_verified").wait_visible()
    name2 = home_page.element("irm_employName").find_element().get_attribute('value')
    email2 = home_page.element("input_email").find_element().get_attribute('value')
    assert name2 == 'Larios Mariscal Juan Luis' and email2 == 'juan.larios@oreillyauto.mx', "Fields not filled"

@pytest.mark.phase2_sp2
#@pytest.mark.flaky(reruns=3)
def test_MXTEST_11015_Shortcuts_GoBackBreadcrumb(web_drivers):
    home_page = HomePage(*web_drivers)
    url = 'https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/accessories/truck-towing-jeep/truck-accessories/alarms/alarm/l/n0165'
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.enable_disable_shortcuts()
    breadcrumb_original = [element.text for element in home_page.element("breadcrumb_elements").find_elements()]
    logging.info(breadcrumb_original)
    home_page.press_shortcuts('SHIFT', 'DELETE')
    home_page.wait_spinner_disappears()
    breadcrumb_actual = [element.text for element in home_page.element("breadcrumb_elements").find_elements()]
    assert len(breadcrumb_actual) < len(breadcrumb_original)
    for x in range(len(breadcrumb_actual)-1):
        home_page.press_shortcuts('SHIFT', 'DELETE')
        home_page.wait_spinner_disappears()
    breadcrumb_final = [element.text for element in home_page.element("breadcrumb_elements").find_elements()]
    assert len(breadcrumb_final) == 0, "The page displayed is not Home Page"


@pytest.mark.flaky(reruns=3)
def test_MXTEST_10920_Spanish_Dashboard(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()

    # HEADER
    expected_header = ["AGREGAR VEHÍCULO", "LISTA DE PRODUCTOS"]
    expected_header_nav = ["CATEGORÍAS", "MARCAS", "OFERTAS", "INTERCAMBIO DE PARTE", "HISTORIAL DE BÚSQUEDA", "ES"]
    actual_header = home_page.get_menu_header_span()
    assert expected_header == actual_header

    # HEADER NAV
    actual_header_nav = home_page.get_menu_header_nav_span()
    assert expected_header_nav == actual_header_nav

    # FOOTER SECTION
    expected_footer_section = ["HERRAMIENTAS", "Rutas de entrega Jalisco", "Lineas de producto", "Rutas de entrega Leon",
                               "Tiendas O’Reilly", "AYUDA", "Centro de ayuda", "Menú de atajos del teclado"]
    actual_footer_section = home_page.footer_section()
    for footer in expected_footer_section:
        assert footer in actual_footer_section

    home_page.validate_slogan_footer_section()
    home_page.validate_copyright_footer_section()
    home_page.validate_logo_footer_section()
    home_page.validate_catalog_version_footer_section()

    # buscar un elemento
    product_url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/search/detail/mikels-oil-can-a3r/mur0/a3r?q=oil"
    home_page.open_new_url(product_url)
    home_page.wait_spinner_disappears()
    home_page.click_on_logo_oreily_home()
    # BODY
    home_page.validate_ultimos_productos_vistos_section()




@pytest.mark.flaky(reruns=3)
def test_MXTEST_10921_Spanish_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.click_on_categories_button()
    english_popular_category_list = home_page.get_popular_category_list()
    english_popular_category_list_text = []
    for category in english_popular_category_list:
        english_popular_category_list_text.append(category.text)

    home_page.close_categories()

    home_page.change_language_En_to_Es()
    home_page.click_on_categories_button()
    spanish_popular_category_list = home_page.get_popular_category_list()
    spanish_popular_category_list_text = []
    for category in spanish_popular_category_list:
        spanish_popular_category_list_text.append(category.text)

    assert len(english_popular_category_list) == len(spanish_popular_category_list)
    print(f"English len list: {len(english_popular_category_list)}")
    print(f"Spanish len list: {len(spanish_popular_category_list)}")
    assert english_popular_category_list_text != spanish_popular_category_list_text
    print(f"English popular part list: {english_popular_category_list_text}")
    print(f"Spanish tipos de parte populares: {spanish_popular_category_list_text}")


@pytest.mark.flaky(reruns=3)
def test_MXTEST_10922_Spanish_Sub_Categories(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.change_language_En_to_Es()
    home_page.click_on_categories_button()
    category = "Bateria y Accesorios"
    home_page.click_on_category_by_text(category)
    home_page.click_ver_todo_link()
    # HEADER NAV
    expected_header_nav = ["CATEGORÍAS", "MARCAS", "OFERTAS", "INTERCAMBIO DE PARTE", "HISTORIAL DE BÚSQUEDA", "ES"]
    actual_header_nav = home_page.get_menu_header_nav_span()
    assert expected_header_nav == actual_header_nav
    # FOOTER SECTION
    expected_footer_section = ["HERRAMIENTAS", "Rutas de entrega Jalisco", "Lineas de producto", "Rutas de entrega Leon",
                               "Tiendas O’Reilly", "AYUDA", "Centro de ayuda", "Menú de atajos del teclado"]
    actual_footer_section = home_page.footer_section()
    for footer in expected_footer_section:
        assert footer in actual_footer_section

    home_page.validate_slogan_footer_section()
    home_page.validate_copyright_footer_section()
    home_page.validate_logo_footer_section()
    home_page.validate_catalog_version_footer_section()


@pytest.mark.flaky(reruns=3)
def test_MXTEST_10923_Spanish_Brands(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.click_brands_btn()
    home_page.click_on_show_all_brands()
    letter_selected = home_page.click_random_letter_brand_menu()
    # GET BRANDS LIST IN ENGLISH
    english_brand_list = home_page.get_list_of_brands_from_letter_selected(letter_selected)
    print(f"English brand_list: {english_brand_list}")

    home_page.change_language_En_to_Es()
    home_page.click_specified_letter_brand_menu(letter_selected)

    # # GET BRANDS LIST IN SPANISH
    spanish_brand_list = home_page.get_list_of_brands_from_letter_selected(letter_selected)
    print(f"Spanish brand list: {spanish_brand_list}")
    assert english_brand_list == spanish_brand_list or len(english_brand_list) == len(spanish_brand_list)


@pytest.mark.inprocess
# @pytest.mark.flaky(reruns=3)
def test_MXTEST_10924_Spanish_Deals(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.click_deals_button()
    #EXPECTED ENGLISH HEADER
    expected_english_header_nav = ["CATEGORIES", "BRANDS", "DEALS", "PART INTERCHANGE", "SEARCH HISTORY", "EN"]
    actual_header_nav = home_page.get_menu_header_nav_span()
    assert expected_english_header_nav == actual_header_nav

    #EXPECTED ENGLISH BREADCRUMB
    expected_english_breadcrumb = ["Home", "Current Ads"]
    actual_breadcrumb_nav = home_page.get_breadcrumb()
    assert expected_english_breadcrumb == actual_breadcrumb_nav

    # EXPECTED ENGLISH DEALS NAVBAR ELEMENTS
    expected_english_deals_navbar = "PAGE"
    actual_breadcrumb_nav = home_page.get_breadcrumb()
    assert expected_english_breadcrumb == actual_breadcrumb_nav

    # EXPECTED ENGLISH DATE OFFER TEXT

    # FOOTER SECTION
    expected_english_footer_section = ["TOOLS", "Delivery routes Jalisco", "Product lines", "Delivery routes Leon",
                               "O’Reilly Stores", "HELP", "Help center", "Shortcuts menu"]

    actual_footer_section = home_page.footer_section()
    for footer in expected_english_footer_section:
        assert footer in actual_footer_section

    home_page.change_language_En_to_Es()


    # EXPECTED SPANISH HEADERS
    expected_header_nav = ["CATEGORÍAS", "MARCAS", "OFERTAS", "INTERCAMBIO DE PARTE", "HISTORIAL DE BÚSQUEDA", "ES"]
    actual_header_nav = home_page.get_menu_header_nav_span()
    assert expected_header_nav == actual_header_nav
    # EXPECTED SPANISH BREADCRUMB

    expected_english_brandcrumb = ["Home", "Current Ads"]
    actual_header_nav = home_page.get_menu_header_nav_span()
    assert expected_english_brandcrumb == actual_header_nav
    # EXPECTED SPANISH DEALS NAVBAR ELEMENTS

    # EXPECTED SPANISH DATE OFFER TEXT

    # FOOTER SECTION
    expected_spanish_footer_section = ["HERRAMIENTAS", "Rutas de entrega Jalisco", "Lineas de producto", "Rutas de entrega Leon",
                               "Tiendas O’Reilly", "AYUDA", "Centro de ayuda", "Menú de atajos del teclado"]
    actual_footer_section = home_page.footer_section()
    for footer in expected_spanish_footer_section:
        assert footer in actual_footer_section

    home_page.validate_slogan_footer_section()
    home_page.validate_copyright_footer_section()
    home_page.validate_logo_footer_section()
    home_page.validate_catalog_version_footer_section()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10925_Spanish_Parts_interchange(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10926_Spanish_Shortcut(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10927_Spanish_Search_History(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10928_Spanish_Order_List(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10929_Spanish_Add_Vehicle_and_Garage(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10930_Spanish_PLP(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10931_Spanish_PLP_Filters(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10932_Spanish_PDP(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10933_Spanish_PDP_report_issue(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10934_PDP_Report_an_incident_search_store(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10935_Spanish_Help_Center(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()

@pytest.mark.phase2_sp2
@pytest.mark.flaky(reruns=3)
def test_MXTEST_10936_Spanish_SearchBar(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()





