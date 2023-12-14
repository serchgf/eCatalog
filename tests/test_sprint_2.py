import logging
import os
import pathlib
import time
import json

import pytest

from src.page_objects.home_page import HomePage

_JSON_PATH = os.path.join(pathlib.Path(__file__).parent.parent, "locators", "HomePage.json")


# --------------------------------------------JUAN LARIOS---------------------------------------------------------------
# HOME PAGE-------------------------------------------------------------------------------------------------------------
# MXTEST-9075
# MXTEST-9074

# MXTEST-9073

def test_MXTEST_9073_HomePage_Vehicle_Filtering_One_country(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    time.sleep(4)
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.click_on_Picker_vehicle_btn()
    span_country = home_page.get_country_span()
    logging.info(span_country)

    assert "MEX" in span_country or "CAN" in span_country or "USA" in span_country, f"MEX should be in: {span_country} message"


# MXTEST-9058
# MXTEST-9056
# MXTEST-9055
# MXTEST-9054
# MXTEST-9053
# MXTEST-9052
# MXTEST-9051
# MXTEST-9076
# MXTEST-9038
# MXTEST-9030
# MXTEST-9024


# ---------------------------------------------lUIS ESPINOSA------------------------------------------------------------
# MXTEST-9027
# MXTEST-9025
# MXTEST-9019
# MXTEST-9023
# MXTEST-9021
# MXTEST-9022
# MXTEST-9020
# MXTEST-9079
# MXTEST-9078
# MXTEST-9077
# MXTEST-9069
# MXTEST-9068
# MXTEST-9067
# PDP ------------------------------------------------------------------------------------------------------------------
# MXTEST-9034


# ---------------------------------------------SERGIO GARCIA------------------------------------------------------------
# MXTEST-9033
#@pytest.mark.haha
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
def test_MXTEST_9059_PDP_Report_Discrepancies(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/cartek/mih/detail/cartek-ceramic-front-brake-pads-ccd2052/mza0/ccd2052"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.scroll_down()
    home_page.click_send_a_report_link()
    full_name = "Sergio Garcia"
    email = "email_fake@fake.com"
    phone = "1234567890"
    store = "Abastos"
    issue_type = "Wrong Image"
    description_error_text = "Test message text, the image is Wrong"
    home_page.scroll_down()
    home_page.wait_spinner_disappears()
    home_page.fill_product_info_report(full_name, email, phone, store, issue_type, description_error_text)
    home_page.click_send_report_button_info_report_btn()
    home_page.validate_report_created_confirmation()
    home_page.get_report_ticket_number()

# MXTEST-9057
#@pytest.mark.haha
def test_MXTEST_9057_PDP_Add_to_List(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    year = "2021"
    make = "Alfa Romeo"
    model = "Giulia"
    submodel = "Lusso"
    home_page.write_a_vehicle_type("Automotive Light Duty")
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
def test_MXTEST_9043_PDP_ProductDetailsNotCompatibility(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/accel/acc/detail/accel-ignition-condenser-111131/acc0/111131"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.validate_nonAplication_product_label()

# MXTEST-9042
#@pytest.mark.haha
def test_MXTEST_9042_PDP_UniversalProductTagPLP(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/accel/acc"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.get_number_of_nonApplication_product_label_in_PLP()

# MXTEST-9041
#@pytest.mark.haha
def test_MXTEST_9041_PDP_ResourcesNotDisplaying(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/accel/acc/detail/accel-spark-plug-0526-4/acc0/05264"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.wait_until_page_load_complete()
    home_page.validate_resources_tab_is_not_displayed()



# MXTEST-9028
# @pytest.mark.haha
def test_MXTEST_9028_PDP_Generic_images_from_Selected_Brand(web_drivers):
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/c/filters/cabin-air-filter/l/02700"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.validate_presence_of_default_image_src()
    product_list = home_page.get_link_product_list()
    home_page.validate_presence_of_default_image_src()
    home_page.select_random_element_of_list(product_list)
    home_page.validate_presence_of_default_image_src()

# MXTEST-9036
#@pytest.mark.haha
def test_MXTEST_9036_PDP_ResourcesDisplay(web_drivers):
    # encontrar un producto que contenga la tab "resources"
    home_page = HomePage(*web_drivers)
    url = "pagina con resources tab"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.click_resources_tab()

# MXTEST-9026
#@pytest.mark.haha
def test_MXTEST_9026_PDP_Product_image_with_available_images_Selected_Brand(web_drivers):
    #falta producto que contenga imagen en 360
    home_page = HomePage(*web_drivers)
    url = "https://testintranet.oreillyauto.mx/ecatalog-mx/#/catalog/brands/gates-mx/mnv/detail/gates-mx-g-force-carbon-cord-cvt-belt-11c3218/mnv0/11c3218"
    home_page.open_new_url(url)
    home_page.wait_spinner_disappears()
    home_page.click_img_arrow_back_button()
    home_page.click_img_arrow_forward_button()
    home_page.click_main_product_img()

# SEARCH BAR-------------------------------------------------------------------------------------------------------------
# MXTEST-9050

#@pytest.mark.haha
def test_MXTEST_9050_SearchBar_Autocomplete_Select_Brand_Vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    year = "2021"
    make = "Alfa Romeo"
    model = "Giulia"
    submodel = "Lusso"
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year(year)
    home_page.write_a_make(make)
    home_page.write_a_model(model)
    home_page.write_a_submodel(submodel)
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    search_criteria = "acc"
    home_page.select_first_suggestion_brand(search_criteria)


# MXTEST-9049
#@pytest.mark.haha
def test_MXTEST_9049_SearchBar_Autocomplete_Select_Category_Vehicle_Selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    year = "2021"
    make = "Alfa Romeo"
    model = "Giulia"
    submodel = "Lusso"
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year(year)
    home_page.write_a_make(make)
    home_page.write_a_model(model)
    home_page.write_a_submodel(submodel)
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    search_criteria = "whe"
    home_page.search_product(search_criteria)
    product_list = home_page.get_link_product_list(1)
    home_page.scroll_down()
    home_page.select_random_element_of_list(product_list)
    home_page.wait_spinner_disappears()

# MXTEST-9048
#@pytest.mark.haha
def test_MXTEST_9048_SearchBar_Partial_Search_Term_Vehicle_selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    year = "2021"
    make = "Alfa Romeo"
    model = "Giulia"
    submodel = "Lusso"
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year(year)
    home_page.write_a_make(make)
    home_page.write_a_model(model)
    home_page.write_a_submodel(submodel)
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    search_criteria = "brake"
    home_page.search_product(search_criteria)
    home_page.wait_spinner_disappears()
    home_page.validate_keyword_in_p_text_of_results_list(search_criteria)




# ---------------------------------------------GRECIA LOPEZ-------------------------------------------------------------
# SEARCH BAR-------------------------------------------------------------------------------------------------------------

# MXTEST-9046 SearchBar_Valid_Item Name_Vehicle_Selected
#@pytest.mark.pruebitas
def test_MXTEST_9046_SearchBar_Valid_Item_Name_Vehicle_Selected(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    search_criteria = "strut mount"
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    year = "2019"
    make = "Acura"
    model = "ILX"
    submodel = "A-Spec"
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year(year)
    home_page.write_a_make(make)
    time.sleep(1)
    home_page.write_a_model(model)
    home_page.write_a_submodel(submodel)
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto, f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"
    #Go to the database and run the following <query>.

#@pytest.mark.pruebitas
def test_MXTEST_9045_searchBar_valid_part_number_vehicle_selected(web_drivers):
# MXTEST-9045 SearchBar_Valid_Part Number_Vehicle_Selected
    home_page = HomePage(*web_drivers)
    home_page.open()
    part_number = "33849"
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    home_page.click_on_vehicle_type_and_select()
    year = home_page.click_on_year_and_select()
    make = home_page.click_on_make_and_select()
    home_page.click_on_model_and_select()
    home_page.click_on_submodel_and_select()
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
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
def test_MXTEST_9044_searchBar_valid_category_vehicle_selected(web_drivers):
    # MXTEST-9044 SearchBar_Valid_Category_Vehicle_Selected
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.click_on_Picker_vehicle_btn()
    year = "2021"
    make = "Alfa Romeo"
    model = "Giulia"
    submodel = "Lusso"
    home_page.write_a_vehicle_type("Automotive Light Duty")
    home_page.write_a_year(year)
    home_page.write_a_make(make)
    home_page.write_a_model(model)
    home_page.write_a_submodel(submodel)
    home_page.click_on_engine_and_select()
    home_page.click_on_add_vehicle_submit_btn()
    search_criteria = "Brake Pads & Shoes"
    home_page.search_product(search_criteria)
    home_page.wait_spinner_disappears()
    product_list = home_page.get_link_product_list(1)
    assert len(product_list) > 0, f"No mostro resultados la categoria: {search_criteria}"

#@pytest.mark.pruebitas
def test_MXTEST_9018_searchBar_partial_search_term(web_drivers):
    # MXTEST-9018 SearchBar_Partial_Search_Term
    home_page = HomePage(*web_drivers)
    home_page.open()
    search_criteria = "strut m"
    home_page.wait_spinner_disappears()
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto, f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"


#@pytest.mark.pruebitas
def test_MXTEST_9016_searchBar_valid_item_name(web_drivers):
# MXTEST-9016 SearchBar_Valid_Item Name
    home_page = HomePage(*web_drivers)
    home_page.open()
    search_criteria = "strut mount"
    home_page.wait_spinner_disappears()
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto, f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"
    #Go to the database and run the following <query>.

#@pytest.mark.pruebitas
def test_MXTEST_9015_searchBar_valid_part_number(web_drivers):
# MXTEST-9015 SearchBar_Valid_Part Number
    home_page = HomePage(*web_drivers)
    home_page.open()
    part_number = "33849"
    home_page.wait_spinner_disappears()
    home_page.element("search_bar").wait_clickable().send_keys(part_number)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    part_number_list = home_page.element("part_number_button").find_elements()
    #logging.info(f"El tamaño de la lista es: {len(part_number_list)}")
    #for part in part_number_list:
    #    logging.info(part.text)
    assert part_number in part_number_list[0].text, f"No se encontro el numero de parte:{part_number} en la busqueda:{part_number_list[0].text}"
    # Go to the database and run the following <query>.

@pytest.mark.pruebitas
def test_MXTEST_9014_searchBar_valid_category(web_drivers):
# MXTEST-9014 SearchBar_Valid_Category
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.wait_spinner_disappears()
    search_criteria = "Brake Pads & Shoes"
    home_page.search_product(search_criteria)
    home_page.wait_spinner_disappears()
    product_list = home_page.get_link_product_list(1)
    assert len(product_list) > 0, f"No mostro resultados la categoria: {search_criteria}"


#@pytest.mark.pruebitas
def test_MXTEST_9040_searchBar_autocomplete_select_brand(web_drivers):
    #MXTEST-9040 SearchBar_Autocomplete_Select_Brand
    home_page = HomePage(*web_drivers)
    # url= "www.google.com"
    # home_page.open_new_url(url)
    home_page.open()
    search_criteria = "bos"
    home_page.wait_spinner_disappears()
    #home_page.search_product("Motor Oil") #Busqueda por valor
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    bosch_brand = home_page.element("highlight_search_result").find_element()
    home_page.clic_javacript(bosch_brand)
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto.upper()}"

    #Go to the database and run the following <query>.

#@pytest.mark.pruebitas
def test_MXTEST_9039_searchBar_autocomplete_select_category(web_drivers):
    # MXTEST-9039 SearchBar_Autocomplete_Select_Category
    home_page = HomePage(*web_drivers)
    # url= "www.google.com"
    # home_page.open_new_url(url)
    home_page.open()
    search_criteria = "acce"
    home_page.wait_spinner_disappears()
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    bosch_brand = home_page.element("highlight_search_result").find_element()
    home_page.clic_javacript(bosch_brand)
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto.upper(), f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto.upper()}"


#@pytest.mark.pruebitas
def test_MXTEST_9037_searchBar_autosuggestions(web_drivers):
    # MXTEST-9037 SearchBar_Autosuggestions
    home_page = HomePage(*web_drivers)
    search_criteria = "bra"
    # url= "www.google.com"
    # home_page.open_new_url(url)
    home_page.open()
    home_page.wait_spinner_disappears()
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    suggestion_list = home_page.get_suggestion_list()
    assert len(suggestion_list) > 0, "No se mostraron sugerencias"
    for element in suggestion_list:
        print(element)

#@pytest.mark.pruebitas
def test_MXTEST_9035_searchBar_invalid_search_term(web_drivers):
    # MXTEST-9035 SearchBar_Invalid_Search Term
    home_page = HomePage(*web_drivers)
    home_page.open()
    search_criteria = "#$$$$"
    expected_message = "We're sorry, no results were found"
    home_page.wait_spinner_disappears()
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    actual_message = home_page.get_no_results_message()
    assert actual_message == expected_message, f"El mensaje actual deberia ser: {expected_message}, en vez de {actual_message}"

#@pytest.mark.pruebitas
def test_MXTEST_9035_searchBar_keywords_search(web_drivers):
    # MXTEST-9031 SearchBar_Keywords_search
    home_page = HomePage(*web_drivers)
    home_page.open()
    search_criteria = "oil"
    home_page.wait_spinner_disappears()
    home_page.element("search_bar").wait_clickable().send_keys(search_criteria)
    home_page.press_enter_key()
    home_page.wait_spinner_disappears()
    lista_productos = home_page.get_description_product()
    for producto in lista_productos:
        assert search_criteria.upper() in producto, f"El nombre de producto: {search_criteria.upper()} no se encontro en {producto}"













