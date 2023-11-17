import json
import logging
import random
import time
import mysql.connector
from selenium.common import JavascriptException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from src.page_objects.base_page import BasePage
from selenium.webdriver.support.select import Select
import locators


class HomePage(BasePage):

    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(HomePage, self).__init__(driver, wait_driver)

    def search(self, value: str):
        logging.info(f"Search {value}")
        self.element("search_input").wait_clickable().send_keys(value)
        self.element("search_btn").wait_clickable().click()

    def search_product(self, value: str):
        #time.sleep(3)
        logging.info(f"Search: {value}")
        search_bar = self.element("search_bar").wait_clickable()
        search_bar.send_keys(value)
        self.element("highlight_search_result").wait_clickable().click()

    def obtain_menu_elements(self) -> list[str]:
        logging.info(f"Get menu bar names")
        self.element("menu_bar").wait_visible()
        return [element.text for element in self.element("menu_bar").find_elements()]

    def click_on_Picker_vehicle_btn(self):
        time.sleep(1)
        logging.info(f"Click on Picker vehicle btn")
        self.element("add_vehicle_btn").wait_clickable().click()

    def write_a_vehicle_type(self, vehicle: str):
        logging.info(f"Write a vehicle type: {vehicle}")
        self.element("vehicle_type_dropdown").wait_clickable().click()
        time.sleep(.5)
        self.javascript_clic(vehicle)

    def write_a_year(self, year: str):
        logging.info(f"Write Year: {year}")
        self.element("year_dropdown").wait_clickable().click()
        self.javascript_clic(year)

    def write_a_make(self, make: str):
        logging.info(f"Write make: {make}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.javascript_clic(make)
    def write_a_model(self, model: str):
        logging.info(f"Write model: {model}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.javascript_clic(model)
    def write_a_submodel(self, submodel: str):
        logging.info(f"Write submodel: {submodel}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.javascript_clic(submodel)
    def write_a_engine(self, engine: str):
        logging.info(f"Write engine: {engine}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.javascript_clic(engine)
    def click_on_vehicle_type_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        # logging.info(f"waiting for vehicle country checkbox icons")
        self.element("vehicle_type_label").wait_visible()
        logging.info(f"Click on Vehicle dropdown")
        dropdown = self.element("vehicle_type_dropdown").wait_clickable()
        #self.clic_javacript(dropdown)
        #time.sleep(4)
        dropdown.click()
        time.sleep(1)
        vehicle_type = self.select_index_list_element(index)
        return vehicle_type

        # if index is None:
        #     self.select_first_list_element()
        # else:
        #     self.select_index_list_element(index)

    def click_on_year_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.2)

        logging.info(f"Click on year dropdown")

        dropdown = self.element("year_dropdown").wait_visible()
        dropdown.click()
        time.sleep(.3)
        year = self.select_index_list_element(index)
        return year

    def click_on_make_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.5)
        logging.info(f"Click on make dropdown")
        dropdown = self.element("make_dropdown").wait_visible()
        #dropdown.click()
        time.sleep(.4)

        make = self.select_index_list_element(index)
        return make

    def click_on_model_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.3)
        logging.info(f"Click on model dropdown")
        dropdown = self.element("model_dropdown").wait_clickable()
        # self.clic_javacript(dropdown)
        # dropdown.click()


        # dropdown.click()
        self.select_index_list_element(index)

    def click_on_submodel_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.3)
        logging.info(f"Click on submodel dropdown")
        dropdown = self.element("submodel_dropdown").wait_clickable()
        # dropdown.click()
        submodel = self.select_index_list_element(index)
        return submodel

    def click_on_engine_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.2)
        logging.info(f"Click on engine dropdown")
        dropdown = self.element("engine_dropdown").wait_clickable()
        # dropdown.click()
        engine = self.select_index_list_element(index)
        return engine

    def send_text_vehicle_type(self, vehicle_type: str):
        logging.info(f"Write into vehicle type textbox: {vehicle_type}")
        self.element("vehicle_type_tbx").wait_clickable().send_keys(vehicle_type, Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(.3)

    def new_submodel_and_select(self, submodel: str):
        logging.info(f"Click on new submodel dropdown")
        """
        Input a submodel and the function remove that element of the list if len more tha 1

        :return: other randome element on the list at least only one element exist
        """
        time.sleep(.2)
        logging.info(f"Click on submodel dropdown")
        dropdown = self.element("submodel_dropdown").wait_clickable()
        dropdown.click()
        time.sleep(.2)
        lista = self.element("list_box").find_elements()
        time.sleep(.2)
        dropdown.click()
        new_submodel_text = ""
        if len(lista) == 1:
            submodel = lista[0].text
            lista[0].click()
            logging.info(f"select element on the list with index: {0}: {submodel}")
            return submodel
        else:
            for i, ele in enumerate(lista):
                if ele.text == submodel:
                    pass
                else:
                    index = i
                    new_submodel = ele
                    new_submodel_text = new_submodel.text
                    logging.info(f"select NEW SUBMODEL with index:{index}-> {new_submodel_text}")
                    ele.click()
                    break
            return new_submodel_text

    #
    def new_engine_and_select(self, engine: str):
        logging.info(f"Click on new engine dropdown")
        """
        Input a engine and the function remove that element of the list if len more tha 1
        :param index:
        :return: other randome element on the list at least only one element exist
        """
        time.sleep(.2)
        logging.info(f"Click on engine dropdown")
        dropdown = self.element("engine_dropdown").wait_clickable()
        dropdown.click()
        time.sleep(.2)
        lista = self.element("list_box").find_elements()
        time.sleep(.2)
        dropdown.click()
        new_engine_text = ""
        if len(lista)==1:
            engine = lista[0].text
            lista[0].click()
            logging.info(f"select element on the list with index: 0: {engine}")
            return engine
        else:
            for i, ele in enumerate(lista):
                if ele.text == engine:
                    pass
                else:
                    index = i
                    new_engine = ele
                    new_engine_text = new_engine.text
                    logging.info(f"select NEW SUBMODEL with index:{index}-> {new_engine_text}")
                    ele.click()
                    break
            return new_engine_text

    def click_on_add_vehicle_submit_btn(self):
        logging.info(f"Click on Add vehicle submit button")
        self.element("add_vehicle_button_submit").wait_clickable().click()

    def click_on_categories_button_and_select_pupular_first_category(self):
        logging.info(f"Click on categories button")
        self.element("categories_btn").wait_clickable().click()
        logging.info(f"selecting a popular category")
        self.select_first_popular_category()

    def click_on_categories_button(self):
        logging.info(f"Click on categories button")
        self.element("categories_btn").wait_clickable().click()

    def click_check_vehicle_fit_btn(self):
        logging.info("Click check vehicle fit button")
        self.element("check_vehicle_fit_btn").wait_clickable().click()

    def get_general_categories_list(self):
        logging.info(f"Get General Category List")
        self.element("general_category_list").wait_visible()
        general_category_list = self.element("general_category_list").find_elements()
        #logging.info(f"El tamaño de la lista general:{len(general_category_list)}")
        return general_category_list

    def get_subcategory_list(self):
        logging.info(f"Get subcategory List")
        self.element("label_subcategory_selected").wait_visible()
        subcategory_list = self.element("subcategory_list").find_elements()
        return subcategory_list

    def get_text_label_subcategory_selected(self):
        logging.info(f"Get label text of subcategory selected")
        subcategory_label = self.element("label_subcategory_selected").wait_visible()
        return subcategory_label.text

    def select_random_element_of_list(self, lista: list):
        #time.sleep(2)
        self.wait_until_page_load_complete()
        logging.info(f"Select a random element of the list")
        index = random.randint(0, len(lista))
        element_selected = lista[index]
        element_text = element_selected.text
        element_text = element_text.upper()
        # self.scroll_to_element(element_selected)
        # self.move_to_element_and_click(element_selected)
        # self.clic_javacript(element_selected)
        time.sleep(.5)
        try:
            self.clic_javacript(element_selected)
        except:
            element_selected.click()

        return element_text

    def wait_search_results_label(self):
        logging.info(f"Wait search results label")
        try:
            logging.info(f"looking for: search results label")
            self.element("search_results_label").wait_visible()
            return 0
        except:
            logging.info(f"looking for: Additional label")
            self.press_end_key()
            #self.scroll_to_element(self.element("additional_label").wait_visible())
            self.element("additional_label").wait_visible()
            return 1

    def click_first_parent_category_on_breadcrumb(self):
        logging.info(f"click on first parent category on breadcrumb")
        lista = self.element("breadcrum_section_link_list").find_elements()
        logging.info(f"select first element on the list: {lista[1].text}")
        first_element = lista[1].text
        lista[1].click()
        return first_element

    def select_index_list_element(self, index=0):
        logging.info(f"Get element list")
        self.element("vehicle_type_label").wait_visible()
        lista = self.element("list_box").find_elements()
        if index != 0:
            n_elementos = len(lista)
            index = random.randint(0, n_elementos)
            time.sleep(.2)
            element_selected = lista[index].text
            logging.info(f"select element on the list with index: {index}: {element_selected}")
            #self.clic_javacript(lista[index])
            lista[index].click()
        else:
            index = 0
            time.sleep(.2)
            element_selected = lista[index].text
            logging.info(f"select element on the list with index: {index}: {element_selected}")
            self.clic_javacript(lista[index])
            #lista[index].click()

        return element_selected

    def press_page_down_key_from_carousel(self):
        logging.info(f"Press Page Down key from carousel")
        element = self.element("carousel").wait_clickable()
        self.page_down_key_from_element(element)



    def get_vehicle_selected(self):
        # era 1.5
        time.sleep(1.5)
        logging.info(f"Get vehicle selected text")
        return self.element("vehicle_selected").wait_visible().text

    def get_part_number(self):
        logging.info(f"Get Part Number")
        part_number_text = self.element("part_number").wait_visible().text
        # logging.info(f"TEXTO ORIGINAL: {part_number_text}")
        part_number_list = part_number_text.split("content_copy")
        part_number = part_number_list[0].rstrip().lstrip()

        logging.info(f"Part Number: {part_number}")
        return part_number

    def select_first_popular_category(self):
        logging.info(f"Select the first popular category in the list")
        lista = self.element("popular_categories_list_btn").find_elements()
        logging.info(f"select first element of the list: {lista[0].text}")
        first_element = lista[0].text
        lista[0].click()
        return first_element

    def click_on_add_new_vehicle_btn(self):
        logging.info(f"Click on add new Vehicle button")
        self.element("add_new_vehicle_btn").wait_clickable().click()

    def click_on_edit_info_btn(self):
        logging.info(f"Click on Edit Info button")
        self.element("edit_info_btn").wait_clickable().click()

    def click_on_save_changes_btn(self):
        logging.info(f"Click on Save Changes button")
        self.element("save_changes_btn").wait_clickable().click()

    def click_on_deleteAll_btn(self):
        logging.info(f"Click on Delete All button")
        self.element("delete_all_btn").wait_clickable().click()

    def click_on_goBack_btn(self):
        logging.info(f"Click on Go Back button")
        self.element("go_back_btn").wait_clickable().click()

    def click_on_accesories(self):
        logging.info(f"Click ACCESORIES")
        self.javascript_clic("Accessories")

    def click_on_exterior_accessories(self):
        logging.info(f"Click Exterior ACCESSORIES")
        self.javascript_clic("Exterior Accessories")

    def click_on_CanopyAndTent(self):
        logging.info(f"Click Canopy And Tent")
        self.javascript_clic("Canopy And Tent")

    def click_element_text_of_list(self, lista:list, text: str):
        logging.info(f"Click on: {text}")
        for element in lista:
            element_text = element.text
            logging.info(f"***************** {element_text}")

            if text in element_text:
                logging.info(f"Click {text.upper()}S*****************")
                self.clic_javacript(element)

                break

    def close_categories(self):
        logging.info(f"Close Categories modal")
        self.element("close_categories_x_button").wait_clickable().click()
    def presenceOf_popular_categories_label(self):
        logging.info(f"Presence of Popular Categories Label")
        try:
            self.element("popular_categories_label").wait_visible()
            return True
        except TimeoutError:
            logging.info(f"Label is not displayed")

    def get_text_label_vehicle_selected(self):
        logging.info(f"Get text label of vehicle selected")
        labels = self.element("labels_vehicle_selected").find_elements()
        submodel_label = labels[0].text
        logging.info(f"SUBMODEL LABEL: {submodel_label}")
        engine_label = labels[1].text
        logging.info(f"ENGINE LABEL: {engine_label}")
        return submodel_label, engine_label

    def get_recent_vehicles_list(self):
        logging.info(f"Get Recent Vehicle List added")
        lista = self.element("recent_vehicles").find_elements()
        logging.info(f"Elements found: {len(lista)}")
        # for ele in lista:
        #     logging.info(f"{ele.text}")
        return len(lista)

    def validate_vehicle_list_cleared(self):
        logging.info(f"validate vehicle list cleared")
        if self.element("add_vehicle_info_label").wait_visible():
            return True

    def validate_parent_category_list_page(self):
        logging.info(f"Validate parent category list page")
        return self.element("element_buttons_grid_category").wait_clickable()

    def get_product_list_2(self):

        logging.info(f"Get Products list_2")
        self.wait_until_page_load_complete()
        self.element("link_products_list_2").wait_visible()
        lista = self.element("link_products_list_2").find_elements()
        if len(lista) != 0:
            return lista
        else:
            self.wait_until_page_load_complete()
            self.element("link_products_list_2").wait_visible()
            lista = self.element("link_products_list_2").find_elements()

    def get_link_product_list(self, type_of_label=0):
        logging.info(f"Get Products list")
        self.wait_until_page_load_complete()
        if type_of_label == 1:
            self.element("additional_label").wait_visible()
            time.sleep(1)
            lista = self.element("link_products_list_2").find_elements()
            if len(lista)!= 0:
                return lista
            else:
                self.element("link_products_list_2").wait_visible()
                time.sleep(1)
                lista = self.element("link_products_list_2").find_elements()
                return lista
        if type_of_label == 0:
            self.element("search_results_label").wait_visible()
            time.sleep(1)
            lista = self.element("link_products_list").find_elements()
            if len(lista)!= 0:
                return lista
            else:
                lista = self.element("link_products_list").find_elements()
                return lista

    def get_popular_category_list(self):
        self.wait_until_page_load_complete()
        logging.info(f"Get popular category list")
        self.element("popular_categories_label").wait_visible()

        lista = self.element("popular_categories_list_btn").find_elements()
        if len(lista) != 0:
            return lista
        else:
            self.element("popular_categories_label").wait_visible()
            lista = self.element("popular_categories_list_btn").find_elements()
            return lista

    def show_product_list(self, product_list: list):
        for product in product_list:
            logging.info(product)

    def click_homepage_button(self):
        logging.info(f"Click home page button")
        self.element("homePage_button").wait_clickable().click()

    def get_lasted_viewed_products_list(self):
        logging.info(f"Get Lasted viewed products list")
        self.element('last_viewed_products_label').wait_visible()
        #self.scroll_to_element(self.element('last_viewed_products_label'))
        self.scroll_down()
        lista =[]
        # self.element("last_viewed_products_label").scroll_down_to_element()
        lista_0 = self.element("lasted_products_viewed_list").find_elements()
        for element in lista_0:
            element = element.text
            element = element.upper()
            lista.append(element)
        return lista

    def clean_product_selected(self, expected_product_selected: str):
        product_selected = expected_product_selected.split('#')
        product_selected = product_selected[0].split('\n')
        return product_selected[1]

    def get_footer_links_name_href_dict(self):
        logging.info(f"Get Footer links list")
        self.element("tools_span").wait_visible()
        dic_name_href = {}
        link_list = self.element("footer_links").find_elements()
        for link in link_list:
            dic_name_href[link.text] = link.get_attribute("href")
        return dic_name_href

    def get_footer_links_href(self):
        logging.info(f"Get Footer links href(url)")
        self.element("tools_span").wait_visible()
        links_href_list = []
        link_list = self.element("footer_links").find_elements()
        for link in link_list:
            links_href_list.append(link.get_attribute('href'))
        return links_href_list

    def click_on_part_interchange_btn(self):
        logging.info(f"Click on 'PART INTERCHANGE' button")
        self.element("part_interchange_linktext").wait_clickable().click()

    def close_part_interchange(self):
        logging.info(f"Close part interchange")
        self.element("close_part_interchange_x_button").wait_clickable().click()

    def get_text_part_interchange_input(self):
        logging.info(f"Get Text from Part Interchange input tbx")
        texto = self.element("part_interchange_input_tbx").wait_visible().get_attribute('ng-reflect-model')
        # logging.info(f"Text from Part Interchange input tbx: {texto}")
        return texto
    def write_part_in_interchange_tbx(self, part):
        logging.info(f"Write Part in Interchange tbx")
        self.element("part_interchange_input_tbx").wait_visible().send_keys(part)

    def clear_part_interchange_input_tbx(self):
        logging.info("Clear part interchange input tbx")
        self.element("part_interchange_input_tbx").wait_visible().clear()


    # def validate_footer_links_href(self, href_list: list, data_json):
    #     logging.info(f"Validate expected href links with actual href(url) on footer page")
    #     name_list =[]
    #     href_list = []
    #     link_list = self.element("footer_links").find_elements()
    #     for link in link_list:
    #         links_href_list.append(link.get_attribute('href'))
    #     return links_href_list
    def click_on_brands(self):
        logging.info(f"Click on brands dropdown list")
        self.element("brands_dropdown").wait_visible().click()


    def click_on_show_all_brands(self):
        logging.info(f"Click on show all brands link text ")
        self.element("show_all_brands_link").wait_clickable().click()

    def clic_outside_of_modal_window(self):
        logging.info("click outside of modal window")
        self.element("search_bar").wait_visible().send_keys(Keys.ESCAPE)

        #self.element("blank_space").wait_visible().click()
        # element = self.element("blank_space").wait_visible()
        # self.move_to_element_coordinates(element, 0, 0)

    def click_part_interchange_search_btn(self):
        logging.info("Click part interchange search button")
        self.element("part_interchange_search_button").wait_visible().click()

    def get_part_interchange_step_2_list(self):
        logging.info("Get part interchange step 2 list")
        self.element("part_interchange_step_2").wait_visible()
        step_2_list = self.element("part_interchange_step_2_list").find_elements()
        # for part_type in step_2_list:
        #     logging.info(part_type.text)

        return step_2_list

    def get_no_results_found_message(self):
        logging.info("Get no results found message")
        return self.element("no_results_container").wait_visible().text

    def get_does_not_fit_meessage(self):
        logging.info("Get does not fit message")
        return self.element("does_not_fit_message_label").wait_visible().text
    def click_on_logo_oreily_home(self):
        logging.info("Click logo oreilly home")
        self.element("img_logo_oreilly_home").wait_visible().click()

    def clic_blank_space(self):
        logging.info("click blank space")
        self.element("blank_space").wait_visible().click()

    def get_random_brand(self):
        logging.info(f"Click Random Brand")
        self.element("explore_brands_label").wait_visible()
        brands_list = self.element("all_brands_link_list").find_elements()
        logging.info(f"El numero de marcas son: {len(brands_list)}")

        index = random.randint(0, len(brands_list))
        brand_selected = brands_list[index].text
        logging.info(f"Brand Selected: {brand_selected}")
        time.sleep(.5)
        brands_list[index].click()
        return brand_selected

    def get_search_results_number(self):
        logging.info(f"Get search results number")
        try:
            self.element("span_filter_by").wait_visible()
        except TimeoutError:
            self.element("span_filter_by").wait_visible()

        self.element("sort_by_dropdown").wait_visible()
        search_results = self.element("search_results_label").wait_visible().text
        logging.info(f"search result label: {search_results}")
        cadena_l = search_results.split('(')
        numero = cadena_l[1].replace(')', '')
        numero = int(numero)
        return numero

    def get_search_message(self):
        logging.info("Get search results message")
        text = self.element("no_results_message").find_element().text
        return text

    def cargar_json_data(self, JSON_PATH: str):
        with open(JSON_PATH) as archivo:
            datos = json.load(archivo)
        return datos

    def mysql_connection(self):
        connection = mysql.connector.connect(
            host="172.22.210.13",
            user="epc_QA_RO",
            password="{BcZJ3qhj]zU!z4%{CvJ",
            db="epc"
        )
        return connection

    def connect_and_consult(self):
        logging.info(f"Connect to DB")
        connection = self.mysql_connection()
        cursor = connection.cursor()
        logging.info(f"Execute query")
        cursor.execute("SELECT * FROM epc.application_vehicle_indexes avi INNER JOIN epc.vehicles v on v.a_vehicle_id = avi.vehicle_id WHERE avi.application_id='161096296'  AND avi.part_type_id = '02512' GROUP BY avi.application_id, avi.vehicle_id;")
        results = cursor.fetchall()
        assert len(results) is not None, "No data to see"
        for result in results:
            logging.info(f"{result}")
        cursor.close()
        connection.close()

