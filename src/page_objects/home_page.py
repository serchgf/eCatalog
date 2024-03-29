import json
import logging
import random
import time
import mysql.connector
from selenium.common import JavascriptException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from src.page_objects.base_page import BasePage
from selenium.webdriver.support.select import Select
import locators


class HomePage(BasePage):
    # sprint 1------------------------------------------------------------------------------------------------------------
    #
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(HomePage, self).__init__(driver, wait_driver)

    def search_and_enter(self, value: str):
        """
        Type the search criteria in search bar and press enter
        :param value:
        :return:
        """
        logging.info(f"Search {value}")
        print(f"Search {value}")
        self.element("search_bar").wait_clickable().send_keys(value, Keys.ENTER)


    def search_product(self, value: str):
        # time.sleep(3)
        """
        Esta funcion escribe un valor en el buscador y da clic en el primer elemento
        resaltado en las sugerencias
        """
        logging.info(f"Search product: {value}")
        print(f"Search product: {value}")
        search_bar = self.element("search_bar").wait_clickable()
        search_bar.send_keys(value)
        time.sleep(1)
        self.element("highlight_search_result").wait_clickable().click()

    def search_wrong_product_name(self, value: str):
        # time.sleep(3)
        logging.info(f"Search product: {value}")
        print(f"Search product: {value}")
        search_bar = self.element("search_bar").wait_clickable()
        search_bar.send_keys(value)
        action = self.actionChain()
        action.send_keys(Keys.ENTER)
        action.perform()

    def obtain_menu_elements(self) -> list[str]:
        logging.info(f"Get menu bar names")
        print(f"Get menu bar names")
        self.element("menu_bar").wait_visible()
        return [element.text for element in self.element("menu_bar").find_elements()]

    def click_on_Picker_vehicle_btn(self):
        time.sleep(1)
        logging.info(f"Click on Picker vehicle btn")
        print(f"Click on Picker vehicle btn")
        self.element("add_vehicle_btn").wait_clickable().click()

    def write_a_vehicle_type(self, vehicle: str):
        logging.info(f"Write a vehicle type: {vehicle}")
        print(f"Write a vehicle type: {vehicle}")
        self.element("vehicle_type_dropdown").wait_clickable().click()
        time.sleep(.5)
        self.javascript_clic(vehicle)

    def write_a_year(self, year: str):
        logging.info(f"Write Year: {year}")
        print(f"Write Year: {year}")
        self.element("year_dropdown").wait_clickable().click()
        self.javascript_clic(year)

    def write_a_make(self, make: str):
        logging.info(f"Write make: {make}")
        print(f"Write make: {make}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.javascript_clic(make)

    def write_a_model(self, model: str):
        logging.info(f"Write model: {model}")
        print(f"Write model: {model}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.element("list_box").wait_clickable()
        self.javascript_clic(model)

    def write_a_submodel(self, submodel: str):
        logging.info(f"Write submodel: {submodel}")
        print(f"Write submodel: {submodel}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.element("list_box").wait_clickable()
        self.javascript_clic(submodel)

    def write_a_engine(self, engine: str):
        logging.info(f"Write engine: {engine}")
        print(f"Write engine: {engine}")
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.element("list_box").wait_clickable()
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
        print(f"Click on Vehicle dropdown")
        self.element("vehicle_type_dropdown").wait_visible()
        dropdown = self.element("vehicle_type_dropdown").wait_clickable()
        # self.clic_javacript(dropdown)
        # time.sleep(4)
        dropdown.click()
        time.sleep(.5)
        try:
            vehicle_type = self.select_index_list_element(index)
            return vehicle_type
        except IndexError:
            vehicle_type = self.select_index_list_element(index)
            return vehicle_type

        # if index is None:
        #     self.select_first_list_element()
        # else:
        #     self.select_index_list_element(index)

    def click_on_vehicle_type_dropdown(self):
        """
        Click on vehicle type dropdown
        :param index:
        :return: list
        """
        logging.info(f"click vehicle type dropdown")
        print(f"click vehicle type dropdown")
        self.element("vehicle_type_label").wait_visible()
        dropdown = self.element("vehicle_type_dropdown").wait_clickable()
        dropdown.click()
        time.sleep(.5)
        self.element("list_box").wait_visible()
        self.element("list_box").wait_clickable()

        vehicle_type_list = self.element("list_box").find_elements()
        return vehicle_type_list

    def click_on_year_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.5)

        logging.info(f"Click on year dropdown")
        print(f"Click on year dropdown")
        dropdown = self.element("year_dropdown").wait_visible()
        self.element("year_dropdown").wait_clickable()
        # dropdown.click()
        try:
            year = self.select_index_list_element(index)
        except IndexError:
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
        print(f"Click on make dropdown")
        dropdown = self.element("make_dropdown").wait_visible()
        self.element("make_dropdown").wait_clickable()
        ##dropdown.click()

        try:
            make = self.select_index_list_element(index)
        except IndexError:
            make = self.select_index_list_element(index)
        return make

    def click_on_model_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.5)
        logging.info(f"Click on model dropdown")
        print(f"Click on model dropdown")
        self.element("model_dropdown").wait_visible()
        dropdown = self.element("model_dropdown").wait_clickable()
        # self.clic_javacript(dropdown)
        # dropdown.click()
        try:
            model = self.select_index_list_element(index)
        except IndexError:
            model = self.select_index_list_element(index)
        return model

    def click_on_submodel_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.5)
        logging.info(f"Click on submodel dropdown")
        print(f"Click on submodel dropdown")
        self.element("submodel_dropdown").wait_visible()
        dropdown = self.element("submodel_dropdown").wait_clickable()
        # dropdown.click()
        time.sleep(.2)
        try:
            submodel = self.select_index_list_element(index)
        except IndexError:
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
        print(f"Click on engine dropdown")
        dropdown = self.element("engine_dropdown").wait_clickable()
        # dropdown.click()
        time.sleep(.2)
        try:
            engine = self.select_index_list_element(index)
        except IndexError:
            engine = self.select_index_list_element(index)
        return engine

    def send_text_vehicle_type(self, vehicle_type: str):
        logging.info(f"Write into vehicle type textbox: {vehicle_type}")
        print(f"Write into vehicle type textbox: {vehicle_type}")
        self.element("vehicle_type_tbx").wait_clickable().send_keys(vehicle_type, Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(.3)

    def new_submodel_and_select(self, submodel: str):
        logging.info(f"Click on new submodel dropdown")
        print(f"Click on new submodel dropdown")
        """
        Input a submodel and the function remove that element of the list if len more than 1

        :return: other randome element on the list at least only one element exist
        """

        time.sleep(.2)
        logging.info(f"Click on submodel dropdown")
        dropdown = self.element("submodel_dropdown").wait_clickable()
        dropdown.click()
        time.sleep(.2)
        try:
            self.element("list_box").wait_visible()
        except TimeoutError:
            self.element("list_box").wait_visible()
        lista = self.element("list_box").find_elements()
        # time.sleep(.2)
        ##dropdown.click()
        new_submodel_text = ""
        new_submodel_text_list = []
        if len(lista) == 1:
            submodel = lista[0].text
            lista[0].click()
            logging.info(f"select element on the list with index: {0}: {submodel}")
            print(f"select element on the list with index: {0}: {submodel}")
            return submodel
        else:
            for i, ele in enumerate(lista):
                if ele.text == submodel:
                    pass
                else:
                    index = i
                    new_submodel = ele
                    new_submodel_text = new_submodel.text
                    new_submodel_text_list = new_submodel_text.split("\n")
                    logging.info(f"select NEW SUBMODEL with index:{index}-> {new_submodel_text}")
                    print(f"select NEW SUBMODEL with index:{index}-> {new_submodel_text_list[0]}")
                    ele.click()
                    break
            return new_submodel_text_list[0]

    #
    def new_engine_and_select(self, engine: str):
        logging.info(f"Click on new engine dropdown")
        print(f"Click on new engine dropdown")
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
        try:
            self.element("list_box").wait_visible()
        except TimeoutError:
            self.element("list_box").wait_visible()
        lista = self.element("list_box").find_elements()

        new_engine_text = ""
        new_engine_text_list = []
        engine_list = []
        if len(lista) == 1:
            engine = lista[0].text
            lista[0].click()
            engine_list = engine.split('\n')
            logging.info(f"select element on the list with index: 0: {engine}")
            print(f"select element on the list with index: 0: {engine_list[0]}")
            return engine_list[0]
        else:
            for i, ele in enumerate(lista):
                if ele.text in " No results found ":
                    dropdown = self.element("engine_dropdown").wait_clickable()
                    time.sleep(1)
                    dropdown.click()
                    print(f"se encontro no results found")
                    self.press_esc_key()
                    time.sleep(.3)
                    break
                if ele.text == engine:
                    pass
                else:
                    index = i
                    new_engine = ele
                    new_engine_text = new_engine.text
                    new_engine_text_list = new_engine_text.split("\n")
                    logging.info(f"select NEW ENGINE with index:{index}-> {new_engine_text}")
                    print(f"select NEW ENGINE with index:{index}-> {new_engine_text_list[0]}")
                    ele.click()
                    break
            return new_engine_text_list[0]

    def click_new_client_continue_btn(self):
        logging.info(f"Click new client continue button")
        print(f"Click new client continue button")
        self.element("new_client_label").wait_visible()
        self.element("new_client_continue_btn").wait_clickable().click()

    def click_new_client_cancel_btn(self):
        logging.info(f"Click new client cancel button")
        print(f"Click new client cancel button")
        self.element("new_client_label").wait_visible()
        self.element("new_client_cancel_btn").wait_clickable().click()

    def shortcut_new_client(self):
        logging.info("New client shortcut: 'SHIFT+C'")
        print("New client shortcut: 'SHIFT+C'")
        action = self.actionChain()
        action.send_keys(Keys.SHIFT + 'C')
        action.perform()
        time.sleep(1)

    def click_on_category_by_text(self, text: str):
        logging.info(f"Click on category: {text}")
        print(f"Click on category: {text}")
        self.element("popular_categories_label").wait_visible()
        self.javascript_clic(text)

    def click_on_subcategory_by_text(self, text: str):
        logging.info(f"Click on subcategory: {text}")
        print(f"Click on subcategory: {text}")
        time.sleep(1)
        self.element("subcategory_list").find_elements()
        self.javascript_clic(text)

    def click_on_add_vehicle_submit_btn(self):
        logging.info(f"Click on Add vehicle submit button")
        print(f"Click on Add vehicle submit button")
        self.element("add_vehicle_button_submit").wait_clickable().click()

    def click_on_categories_button_and_select_pupular_first_category(self):
        logging.info(f"Click on categories button")
        print(f"Click on categories button")
        self.element("categories_btn").wait_clickable().click()
        logging.info(f"selecting a popular category")
        print(f"selecting a popular category")
        self.select_first_popular_category()

    def click_on_categories_button(self):
        logging.info(f"Click on categories button")
        print(f"Click on categories button")
        self.element("categories_btn").wait_clickable().click()

    def click_check_vehicle_fit_btn(self):
        logging.info("Click check vehicle fit button")
        print("Click check vehicle fit button")
        self.element("check_vehicle_fit_btn").wait_clickable().click()

    def click_check_vehicle_fit_btn_producction(self):
        logging.info("Click check vehicle fit button produccion")
        print("Click check vehicle fit button produccion")
        self.element("check_vehicle_fit_btn_produccion").wait_clickable().click()

    def get_general_categories_list(self):

        logging.info(f"Get General Category List")
        self.element("general_categories_label").wait_visible()
        print(f"Get General Category List")
        self.element("general_category_list").wait_visible()
        general_category_list = self.element("general_category_list").find_elements()
        # logging.info(f"El tamaño de la lista general:{len(general_category_list)}")
        return general_category_list

    def get_subcategory_list(self):
        logging.info(f"Get subcategory List")
        print(f"Get subcategory List")
        # self.element("label_subcategory_selected").wait_visible()
        self.element("go_back_btn").wait_visible()
        try:
            logging.info(f"try subcategory_list")
            print(f"try subcategory_list")
            subcategory_list = self.element("subcategory_list").find_elements()
        except:
            try:
                logging.info(f"try subcategory_list_2")
                print(f"try subcategory_list_2")
                subcategory_list = self.element("subcategory_list_2").find_elements()
            except:
                logging.info(f"try subcategory_list_3")
                print(f"try subcategory_list_3")
                subcategory_list = self.element("subcategory_list_3").find_elements()
        return subcategory_list

    def get_text_label_subcategory_selected(self):
        logging.info(f"Get label text of subcategory selected")
        print(f"Get label text of subcategory selected")
        subcategory_label = self.element("label_subcategory_selected").wait_visible()
        return subcategory_label.text

    # def select_random_element_of_list(self, lista: list):
    #     #time.sleep(2)
    #     self.wait_until_page_load_complete()
    #     logging.info(f"Select a random element of the list")
    #     print(f"Select a random element of the list")
    #     index = random.randint(0, len(lista))
    #     element_selected = lista[index]
    #     element_text = element_selected.text
    #     element_text = element_text.upper()
    #     # self.scroll_to_element(element_selected)
    #     # self.move_to_element_and_click(element_selected)
    #     # self.clic_javacript(element_selected)
    #     time.sleep(.5)
    #     try:
    #         self.clic_javacript(element_selected)
    #     except:
    #         element_selected.click()
    #
    #     return element_text

    def wait_search_results_label(self):
        logging.info(f"Wait search results label")
        print(f"Wait search results label")
        try:
            logging.info(f"looking for: search results label")
            print(f"looking for: search results label")
            self.element("search_results_label").wait_visible()
            return 0
        except:
            logging.info(f"looking for: Additional label")
            print(f"looking for: Additional label")
            self.press_end_key()
            # self.scroll_to_element(self.element("additional_label").wait_visible())
            self.element("additional_label").wait_visible()
            return 1

    def click_first_parent_category_on_breadcrumb(self):
        logging.info(f"click on first parent category on breadcrumb")
        print(f"click on first parent category on breadcrumb")
        lista = self.element("breadcrum_section_link_list").find_elements()
        logging.info(f"select first element on the list: {lista[1].text}")
        print(f"select first element on the list: {lista[1].text}")
        first_element = lista[1].text.upper()
        lista[1].click()
        return first_element

    def select_index_list_element(self, index=0):
        logging.info(f"Get element list")
        print(f"Get element list")
        self.element("vehicle_type_label").wait_visible()
        self.element("list_box").wait_visible()

        lista = self.element("list_box").find_elements()

        if index != 0:
            n_elementos = len(lista)
            index = random.randint(0, n_elementos)
            time.sleep(.2)
            element_selected = lista[index].text
            logging.info(f"select element on the list with index: {index}: {element_selected}")
            print(f"select element on the list with index: {index}: {element_selected}")
            # self.clic_javacript(lista[index])
            if element_selected in ' No results found ':
                self.press_esc_key()
                time.sleep(.5)
                return 0
            else:
                if index > len(lista):
                    index = index - len(lista)
                lista[index].click()
        else:
            index = 0
            time.sleep(.2)
            element_selected = lista[index].text
            logging.info(f"select element on the list with index: {index}: {element_selected}")
            print(f"select element on the list with index: {index}: {element_selected}")
            if element_selected in ' No results found ':
                self.press_esc_key()
                return 0
            else:
                if index > len(lista):
                    index = index - len(lista)
                lista[index].click()

        return element_selected

    def click_on_specific_index_on_list_element(self, lista: list, index: int):
        """ click on specific index on list element provided """
        time.sleep(.2)
        element_selected = lista[index].text
        logging.info(f"select element on the list with index: {index}: {element_selected}")
        print(f"select element on the list with index: {index}: {element_selected}")
        self.clic_javacript(lista[index])
        # lista[index].click()

        return element_selected

    def press_page_down_key_from_carousel(self):
        logging.info(f"Press Page Down key from carousel")
        print(f"Press Page Down key from carousel")
        element = self.element("carousel").wait_clickable()
        self.page_down_key_from_element(element)

    def get_vehicle_selected(self):
        # era 1.5
        time.sleep(1.5)
        logging.info(f"Get vehicle selected text")
        print(f"Get vehicle selected text")
        return self.element("vehicle_selected").wait_visible().text

    def get_country_span(self):
        logging.info("Get MEX span")

        span = self.element("MEX_span").wait_visible().text
        return span

        # text = self.element("vehicle_selected").wait_visible().text
        # vehicle_selected = text.split('\n')
        # return vehicle_selected[0]

    def get_part_number(self):
        logging.info(f"Get Part Number")
        print(f"Get Part Number")
        try:
            part_number_text = self.element("part_number").wait_visible().text
        except TimeoutError:
            part_number_text = self.element("part_number_mx").wait_visible().text
        logging.info(f"TEXTO ORIGINAL: {part_number_text}")
        part_number_text = part_number_text.replace("\ncontent_copy", '')
        part_number_list = part_number_text.split("\n")
        # part_number_list = part_number_text.split("content_copy")
        part_number = part_number_list[0].rstrip().lstrip()

        logging.info(f"Part Number: {part_number}")
        print(f"Part Number: {part_number}")
        return part_number_text

    def get_part_number_list(self):
        logging.info("Get part number list")
        part_number_list = self.element("part_number_button").find_elements()
        part_number_list_text = []
        for part in part_number_list:
            part_number_list_text.append(part.text)

        return part_number_list_text

    def select_first_popular_category(self):
        logging.info(f"Select the first popular category in the list")
        print(f"Select the first popular category in the list")
        lista = self.element("popular_categories_list_btn").find_elements()
        logging.info(f"select first element of the list: {lista[0].text}")
        print(f"select first element of the list: {lista[0].text}")
        first_element = lista[0].text
        lista[0].click()
        return first_element

    def click_on_add_new_vehicle_btn(self):
        logging.info(f"Click on add new Vehicle button")
        print(f"Click on add new Vehicle button")
        self.element("add_new_vehicle_btn").wait_clickable().click()

    def click_on_edit_info_btn(self):
        logging.info(f"Click on Edit Info button")
        print(f"Click on Edit Info button")
        self.element("edit_info_btn").wait_clickable().click()

    def click_on_save_changes_btn(self):
        logging.info(f"Click on Save Changes button")
        print(f"Click on Save Changes button")
        self.element("save_changes_btn").wait_visible()
        self.element("save_changes_btn").wait_clickable().click()

    def click_on_deleteAll_btn(self):
        logging.info(f"Click on Delete All button")
        print(f"Click on Delete All button")
        self.element("delete_all_btn").wait_clickable().click()

    def click_on_goBack_btn(self):
        logging.info(f"Click on Go Back button")
        print(f"Click on Go Back button")
        self.element("go_back_btn").wait_clickable().click()

    def click_on_accesories(self):
        logging.info(f"Click ACCESORIES")
        print(f"Click ACCESORIES")
        self.javascript_clic("Accessories")

    def click_on_exterior_accessories(self):
        logging.info(f"Click Exterior ACCESSORIES")
        print(f"Click Exterior ACCESSORIES")
        self.javascript_clic("Exterior Accessories")

    def click_on_CanopyAndTent(self):
        logging.info(f"Click Canopy And Tent")
        print(f"Click Canopy And Tent")
        self.javascript_clic("Canopy And Tent")

    def click_element_text_of_list(self, lista: list, text: str):
        logging.info(f"Click on: {text}")
        print(f"Click on: {text}")
        for element in lista:
            element_text = element.text
            logging.info(f"***************** {element_text}")
            print(f"***************** {element_text}")
            if text in element_text:
                logging.info(f"Click {text.upper()}S*****************")
                print(f"Click {text.upper()}S*****************")
                self.clic_javacript(element)
                break

    def close_categories(self):
        logging.info(f"Close Categories modal")
        print(f"Close Categories modal")
        self.element("close_categories_x_button").wait_clickable().click()

    def presenceOf_popular_categories_label(self):
        logging.info(f"Presence of Popular Categories Label")
        print(f"Presence of Popular Categories Label")
        try:
            self.element("popular_categories_label").wait_visible()
            return True
        except TimeoutError:
            logging.info(f"Label is not displayed")
            print(f"Label is not displayed")

    def get_text_label_vehicle_selected(self):
        logging.info(f"Get text label of vehicle selected")
        print(f"Get text label of vehicle selected")
        labels = self.element("labels_vehicle_selected").find_elements()
        submodel_label = labels[0].text
        logging.info(f"SUBMODEL LABEL: {submodel_label}")
        print(f"SUBMODEL LABEL: {submodel_label}")
        engine_label = labels[1].text
        engine_label_list = engine_label.split('\n')
        logging.info(f"ENGINE LABEL: {engine_label_list[0]}")
        print(f"ENGINE LABEL: {engine_label}")
        return submodel_label, engine_label

    def get_recent_vehicles_list(self):
        logging.info(f"Get Recent Vehicle List added")
        print(f"Get Recent Vehicle List added")
        lista = self.element("recent_vehicles").find_elements()
        logging.info(f"Elements found: {len(lista)}")
        print(f"Elements found: {len(lista)}")
        # for ele in lista:
        #     logging.info(f"{ele.text}")
        return len(lista)

    def validate_vehicle_list_cleared(self):
        logging.info(f"validate vehicle list cleared")
        print(f"validate vehicle list cleared")
        if self.element("add_vehicle_info_label").wait_visible():
            return True

    def validate_parent_category_list_page(self):
        logging.info(f"Validate parent category list page")
        print(f"Validate parent category list page")
        return self.element("element_buttons_grid_category").wait_clickable()

    def get_link_product_list(self, type_of_label=0):
        """ '0' means the results pages contains 'Search Results' label on top
            '1' means the results pages contains 'Additional' label at bottom
            Returns: a list of elements"""

        logging.info(f"Get Products list")
        print(f"Get Products list")
        self.wait_until_page_load_complete()
        if type_of_label == 1:
            # self.element("additional_label").wait_visible()
            time.sleep(1)
            lista = self.element("link_products_list_2").find_elements()
            if len(lista) != 0:
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
            if len(lista) != 0:
                return lista
            else:
                lista = self.element("link_products_list").find_elements()
                return lista

    def get_popular_category_list(self):
        self.wait_until_page_load_complete()
        logging.info(f"Get popular category list")
        print(f"Get popular category list")
        self.element("popular_categories_label").wait_visible()

        lista = self.element("popular_categories_list_btn").find_elements()
        if len(lista) != 0:
            return lista
        else:
            self.element("popular_categories_label").wait_visible()
            lista = self.element("popular_categories_list_btn").find_elements()
            return lista

    def show_product_list(self, product_list: list):
        logging.info("show product list")
        for product in product_list:
            if type(product) is not str:
                logging.info(product.text)
            else:
                logging.info(product)

    def click_homepage_button(self):
        logging.info(f"Click home page button")
        print(f"Click home page button")
        self.element("homePage_button").wait_clickable().click()

    def get_lasted_viewed_products_list(self):
        logging.info(f"Get Lasted viewed products list")
        print(f"Get Lasted viewed products list")
        self.element('last_viewed_products_label').wait_visible()
        # self.scroll_to_element(self.element('last_viewed_products_label'))
        self.scroll_down()
        lista = []
        # self.element("last_viewed_products_label").scroll_down_to_element()
        lista_0 = self.element("lasted_products_viewed_list").find_elements()
        for element in lista_0:
            element = element.text
            element = element.upper()
            lista.append(element)
        return lista

    def get_lasted_viewed_products_list2(self):
        """
        regresa la lista obtenida sin modificar texto (texto original)
        :return:
        """
        logging.info(f"Get Lasted viewed products list")
        print(f"Get Lasted viewed products list")
        self.element('last_viewed_products_label').wait_visible()
        # self.scroll_to_element(self.element('last_viewed_products_label'))
        self.scroll_down()
        lista = []
        # self.element("last_viewed_products_label").scroll_down_to_element()
        lista_0 = self.element("lasted_products_viewed_list").find_elements()
        return lista_0

    def get_last_research_product_list(self):
        """
        regresa la lista obtenida del search history
        :return:
        """
        logging.info(f"get_last_research_product_list")
        print(f"Get Lasted viewed products list")
        lista_0 = self.element("last_searches_labels").find_elements()
        return lista_0

    def clean_product_selected(self, expected_product_selected: str):
        print(f"clean product selected")
        product_selected = expected_product_selected.split('#')
        product_selected = product_selected[0].split('\n')
        return product_selected[1]

    def get_footer_links_name_href_dict(self):
        logging.info(f"Get Footer links list")
        print(f"Get Footer links list")
        self.element("tools_span").wait_visible()
        dic_name_href = {}
        link_list = self.element("footer_links").find_elements()
        for link in link_list:
            if "’" in link.text:
                llave = link.text.replace("’", "'")
                dic_name_href[llave] = link.get_attribute("href")
            else:
                dic_name_href[link.text] = link.get_attribute("href")
        return dic_name_href

    def get_footer_links_href(self):
        logging.info(f"Get Footer links href(url)")
        print(f"Get Footer links href(url)")
        self.element("tools_span").wait_visible()
        links_href_list = []
        link_list = self.element("footer_links").find_elements()
        for link in link_list:
            links_href_list.append(link.get_attribute('href'))
        return links_href_list

    def click_on_part_interchange_btn(self):
        logging.info(f"Click on 'PART INTERCHANGE' button")
        print(f"Click on 'PART INTERCHANGE' button")
        self.element("part_interchange_linktext").wait_clickable().click()

    def close_part_interchange(self):
        logging.info(f"Close part interchange")
        print(f"Close part interchange")
        self.element("close_part_interchange_x_button").wait_clickable().click()

    def get_text_part_interchange_input(self):
        logging.info(f"Get Text from Part Interchange input tbx")
        print(f"Get Text from Part Interchange input tbx")
        time.sleep(.2)
        texto = self.element("part_interchange_input_tbx").wait_visible().get_attribute('ng-reflect-model')
        # logging.info(f"Text from Part Interchange input tbx: {texto}")
        return texto

    def write_part_in_interchange_tbx(self, part):
        logging.info(f"Write Part in Interchange tbx")
        print(f"Write Part in Interchange tbx")
        self.element("part_interchange_input_tbx").wait_visible().send_keys(part)

    def clear_part_interchange_input_tbx(self):
        logging.info("Clear part interchange input tbx")
        print("Clear part interchange input tbx")
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
        print(f"Click on brands dropdown list")
        self.element("brands_dropdown").wait_visible().click()

    def click_on_show_all_brands(self):
        logging.info(f"Click on show all brands link text ")
        print(f"Click on show all brands link text ")
        self.element("show_all_brands_link").wait_clickable().click()

    def clic_outside_of_modal_window(self):
        logging.info("click outside of modal window")
        print("click outside of modal window")
        self.element("search_bar").wait_visible().send_keys(Keys.ESCAPE)

        # self.element("blank_space").wait_visible().click()
        # element = self.element("blank_space").wait_visible()
        # self.move_to_element_coordinates(element, 0, 0)

    def click_part_interchange_search_btn(self):
        logging.info("Click part interchange search button")
        print("Click part interchange search button")
        self.element("part_interchange_search_button").wait_visible().click()

    def get_part_interchange_step_2_list(self):
        logging.info("Get part interchange step 2 list")
        print("Get part interchange step 2 list")
        self.element("part_interchange_step_2").wait_visible()
        step_2_list = self.element("part_interchange_step_2_list").find_elements()
        # for part_type in step_2_list:
        #     logging.info(part_type.text)

        return step_2_list

    def get_no_results_container_message(self):
        """
        function to get message with locator "no_results_container"
        We're sorry, no results were found
        :return:
        """
        logging.info("Get no results found message")
        print("Get no results found message")
        return self.element("no_results_container").wait_visible().text

    def get_no_results_message(self):
        """
        function to get message with locator "no_results_message"
        We're sorry, no results were found
        :return:
        """
        logging.info("Get message:'We're sorry, no results were found'")
        print("Get message:'We're sorry, no results were found'")
        return self.element("no_results_message").wait_visible().text

    def get_compatibility_meessage(self):
        logging.info("Get does not fit message")
        print("Get does not fit message")
        time.sleep(2)
        # return self.element("does_not_fit_message_label").wait_visible().text
        return self.element("compatibility_message_label").wait_visible().text

    def click_on_logo_oreily_home(self):
        logging.info("Click logo oreilly home")
        print("Click logo oreilly home")
        self.element("img_logo_oreilly_home").wait_visible().click()

    def clic_blank_space(self):
        logging.info("click blank space")
        print("click blank space")
        self.element("blank_space").wait_visible().click()

    def get_random_brand(self):
        """
        selec a random brand
        :return: random brand selected
        """
        logging.info(f"Click Random Brand")
        print(f"Click Random Brand")
        self.element("explore_brands_label").wait_visible()
        brands_list = self.element("all_brands_link_list").find_elements()
        logging.info(f"El numero de marcas son: {len(brands_list)}")
        print(f"El numero de marcas son: {len(brands_list)}")

        index = random.randint(0, len(brands_list))

        brand_selected = brands_list[index].text
        logging.info(f"Brand Selected: {brand_selected}")
        print(f"Brand Selected: {brand_selected}")
        try:
            logging.info(f"Try click on: {brand_selected}")
            print(f"Try click on: {brand_selected}")
            self.javascript_clic(brand_selected)
        except JavascriptException:

            time.sleep(1)
            logging.info(f"Java except click on: {brand_selected}")
            print(f"Try click on: {brand_selected}")
            self.clic_javacript(brands_list[index])
            # brands_list[index].click()
        # brands_list[index].click() funciona original
        return brand_selected

    def get_search_results_number(self):
        logging.info(f"Get search results number")
        print(f"Get search results number")
        try:
            self.element("span_filter_by").wait_visible()
        except TimeoutError:
            try:
                self.element("span_filter_by").wait_visible()
            except TimeoutError:
                try:
                    self.element("search_results_label").wait_visible()
                except TimeoutError:
                    return self.element("no_results_message").wait_visible().text

        self.element("sort_by_dropdown").wait_visible()
        search_results = self.element("search_results_number").wait_visible().text
        logging.info(f"search result label: {search_results}")
        print(f"search result label: {search_results}")
        numero = search_results.replace('(', '').replace(')', '')
        numero = int(numero)
        return numero

    def click_order_by_dropdown_and_select_option(self, option: str):
        """
        Click Order by dropdown and select any of fallowing options:
        :param option: 'Relevance', 'A - Z', 'Z - A'
        :return:
        """
        logging.info(f"Click sort by dropdown and select option: {option}")
        print(f"Click sort by dropdown and select option: {option}")
        self.element("sort_by_label").wait_visible()
        self.element("sort_by_dropdown").wait_clickable().click()
        self.javascript_clic(option)
        time.sleep(3)

    def get_search_message(self):
        logging.info("Get search results message")
        print("Get search results message")
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
        print(f"Connect to DB")
        connection = self.mysql_connection()
        cursor = connection.cursor()
        logging.info(f"Execute query")
        cursor.execute(
            "SELECT * FROM epc.application_vehicle_indexes avi INNER JOIN epc.vehicles v on v.a_vehicle_id = avi.vehicle_id WHERE avi.application_id='161096296'  AND avi.part_type_id = '02512' GROUP BY avi.application_id, avi.vehicle_id;")
        results = cursor.fetchall()
        assert len(results) is not None, "No data to see"
        for result in results:
            logging.info(f"{result}")
            print(f"{result}")
        cursor.close()
        connection.close()

    # ------------------------------------- funciones de Juan

    def select_random_element_of_list(self, lista: list):
        """
        Select and click on a random element of the list given
        :param lista:
        :return: text of element selected
        """
        self.wait_until_page_load_complete()
        logging.info(f"Select a random element of the list")
        index = random.randint(0, len(lista)-1)
        try:
            element_selected = lista[index]
            element_text = element_selected.text

            try:
                self.javascript_clic(element_text)
            except:
                element_selected.click()


            element_text = element_text.upper()
            return element_text
        except IndexError:
            index = random.randint(0, len(lista)-1)
            element_selected = lista[index]
            element_text = element_selected.text
            try:
                element_selected.click()
            except ElementClickInterceptedException:
                self.javascript_clic(element_text)

            element_text = element_text.upper()
            return element_text

    def select_specific_category_of_list(self, lista: list, index=0):
        self.wait_until_page_load_complete()
        element_selected = lista[index]
        element_text = element_selected.text
        logging.info(f"Select {element_text} from the list")

        try:
            element_selected.click()
        except ElementClickInterceptedException:
            self.javascript_clic(element_text)

        element_text = element_text.upper()
        return element_text

    def select_first_subcategory(self):
        logging.info(f"Select the first subcategory in the CLP")
        lista = self.element("category_landing_elements_img").find_elements()
        element_selected = lista[0].text
        logging.info(f"select first element of the list: {element_selected}")
        lista[0].click()
        return element_selected

    def validate_product_list_page_vehicle(self, subcategory_selected, vehicle):

        year, make, model, submodel = vehicle
        make = make.split('\n')[0]
        model = model.split('\n')[0]
        submodel = submodel.split('\n')[0]
        logging.info("Validate product list page")
        # try:
        #     self.element("span_filter_by").wait_visible()
        #     self.element("sort_by_dropdown").wait_visible()
        # except TimeoutError:
        #     self.element("span_filter_by").wait_visible()
        #     self.element("sort_by_dropdown").wait_visible()
        #
        assert self.element(
            "plp_title").find_element().text.lower() == subcategory_selected.lower(), "The subcategory is not match"
        assert self.element(
            "fits_element").find_element().text == f"Fits {make} {model} {year}", "The vehicle don't match"

    def validate_no_products_found(self):
        try:
            if self.element("plp_error").find_element():
                return True
        except NoSuchElementException:
            return False

    def validate_no_results_were_found(self):
        try:
            if self.element("no_results_container").find_element():
                return True
        except NoSuchElementException:
            return False

    def select_vehicle_specific(self):
        self.click_on_Picker_vehicle_btn()
        time.sleep(0.5)
        year = "2021"
        make = "Chevrolet"
        model = "Aveo"
        submodel = "LT"
        self.write_a_vehicle_type("Automotive Light Duty")
        self.write_a_year(year)
        self.write_a_make(make)
        self.write_a_model(model)
        self.write_a_submodel(submodel)
        self.click_on_engine_and_select()
        time.sleep(.5)
        self.click_on_add_vehicle_submit_btn()

        return year, make, model, submodel

    def validate_product_list_page(self, subcategory_selected):

            logging.info("Validate product list page")

            products_number = self.get_search_results_number()

            assert self.element(
                "plp_title").find_element().text.lower() == subcategory_selected.lower(), "The subcategory is not match"
            return products_number


    def validate_pagination(self):

        logging.info("Validate the pagination")
        products_number = self.get_search_results_number()

        if products_number > 20:
            elements_in_page = self.element("no_part_copy_to_clipboard").find_elements()
            assert len(
                elements_in_page) == 20, f"The number of elements: {len(elements_in_page)}  in page is minor than 20"
            logging.info(f"Elements per page: {len(elements_in_page)}")

    def select_random_category_filter(self):
        logging.info("Select a category from Categories filter")
        category_filter = self.element("filter_option_list").find_elements()
        index = 0
        if len(category_filter) > 1:
            index = random.randint(0, len(category_filter))
        category_selected = category_filter[index].text
        logging.info(f"Category Selected: {category_selected}")
        category_filter[index].click()
        return category_selected

    def validate_page_filtered(self, category_selected, total, total_filtered):
        logging.info("Validate filtered")
        category = self.element("filter_option_selected").wait_visible().text
        assert category == category_selected, "The category selected is not match"
        assert total >= total_filtered, "The number of products must be minor when filter"

    def select_brand_filter(self):
        logging.info("Select a brand from Brands filter")
        filter_buttons = self.element("filters_buttons").find_elements()
        filter_buttons[2].click()
        brand = filter_buttons[2].text
        attributes_list = self.element("filter_option_list").find_elements()
        index = random.randint(0, len(attributes_list) - 1)
        attribute_selected = attributes_list[index].text
        logging.info(f"Attribute Selected: {attribute_selected}")
        attributes_list[index].click()

        return brand

    def select_random_attribute(self):
        logging.info("Select an attribute")

        attribute_filter_list = self.element("filters_buttons").find_elements()
        index = random.randint(0, len(attribute_filter_list))
        attribute_selected = attribute_filter_list[index].text
        logging.info(f"Attribute Selected: {attribute_selected}")
        attribute_filter_list[index].click()
        time.sleep(1)
        attribute_option_list = self.element("filter_option_list").find_elements()
        index = random.randint(0, len(attribute_option_list) - 1)
        attribute_option_selected = attribute_option_list[index].text
        logging.info(f"Attribute Option Selected: {attribute_option_selected}")
        attribute_option_list[index].click()
        return attribute_option_selected

    def validate_filtered_page(self, brand_selected, attribute, total, total_filtered):
        logging.info("Validate filtered")
        options = self.element("filter_option_selected").find_elements()
        print(f"{options[0].text} y {brand_selected}")
        print(f"{options[1].text} y {attribute}")
        # assert options[0].text == brand_selected, "The Brand selected is not match"
        # assert options[1].text == attribute, "The attribute is not the correct"
        assert total > total_filtered, "The number of products must be minor when filter"

    def validate_category_landing_page(self, subcategory_selected):
        try:
            if self.element("category_landing_title").find_element().text.upper() == subcategory_selected.upper():
                logging.info(f"Validate categories in landing page")
                total = self.clp_category_result()
                logging.info(f"The total of categories in page = {total}")
                return True
        except NoSuchElementException:
            return False

    def clp_category_result(self):
        logging.info("Get the total of categories on page")
        img_cat = self.element("img_cat_names").find_elements()
        additional = self.element("additional_cat_names").find_elements()
        total = len(img_cat) + len(additional)
        return total

    def get_product_list_2(self):
        logging.info("Get product list 2")
        time.sleep(.5)
        self.wait_until_page_load_complete()
        self.element("link_products_list_2").wait_visible()
        lista = self.element("link_products_list_2").find_elements()
        if len(lista) != 0:
            return lista
        else:
            self.wait_until_page_load_complete()
            self.element("link_products_list_2").wait_visible()
            lista = self.element("link_products_list_2").find_elements()
            return lista

    # *******************FUNCIONES DE LUIS**************************************
    def click_on_brands_images_btn(self):
        time.sleep(1)
        logging.info(f"Click on brands images btn")
        print(f"Click on brands images btn")
        self.element("brands_images").wait_clickable().click()
        time.sleep(3)
        self.scroll_down()
        self.scroll_down()
        self.scroll_down()

    def get_img_part_brand(self):
        logging.info("Get img part brand")

        img = self.element("img_parts_of_brands").wait_visible().text
        return img

    def click_on_search_history(self):
        time.sleep(1)
        logging.info(f"Click on search history btn")
        print(f"Click on search history btn")
        self.element("search_history_link").wait_clickable().click()

    def click_on_last_searches(self):
        time.sleep(1)
        logging.info(f"Click on search history btn")
        print(f"Click on search history btn")
        self.element("search_history_last_searches").wait_clickable().click()

    def clean_search(self):
        logging.info(f"clean Search")
        print(f"clean search")
        self.element("search_bar").clean_element()

    def accept_alert_message(self):
        logging.info(f"accept alert message")
        print(f"accept alert message")
        self.accept_alert_message()

    def click_on_open_search(self):
        time.sleep(1)
        logging.info(f"Click on search history btn")
        print(f"Click on search history btn")
        self.element("open_search").wait_clickable().click()

    def click_on_first_product(self):
        time.sleep(1)
        logging.info(f"Click on search history btn")
        print(f"Click on search history btn")
        self.element("img_of_product").wait_clickable().click()

    def clicks_carousel_last_viewed_products(self):
        logging.info(f"show_last_viewed_products_label")
        print(f"show_last_viewed_products_label")
        self.element("carousel").wait_clickable().click()
        time.sleep(2)
        self.press_page_down()
        time.sleep(2)
        self.element("backward_button_latest").wait_clickable().click()
        self.element("backward_button_latest").wait_clickable().click()
        self.element("backward_button_latest").wait_clickable().click()
        self.element("backward_button_latest").wait_clickable().click()
        time.sleep(4)
        self.element("forward_button_latest").wait_clickable().click()
        self.element("forward_button_latest").wait_clickable().click()
        self.element("forward_button_latest").wait_clickable().click()
        self.element("forward_button_latest").wait_clickable().click()
        time.sleep(3)

    def delete_element_from_open_search(self):
        logging.info(f"delete element from open search")
        print(f"delete element from open search")
        self.element("search_history_criteria").wait_visible()
        # lista = self.element("search_history_criteria").find_elements()
        elemento = self.element("search_history_criteria").wait_clickable()
        # elemento = lista[2]

        self.move_to_element(elemento)
        self.element('button_remove_from_search_history').wait_clickable().click()

        # self.javascript_clic("remove_from_search_history")
        time.sleep(2)

    def search_into_search_history(self, value: str):
        logging.info(f"Search {value}")
        print(f"Search {value}")
        self.element("searchbar_in_search_history").wait_clickable().send_keys(value)

    def clean_searchbar_in_search_history(self):
        logging.info(f"clean Search history")
        print(f"clean search history")
        self.element("searchbar_in_search_history").clean_element()


    def click_clear_search_history_btn(self):
        logging.info(f"click_new_clear_search_history_btn")
        print(f"click_new_clear_search_history_btn")
        self.element("clear_history_btn").wait_clickable().click()
        self.element("clear_search_history_label").wait_visible()
        self.element("clear_search_history_btn").wait_clickable().click()

    def validate_carousel_is_visible(self):
        logging.info(f"validate_carousel_is_visible")
        print(f"validate_carousel_is_visible")
        element = self.element("carousel").wait_visible().is_displayed()
        return element

    def validate_presence_of_oil_product(self):
        logging.info("validate_presence_of_oil_product")
        assert self.element("oil_product_label").find_element().is_displayed(), f"oil product is not displayed"

    def search_specific_product(self, value: str):
        logging.info(f"search_specific_product {value}")
        print(f"search_specific_product {value}")
        self.element("search_bar").wait_clickable().send_keys(value)

    # *******************FIN DE FUNCIONES DE LUIS**************************************

    # -------------------------------------------SPRINT 2-------------------------------------------------------------------
    def select_mex_country(self):
        logging.info("Select MEX in vehicle country selection")
        time.sleep(.5)
        self.element("vehicle_country_checkbox_icons").wait_visible()
        self.element("USA_check").find_element().click()
        self.element("CAN_check").find_element().click()

    def select_usa_can_country(self):
        logging.info("Select USA and CAN in vehicle country selection")
        time.sleep(.5)
        self.element("vehicle_country_checkbox_icons").wait_visible()
        self.element("MEX_check").find_element().click()

    def click_on_year_dropdown(self, index=0):
        time.sleep(.5)
        logging.info("Click on year dropdown")
        print("Click on year dropdown")
        self.element("year_dropdown").wait_clickable().click()
        try:
            year = self.select_index_list_element(index)
        except IndexError:
            year = self.select_index_list_element(index)
        return year

    def get_country_chips(self):
        time.sleep(.5)
        logging.info("Get country chips text")
        lista = self.element("chip_elements").find_elements()
        texto = []
        for e in lista:
            texto.append(e.text)
        return texto

    def click_on_brand(self, brand):
        """
        perform a click action on brand given
        :param brand:
        :return:
        """
        time.sleep(.5)
        logging.info(f"Click on {brand} brand ")
        print(f"Click on {brand} brand ")
        self.element("explore_brand_text").wait_visible()
        if brand == 'Body Glove':
            self.element("bodyglove_brand").find_element().click()
        if brand == 'Cartek':
            self.element("cartek_brand").find_element().click()
        if brand == 'Armor All':
            self.element("armorall_brand").find_element().click()
        if brand == 'Gates':
            self.element("gates_brand").find_element().click()

    def click_on_first_add_to_list_available(self):
        time.sleep(.5)
        logging.info("Click on ADD TO LIST button")
        print("Click on ADD TO LIST button")
        self.element("add_to_list_btn").wait_clickable().click()

    def get_products_names(self):
        time.sleep(.5)
        logging.info("Get the products names")
        print("Get the products names")
        list_name = self.element("product_name").find_elements()
        names = []
        for name in list_name:
            names.append(name.text)
        return names

    def validate_orderList_display(self):
        time.sleep(1)
        logging.info("Validate the order list display")
        print("Validate the order list display")
        self.element("order_list_label").wait_visible()
        title = self.element("panel_title").find_element()
        product = self.element("product_name_ol").find_element()
        return title.text, product.text

    def add_multiple_products_to_order_list(self, qty):
        time.sleep(.5)
        logging.info("Add multiple products to order list")
        print("Add multiple products to order list")
        for i in range(qty):
            self.click_on_first_add_to_list_available()
            self.element("close_modal").find_element().click()
        self.element("order_list_button").wait_visible().click()
        products = self.element("product_name_ol").find_elements()
        product_name = [product.text for product in products]
        return product_name

    def delete_product_from_order_list(self):
        time.sleep(.5)
        logging.info("Delete product from order list")
        print("Delete product from order list")
        self.element("delete_button").wait_clickable().click()
        products = self.element("product_name_ol").find_elements()
        if len(products) == 0:
            label = self.element("no_added_label").wait_visible().text
            return label
        else:
            product_name = [product.text for product in products]
            return product_name

    def delete_all_products(self):
        time.sleep(.5)
        logging.info("Delete all products from order list")
        print("Delete all products from order list")
        self.element("delete_all_button").wait_clickable().click()
        self.element("clear_label").wait_visible()
        self.element("yes_remove_button").wait_clickable().click()
        self.take_screenshot("Delete all successfully")
        label = self.element("no_added_label").wait_visible().text
        return label

    def delete_all_products_cancel(self):
        time.sleep(.5)
        logging.info("Delete all products from order list")
        print("Delete all products from order list")
        self.element("delete_all_button").wait_clickable().click()
        self.element("clear_label").wait_visible()
        self.element("cancel_btn").wait_clickable().click()
        time.sleep(1)
        products = self.element("product_name_ol").find_elements()
        product_name = [product.text for product in products]
        return product_name

    def click_img_thumbnail(self):
        time.sleep(.5)
        logging.info("Click on the image thumbnail")
        print("Click on the image thumbnail")
        self.element("img_thumbnail").wait_clickable().click()

    def get_pdp_title(self):
        time.sleep(.5)
        logging.info("Validate that the PDP is the correct")
        print("Validate that the PDP is the correct")
        title = self.element("pdp_title").find_element().text
        return title

    def get_plp_images(self):
        time.sleep(.5)
        logging.info("Get the plp images")
        print("Get the plp images")
        images = self.element("plp_images").find_elements()
        img_src = [image.get_attribute("src") for image in images]
        return img_src

    def get_plp_fit_notes(self):
        time.sleep(.5)
        logging.info("Get the fitment notes from products")
        print("Get the fitment notes from products")
        fit_notes = self.element("fitment_notes").find_elements()
        return fit_notes

    def wait_spinner_disappears(self):
        logging.info("Wait spinner disappears")
        self.element("loading_img").wait_until_disappears()

    # -------------------------------------------SPRINT 2-------------------------------------------------------------------

    def get_random_brand_icon_list(self):
        logging.info("Click on Random Brand Icon")
        print("Click on Random Brand Icon")
        self.element("explore_bands_icons_h3").wait_visible()
        brand_icon_list = self.element("explore_brand_icons").find_elements()
        return brand_icon_list

    def click_compatibility_tab(self):
        logging.info("Click Compability tab")
        print("Click Contability tab")
        self.element("compatibility_tab").wait_visible()
        self.element("compatibility_tab").wait_clickable().click()

    def click_details_tab(self):
        logging.info("Click Compability tab")
        print("Click Contability tab")
        self.element("details_tab").wait_visible()
        self.element("details_tab").wait_clickable().click()

    def get_compatibility_list(self):
        logging.info("Get Compatibility List")
        print("Get Compatibility List")
        compatibility_list = self.element("compatibility_list_tab").find_elements()
        return compatibility_list

    def get_compatibility_vehicles_table(self):
        logging.info("Get Compatibility Vehicles Table")
        print("Get Compatibility Vehicles Table")
        self.element("compatibility_vehicles_table").wait_visible()
        table_header = self.element("compatibility_vehicles_table").find_elements()
        for header in table_header:
            logging.info(header.text)
            print(header.text)

    def show_compatibility_vehicle_list_tab(self):
        logging.info("Show Compatibility Vehicles list : 'Brand (# cars)'")
        print("Show Compatibility Vehicles list: 'Brand (# cars)'")
        compatibility_vehicle_list = self.element("compatibility_list_span").find_elements()
        for tab in compatibility_vehicle_list:
            tab_list = tab.text
            logging.info(f"{tab_list})")
            print(f"{tab_list})")
            # brand = tab_list[0]
            # cars = tab_list[1]
            # logging.info(f"{brand} ({cars})")
            # print(f"{brand} ({cars})")

    def validate_presence_of_details_sections(self, expected_sections: list):
        """
        compare expected sections list passed, with sections displayed in webpage
        :param expected_sections: list
        :return: assertion
        """
        logging.info("Validate presence of Details sections")
        self.element("details_sections_list").wait_visible()
        sections_list_in_webpage = self.element("details_sections_list").find_elements()
        sections_list_in_webpage_text = []
        for section in sections_list_in_webpage:
            sections_list_in_webpage_text.append(section.text)
        #about_this_brand_section_label = self.element("about_this_brand_section_label").find_element().text
        #sections_list_in_webpage_text.append(about_this_brand_section_label)
        assert sections_list_in_webpage_text == expected_sections, f"sections in webpage: {sections_list_in_webpage_text} should be:: {expected_sections}"

    def get_data_from_detailed_description_section(self):
        logging.info("Get data from details 'detailed description' section")
        product_name = self.element("detailed_description_product_name").find_element().text
        print(product_name)
        lista = self.element("detailed_description_product_list").find_elements()
        for ele in lista:
            print(ele.text)

    def get_data_from_details_product_information_section(self):
        logging.info("Get data from details 'product information' section")
        lista = self.element("product_information_section_list").find_elements()
        for ele in lista:
            print(ele.text)

    def get_data_from_details_how_to_use_the_product_section(self):
        logging.info("Get data from details 'how to use the product' section")
        lista = self.element("how_to_use_the_product_description_list").find_elements()
        for ele in lista:
            print(ele.text)

    def get_data_from_details_about_this_brand_section(self):
        logging.info("Get data from details 'about this brand' section")
        texto = self.element("about_this_brand_text").find_element().text
        print(texto)

        p = self.element("about_this_brand_p").find_element().text
        print(p)

        lista = self.element("about_this_brand_li").find_elements()
        for ele in lista:
            print(ele.text)

    def click_send_a_report_link(self):
        logging.info("Click on send a report link")
        self.element("send_report_btn").wait_visible()
        send_a_report_btn = self.element("send_report_btn").wait_clickable()
        try:
            self.clic_javacript(send_a_report_btn)
        except ElementClickInterceptedException:
            self.javascript_clic('Send a report')

    def fill_product_info_report(self, name: str, email: str, phone: str, store: str, issue_type: str,
                                 description_error_text: str):
        """
        :param name: str
        :param email: str
        :param phone: str
        :param store: str
        :param issue_type: str
        :param description_error_text: str
        :return:
        """
        logging.info("Fill Product Info Report")
        time.sleep(1)
        self.element("product_info_report_label").wait_visible()
        self.write_fullName(name)
        self.write_email(email)
        self.write_phoneNumber(phone)
        self.click_store_dropdown()
        self.select_a_store(store)
        self.element("about_the_issue_span").wait_visible()
        self.press_PageDown_key()
        self.click_issue_type_dropdown()
        self.select_a_issue_type(issue_type)
        self.write_describe_the_issue(description_error_text)

    def write_fullName(self, fullname: str):
        logging.info(f"Write Full Name: {fullname}")
        self.element("input_fullName_tbx").wait_clickable().send_keys(fullname)

    def write_email(self, email: str):
        logging.info(f"Write email: {email}")
        self.element("input_email_tbx").wait_clickable().send_keys(email)

    def write_phoneNumber(self, phone_number: str):
        logging.info(f"Write phone_number: {phone_number}")
        self.element("input_phoneNumber_tbx").wait_clickable().send_keys(phone_number)

    def click_store_dropdown(self):
        logging.info("Click Store dropdown")
        self.element("store_dropdown").wait_clickable().click()

    def select_a_store(self, store: str):
        logging.info(f"Select the Storer: {store}")
        self.javascript_clic(store)

    def click_issue_type_dropdown(self):
        logging.info("Click Issue Type dropdown")
        self.element("issue_type_dropdown").wait_clickable().click()

    def select_a_issue_type(self, issue_type: str):
        logging.info(f"Select the issue: {issue_type}")
        self.javascript_clic(issue_type)

    def write_describe_the_issue(self, description: str):
        logging.info(f"Writing the issue type description")
        self.element("textarea_description_error").wait_clickable().send_keys(description)

    def click_send_report_button_info_report_btn(self):
        logging.info("Clic send report btn product info report")
        self.element("send_report_btn_product_info_report").wait_clickable().click()

    def validate_report_created_confirmation(self):
        logging.info("Validate Report Created confirmation")
        # self.element("report_created_confirmation").wait_visible()
        assert self.element(
            "report_created_confirmation").find_element().is_displayed(), "Expected message is not displayed"

    def get_report_ticket_number(self):
        logging.info("Get Report ticket number")
        assert self.element("report_ticket_number").find_element().is_displayed(), "Ticket number is not displayed"
        ticket_number = self.element("report_ticket_number").wait_visible().text
        logging.info(f"{ticket_number}")
        # print(f"ticket_number: {ticket_number}")
        return ticket_number

    def click_add_to_list_btn(self):
        logging.info("Click 'ADD TO LIST' button")
        self.element("add_to_list_btn").wait_clickable().click()

    def validate_presence_of_modal_order_list_elements(self):
        logging.info("Validate presence of modal order list elements")
        logging.info("Validate presence of order list subtitle")
        assert self.element(
            "modal_order_list_subtitle").find_element().is_displayed(), f"Order list subtitle is not displayed"
        logging.info("Validate presence of Quantity of items in the list")
        assert self.element(
            "modal_order_list_items_number").find_element().is_displayed(), f"Quantity of items is not displayed"
        items_span = self.element("modal_order_list_items_number").find_element().text.lstrip().rstrip().split(" ")
        items = items_span[0]
        logging.info(f"number of items: {items}")
        print(f"number of items: {items}")
        assert self.element(
            "modal_order_list_deleteAll_btn").find_element().is_displayed(), f"Delete All button is not displayed"
        assert self.element(
            "modal_order_list_vehicle_information").find_element().is_displayed(), f"Vehicle information is not displayed"
        vehicle_description = self.element("modal_order_list_vehicle_information").find_element().text
        assert self.element(
            "modal_order_list_product_description").find_element().is_displayed(), f"Product description is not displayed"
        assert self.element(
            "modal_order_list_part_number").find_element().is_displayed(), f"Part number is not displayed"
        assert self.element(
            "modal_order_list_delete_btn").find_element().is_displayed(), f"Delete button is not displayed"
        return vehicle_description

    def validate_nonAplication_product_label(self):
        logging.info("Validate universal product message:'Non Application'")
        assert self.element(
            "nonApplication_message").find_element().is_displayed(), "'Non Applicatioon' messages is not displayed as expected"
        logging.info("universal product message:'Non Application' is displayed correctly")

    def get_number_of_nonApplication_product_label_in_PLP(self):
        logging.info("Get number of 'Non Application' productos in Product List Page")
        number_of_nonApplication = self.element("nonApplication_message").find_elements()
        logging.info(
            f"Exists '{len(number_of_nonApplication)}' 'Non Application' product in the current Product list Page")
        assert len(number_of_nonApplication) > 0, f"At least one 'non Application' product must exists in the list"

    def validate_compatibility_tab_is_not_displayed(self):
        logging.info("validate Compatibility tab is not displayed")
        try:
            self.element("compatibility_tab").find_element().is_displayed()
            assert False, f"Compatibility tab should not be displayed"
        except NoSuchElementException:
            logging.info("Compatibility tab is not displayed Correctly")
            assert True

    def validate_presence_of_default_image_src(self):
        logging.info("validate presence of default image")
        assert self.element(
            "default_img_product").find_element().is_displayed(), f"default image src should be displayed"

    def validate_resources_tab_is_not_displayed(self):
        logging.info("Validate 'Resources' tab is not displayed")
        try:
            self.element("resources_tab").find_element().is_displayed()
            assert False, f"Resources tab should not be displayed"
        except NoSuchElementException:
            logging.info("Resources tab is not displayed Correctly")
            assert True

    def click_resources_tab(self):
        logging.info("Click 'Resources' tab")
        print("Click Resources tab")
        self.element("resources_tab").wait_visible()
        time.sleep(1)
        self.element("resources_tab").wait_clickable().click()

    def click_main_product_img(self):
        logging.info("Click main product img")
        print("Click main product img")
        self.element("main_product_img").wait_visible()
        self.element("main_product_img").wait_clickable().click()

    def click_img_arrow_back_button(self):
        logging.info("Click img arrow back button")
        print("Click img arrow back button")
        self.element("img_arrow_back_button").wait_visible()
        self.element("img_arrow_back_button").wait_clickable().click()

    def click_img_arrow_forward_button(self):
        logging.info("img arrow forward button")
        print("img arrow forward button")
        self.element("img_arrow_forward_button").wait_visible()
        self.element("img_arrow_forward_button").wait_clickable().click()

    def select_first_suggestion_brand(self, keyword: str):
        logging.info("Select first suggestion brand")

        print(f"Search product: {keyword}")
        search_bar = self.element("search_bar").wait_clickable()
        search_bar.send_keys(keyword)
        time.sleep(1)
        self.element("first_suggestion_brand_highlight").wait_visible()
        self.element("first_suggestion_brand_highlight").wait_clickable().click()

    def validate_keyword_in_p_text_of_results_list(self, keyword: str):
        logging.info("Get 'p' text of results list")
        self.element("product_name").wait_visible()
        p_text_list = self.element("product_name").find_elements()
        for p in p_text_list:
            assert keyword.upper() in p.text.upper(), f"The keyword: '{keyword.upper()}' should be appears in {p.text.upper()}"

    # ****************************************************Grecia************************************
    def get_description_product(self):
        logging.info("Get description product")
        description_text_list = []
        description_list = self.element("description_product_result").find_elements()
        for description in description_list:
            description_text_list.append(description.text)
        return description_text_list

    def get_suggestion_list(self):
        logging.info("Get suggestion list")
        suggestion_text_list = []
        lista = self.element("suggestion_list").find_elements()
        for suggestion in lista:
            suggestion_text_list.append(suggestion.text)
        return suggestion_text_list

    def click_help_center(self):
        logging.info("Scroll down and click in Help Center button")
        self.scroll_down()
        self.element("help_center_btn").find_element().click()

# Phase 2 sprint 1-------------------------------------------------------------------------------------------------

    def click_on_video(self):
        logging.info("Click on video")
        print("Click on video")
        self.element("video_resources_span").wait_visible()
        self.element("internal_video_player_resource").wait_clickable().click()
        self.wait_until_page_load_complete()
        print("switch to iframe")
        self.element("video_player_iframe").switch_to_iframe()
        self.element("youtube_play_button").wait_clickable().click()
        time.sleep(2)

    def validate_hidden_video_resource(self):
        logging.info("Validate hidden video resource")
        print("Validate ihidden video resource")

        try:
            self.element("video_resources_span").wait_visible()
        except:
            print("Video resource does not visible as expected")
            return True

    def click_random_related_product(self):
        logging.info("Click a Related Product")
        print("Click a Related Product")
        self.element("related_products_span").wait_visible()
        related_items = self.element("related_products_carousel_items").find_elements()
        n_elementos = len(related_items)
        index = random.randint(0, n_elementos)
        self.clic_javacript(related_items[index])

    def click_random_related_Category(self):

        logging.info("Click a Related Category")
        print("Click a Related Category")
        self.element("related_categories_span").wait_visible()
        related_items = self.element("related_category_carousel_items").find_elements()
        n_elementos = len(related_items)
        index = random.randint(0, n_elementos)
        self.clic_javacript(related_items[index])

    def validate_hidden_related_product(self):
        logging.info("Validate hidden related product")
        print("Validate hidden related product")

        try:
            self.element("related_products_span").wait_visible()
        except:
            print("related product does not visible as expected")
            return True
    def validate_hidden_related_cateogory(self):
        logging.info("Validate hidden related category")
        print("Validate hidden related category")

        try:
            self.element("related_categories_span").wait_visible()
        except:
            print("related category does not visible as expected")
            return True
    def validate_help_center_page(self):
        time.sleep(1)
        logging.info("Validate that Help Center page is loaded")
        assert self.element("hcp_title").find_element().text == "Centro de ayuda", "The title should be 'Centro de ayuda'"
        assert self.element("hcp_faq_title").find_element().text == "Preguntas frecuentes", "The FAQ´s title should be 'Preguntas frecuentes'"
        assert self.element("hcp_videos_section").find_element().text == "Videos de apoyo", "The videos section title should be 'Videos de apoyo'"
        assert self.element("hcp_issue_report").find_element().text == "REPORTAR UN INCIDENTE", "The issue report button title should be 'REPORTAR UN INCIDENTE'"

    def validate_issue_report_modal(self):
        logging.info("Validate that the issue report modal is displayed in page")
        time.sleep(1)
        assert self.element("irm_title").find_element().text == "Reporte de incidente","The modal's title should be 'Reporte de incidente'"
        assert self.element("irm_user_info").find_element().text == "Información del usuario", "The user info section title should be 'Información del usuario'"
        assert self.element("irm_about_issue").find_element().text == "Acerca del incidente", "The about issue section title should be 'Acerca del incidente'"
        assert self.element("irm_issue_description").find_element().text == "Describe el incidente", "The issue description title should be 'Describe el incidente'"
        assert self.element("irm_submit_btn").find_element().is_displayed(), "The 'Enviar Informe' button should be present"

    def validate_error_messages(self, messages:list):
        logging.info("Validate that the error messages are displayed")
        expected_messages = ["Por favor, escriba un NIP.", "Por favor, escribe un correo electrónico válido","Por favor, escribe un nombre",
                             "Por favor, seleccione un campo.", "Por favor, seleccione un campo.", "Por favor, escribe una descripción"]
        count = 0
        for message in messages:
            if message in expected_messages:
                logging.info(f"Error message: {message}")
                count = count + 1
            if count == 0: logging.info("No error message in page")
        #count = sum(1 for message in messages if message in expected_messages)

        return count

    def select_incident_type(self):
        self.element("irm_incidentType").find_element().click()
        time.sleep(1)
        options = self.element("irm_dropdown_options").find_elements()
        selection = self.select_random_element_of_list(options)
        logging.info(f"Option selected '{selection}'")

    def select_frequency(self):
        self.element("irm_frequency").find_element().click()
        time.sleep(1)
        options = self.element("irm_dropdown_options").find_elements()
        selection = self.select_random_element_of_list(options)
        logging.info(f"Option selected '{selection}'")

    def select_random_video(self):
        videos = self.element("hcp_video_button").find_elements()
        index = random.randint(0, len(videos) - 1)
        try:
            self.scroll_to_element("hcp_paginator")
        except JavascriptException:
            pass
        videos[index].click()
        self.wait_until_page_load_complete()
        return self.switch_to_window()
    def get_video_titles(self):
        videos_titles = self.element("hcp_video_title").find_elements()
        title_txt = [title.text for title in videos_titles]
        return title_txt