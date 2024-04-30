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

    home_page.validate_spanish_slogan_footer_section()
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

    home_page.validate_spanish_slogan_footer_section()
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


@pytest.mark.flaky(reruns=3)
def test_MXTEST_10924_Spanish_Deals(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.click_deals_button()
    home_page.wait_spinner_disappears()
    #EXPECTED ENGLISH HEADER
    expected_english_header_nav = ["CATEGORIES", "BRANDS", "DEALS", "PART INTERCHANGE", "SEARCH HISTORY", "EN"]
    actual_header_nav = home_page.get_menu_header_nav_span()
    assert expected_english_header_nav == actual_header_nav

    #EXPECTED ENGLISH BREADCRUMB
    expected_english_breadcrumb = ["Home", "Current Ads"]
    actual_breadcrumb_nav = home_page.get_breadcrumb()
    assert expected_english_breadcrumb == actual_breadcrumb_nav

    # EXPECTED ENGLISH DEALS NAVBAR ELEMENTS
    expected_english_deals_navbar = "PAGE 1"
    actual_english_deals_navbar_text = home_page.get_element_pages_navbar_deals()
    assert expected_english_deals_navbar in actual_english_deals_navbar_text

    # EXPECTED ENGLISH DATE OFFER TEXT
    expected_date_offer_english_text_1 = 'From '
    expected_date_offer_english_text_2 = ' to '
    actual_date_offer_english_text = home_page.get_offer_date_info_in_additional_ads()
    assert expected_date_offer_english_text_1 in actual_date_offer_english_text
    assert expected_date_offer_english_text_2 in actual_date_offer_english_text
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
    expected_english_breadcrumb = ["Inicio", "Ofertas vigentes"]
    actual_breadcrumb_nav = home_page.get_breadcrumb()
    assert expected_english_breadcrumb == actual_breadcrumb_nav

    # EXPECTED SPANISH DEALS NAVBAR ELEMENTS
    expected_spanish_deals_navbar = 'GINA 1'
    spanish_nav_bar_element_list = home_page.get_element_pages_navbar_deals()
    cont = 0
    for element in spanish_nav_bar_element_list:
        if expected_spanish_deals_navbar in element:
            cont += 1
            break
    assert cont > 0, "No 'Page' span displayed"
    # EXPECTED SPANISH DATE OFFER TEXT
    expected_date_offer_spanish_text1 = 'Del '
    expected_date_offer_spanish_text2 = ' a '
    actual_date_offer_spanish_text = home_page.get_offer_date_info_in_additional_ads()
    assert expected_date_offer_spanish_text1 in actual_date_offer_spanish_text
    assert expected_date_offer_spanish_text2 in actual_date_offer_spanish_text

    # FOOTER SECTION
    expected_spanish_footer_section = ["HERRAMIENTAS", "Rutas de entrega Jalisco", "Lineas de producto", "Rutas de entrega Leon",
                               "Tiendas O’Reilly", "AYUDA", "Centro de ayuda", "Menú de atajos del teclado"]
    actual_footer_section = home_page.footer_section()
    for footer in expected_spanish_footer_section:
        assert footer in actual_footer_section

    home_page.validate_spanish_slogan_footer_section()
    home_page.validate_copyright_footer_section()
    home_page.validate_logo_footer_section()
    home_page.validate_catalog_version_footer_section()


@pytest.mark.flaky(reruns=3)
def test_MXTEST_10925_Spanish_Parts_interchange(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.change_language_En_to_Es()
    home_page.click_on_part_interchange_btn()
    part = '51060R'
    home_page.write_part_in_interchange_tbx(part)
    home_page.click_part_interchange_search_btn()
    spanish_text_expected = ['Intercambio de parte', 'PASO 1: Escribe un número de parte', 'PASO 2: Elige la categoría que quieres reemplazar:', 'Nota: El intercambio es sólo una referencia.']
    part_interchange_dialog_text = home_page.get_part_interchange_dialog_form_span()
    for expected_text in spanish_text_expected:
        assert expected_text in part_interchange_dialog_text
    home_page.click_first_element_step2_part_interchange()
    home_page.wait_spinner_disappears()
    home_page.click_all_brands_step3_part_interchange()

    # validar que se enentre numero de parte en breadcrumb Inicio Búsqueda de intercambio de partes para '51060r'
    spanish_breadcrumb = home_page.get_last_element_of_breadcrumb()
    assert part.lower() in spanish_breadcrumb

    # validad palabra Resultados de búsqueda
    actual_search_result_text = home_page.get_search_results_span_es()
    expected_spanish_label_search_results = "Resultados de búsqueda"
    assert actual_search_result_text == expected_spanish_label_search_results



    expected_spanish_footer_section = ["HERRAMIENTAS", "Rutas de entrega Jalisco", "Lineas de producto", "Rutas de entrega Leon",
                               "Tiendas O’Reilly", "AYUDA", "Centro de ayuda", "Menú de atajos del teclado"]
    actual_footer_section = home_page.footer_section()
    for footer in expected_spanish_footer_section:
        assert footer in actual_footer_section

    home_page.validate_spanish_slogan_footer_section()
    home_page.validate_copyright_footer_section()
    home_page.validate_logo_footer_section()
    home_page.validate_catalog_version_footer_section()


@pytest.mark.flaky(reruns=3)
def test_MXTEST_10926_Spanish_Shortcut(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    # home_page.wait_spinner_disappears()
    home_page.change_language_En_to_Es()
    # click en menu de atajos de teclado
    home_page.click_shortcuts_menu_btn()
    # obtener todos los elementos de atajos de teclado y comparar
    expected_submenu_title_header_h3 = "ATAJOS DEL TECLADO"
    actual_submenu_title_header_h3 = home_page.get_submenu_header_title_container_h3()
    assert actual_submenu_title_header_h3 == expected_submenu_title_header_h3
    # Get subtitle shortcut section
    expected_functionalities_span_spanish = "Funcionalidades"
    expected_goto_span_spanish = '"Ir a" acciones'
    expected_navigation_span_spanish = "Navegación"
    actual_functionalities_span = home_page.get_shortcut_functionalities_span()
    actual_goto_span = home_page.get_shortcut_goto_span()
    actual_navigation_span = home_page.get_shortcut_navigation_span()
    assert actual_functionalities_span == expected_functionalities_span_spanish.upper()
    assert actual_goto_span == expected_goto_span_spanish.upper()
    assert actual_navigation_span == expected_navigation_span_spanish.upper()

    # Get description and shortcuts list
    expected_description_and_shortcut_list = ['Nuevo Cliente Ctrl Alt N', 'Barra de búsqueda Alt B', 'Agregar / Cambiar vehículo Alt V', 'Eliminar Vehículo Alt D', 'Agregar a la Lista Alt A', 'Limpiar Filtros Alt J', 'Copiar Número de Parte Alt C', 'Ir a la Equivalencia de parte Shift P', 'Ir a Tipos de Parte Shift C', 'Ir a Ofertas Shift D', 'Ir a Marcas Shift B', 'Ir al Historial de Búsqueda Shift H', 'Ir a la Lista de la Orden Shift L', 'Ir a la Página de Inicio Shift Space', 'Regresar Shift Delete', 'Navegar Tab', 'Aceptar / Click CTA Enter', 'Cancelar / Cerrar / Salir Esc', 'Abrir lista de atajos Alt O']
    actual_description_and_shortcut_list = home_page.get_description_and_shortcuts_list()
    assert actual_description_and_shortcut_list == expected_description_and_shortcut_list

    # VALIDAR PRESENCIA DE "Habilitar / Deshabilitar Atajos del Teclado" toggle
    home_page.click_switch_slider_btn()
    home_page.close_shortcut_modal()
    home_page.press_shortcuts('CTRL', 'ALT', 'N')
    home_page.click_new_client_x_close_btn()
    home_page.press_shortcuts("ALT", "O")
    home_page.click_switch_slider_btn()
    home_page.close_shortcut_modal()
    home_page.press_shortcuts('CTRL', 'ALT', 'N')
    visibility = home_page.validate_new_client_popup_visibility()
    assert visibility is False, "The PopUp client should bo visible"



@pytest.mark.flaky(reruns=3)
def test_MXTEST_10927_Spanish_Search_History(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    vehicle = "Automotive Light Duty"
    home_page.write_a_vehicle_type(vehicle)
    home_page.click_on_year_and_select()
    home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    engine = home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_search_history()
    # validate title
    expected_english_search_history_title_span = 'Search history'
    actual_english_search_history_title_span = home_page.get_search_history_title()
    assert actual_english_search_history_title_span == expected_english_search_history_title_span
    # validate 3 tabs
    expected_english_search_history_tab_list = ["ALL SEARCHES", "VEHICLE SEARCH", "OPEN SEARCH"]
    actual_english_search_history_tab_list = home_page.get_search_history_tabs()
    print(f"Actual tabs: {actual_english_search_history_tab_list}")
    assert actual_english_search_history_tab_list == expected_english_search_history_tab_list
    # validate search bar in the three tabs
    # click on each tab an validate the searchbar
    home_page.click_all_searches_tab()
    assert home_page.validate_searchbar_in_all_search(), "A search bar should be displayed"
    home_page.click_vehicle_search_tab()
    assert home_page.validate_searchbar_in_vehicle_search(), "A search bar should be displayed"
    home_page.click_open_search_tab()
    assert home_page.validate_searchbar_in_open_search(), "A search bar should be displayed"
    # close the search history modal
    home_page.close_search_history_modal()
    # input some item to search in the search bar on top
    search_criteria = "Oil"
    home_page.search_and_enter(search_criteria)
    # 16 clean the text of searchbar
    home_page.clean_search()
    # 17 enter a brand for search
    # 18 press enter
    search_criteria = "cartek"
    home_page.search_and_enter(search_criteria)
    # click on search history button
    home_page.click_on_search_history()
    # 20 click to expand the information
    home_page.click_last_searches_expand_btn()
    # close the search history modal
    home_page.close_search_history_modal()
    # click on language selector and select spanish option
    home_page.change_language_En_to_Es()
    # click on historial de busqueda button
    home_page.click_on_search_history()
    # validate title in spanish
    expected_spanish_search_history_title_span = 'Historial de búsqueda'
    actual_spanish_search_history_title_span = home_page.get_search_history_title()
    assert actual_spanish_search_history_title_span == expected_spanish_search_history_title_span
    # validate tabs in spanish
    expected_spanish_search_history_tab_list = ["TODAS LAS BÚSQUEDAS", "BÚSQUEDA POR VEHÍCULO", "BÚSQUEDA LIBRE"]
    actual_spanish_search_history_tab_list = home_page.get_search_history_tabs()
    print(f"Actual tabs: {actual_spanish_search_history_tab_list}")
    assert actual_spanish_search_history_tab_list == expected_spanish_search_history_tab_list



@pytest.mark.inprocess
#@pytest.mark.flaky(reruns=3)
def test_MXTEST_10928_Spanish_Order_List(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open_url_mx()
    home_page.change_language_En_to_Es()
    # HEADER
    expected_header = ["AGREGAR VEHÍCULO", "LISTA DE PRODUCTOS"]
    expected_header_nav = ["CATEGORÍAS", "MARCAS", "OFERTAS", "INTERCAMBIO DE PARTE", "HISTORIAL DE BÚSQUEDA", "ES"]
    actual_header = home_page.get_menu_header_span()
    assert expected_header == actual_header

    home_page.click_on_Picker_vehicle_btn()
    vehicle = "Automotive Light Duty"
    home_page.write_a_vehicle_type(vehicle)
    home_page.click_on_year_and_select()
    home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    engine = home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
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





