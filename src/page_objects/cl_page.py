import logging
import random
import time
import mysql.connector
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from src.page_objects.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class CLPage(BasePage):

    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(CLPage, self).__init__(driver, wait_driver)

    def click_on_categories_button_and_select_pupular_first_category(self):
        logging.info(f"Click on categories button")
        self.element("categories_btn").wait_clickable().click()
        logging.info(f"selecting a popular category")
        self.select_first_popular_category()

    def click_on_categories_button(self):
        logging.info(f"Click on categories button")
        self.element("categories_btn").wait_clickable().click()

    def get_general_categories_list(self):
        logging.info(f"Get General Category List")
        self.element("list_container").wait_visible()
        general_category_list = self.element("general_category_list").find_elements()
        # logging.info(f"El tamaño de la lista general:{len(general_category_list)}")
        return general_category_list

    def get_subcategory_list(self):
        logging.info(f"Get subcategory List")
        self.element("label_subcategory_selected").wait_visible()
        self.element("list_container").wait_visible()
        subcategory_list = self.element("subcategory_list").find_elements()
        return subcategory_list

    def get_text_label_subcategory_selected(self):
        logging.info(f"Get label text of subcategory selected")
        subcategory_label = self.element("label_subcategory_selected").wait_visible()
        return subcategory_label.text

    def select_random_element_of_list(self, lista: list):
        self.wait_until_page_load_complete()
        logging.info(f"Select a random element of the list")
        index = random.randint(0, len(lista))
        try:
            element_selected = lista[index-1]
            element_text = element_selected.text

            try:
                element_selected.click()
            except ElementClickInterceptedException:
                self.javascript_clic(element_text)

            element_text = element_text.upper()
            return element_text
        except IndexError:
            index = random.randint(0, len(lista))
            element_selected = lista[index-1]
            element_text = element_selected.text

            try:
                element_selected.click()
            except ElementClickInterceptedException:
                self.javascript_clic(element_text)

            element_text = element_text.upper()
            return element_text

    def click_first_parent_category_on_breadcrumb(self):
        logging.info(f"click on first parent category on breadcrumb")
        lista = self.element("breadcrum_section_link_list").find_elements()
        logging.info(f"select first element on the list: {lista[1].text}")
        first_element = lista[1].text
        lista[1].click()
        return first_element

    def select_index_list_element(self, index=0):
        logging.info(f"Get element list")
        lista = self.element("list_box").find_elements()

        if index != 0:
            n_elementos = len(lista)
            index = random.randint(0, n_elementos-1)
            time.sleep(.2)
            element_selected = lista[index].text
            logging.info(f"select element on the list with index: {index}: {element_selected}")
            lista[index].click()
        else:
            index = 1
            time.sleep(.2)
            element_selected = lista[index].text
            logging.info(f"select element on the list with index: {index}: {element_selected}")
            lista[index].click()

        return element_selected

    def select_first_popular_category(self):
        logging.info(f"Select the first popular category in the list")

        lista = self.element("popular_categories_list_btn").find_elements()
        logging.info(f"select first element of the list: {lista[0].text}")
        first_element = lista[0].text
        lista[0].click()
        return first_element

    def get_link_product_list(self):
        logging.info(f"Get Products list")
        lista = self.element("link_products_list").find_elements()
        return lista

    def get_popular_category_list(self):
        logging.info(f"Get popular category list")
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
        # self.scroll_down()
        lista = []
        # self.element("last_viewed_products_label").scroll_down_to_element()
        lista_0 = self.element("lasted_products_viewed_list").find_elements()
        for element in lista_0:
            element = element.text
            element = element.upper()
            lista.append(element)
        return lista

    # def validate_category_landing_page(self):
    #     try:
    #         self.element("category_landing_title").find_element()
    #         logging.info(f"Validate category landing page")
    #         return self.element("category_landing_title").find_element().text
    #     except NoSuchElementException:
    #         return False
    def validate_category_landing_page(self, subcategory_selected):
        try:
            if self.element("category_landing_title").find_element().text == subcategory_selected:
                logging.info(f"Validate categories in landing page")
                total = self.clp_category_result()
                logging.info(f"The total of categories in page = {total}")
                return True
        except NoSuchElementException:
            return False

    def validate_product_list_page(self, subcategory_selected):
        try:
            if self.element("plp_title").find_element().text.upper() == subcategory_selected:
                logging.info("Validate product list page")
                total = self.get_search_results_number()
                logging.info(f"The total of products = {total}")
                return True
        except NoSuchElementException:
            return False

    def validate_no_products_found(self):
        try:
            if self.element("plp_error").find_element():
                return True
        except NoSuchElementException:
            return False

    def clp_category_result(self):
        logging.info("Get the total of categories on page")
        img_cat = self.element("img_cat_names").find_elements()
        additional = self.element("additional_cat_names").find_elements()
        total = len(img_cat) + len(additional)
        return total

    def get_search_results_number(self):
        logging.info(f"Get search results number")
        try:
            self.element("span_filter_by").wait_visible()
            self.element("sort_by_dropdown").wait_visible()
        except TimeoutError:
            self.element("span_filter_by").wait_visible()
            self.element("sort_by_dropdown").wait_visible()


        search_results = self.element("search_results_label").find_element().text
        logging.info(f"search result label: {search_results}")
        cadena_l = search_results.split('(')
        numero = cadena_l[1].replace(')', '')
        numero = int(numero)
        return numero

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
        cursor.execute(
            "SELECT * FROM epc.application_vehicle_indexes avi INNER JOIN epc.vehicles v on v.a_vehicle_id = avi.vehicle_id WHERE avi.application_id='161096296'  AND avi.part_type_id = '02512' GROUP BY avi.application_id, avi.vehicle_id;")
        results = cursor.fetchall()
        assert len(results) is not None, "No data to see"
        for result in results:
            logging.info(f"{result}")
        cursor.close()
        connection.close()

    def click_on_Picker_vehicle_btn(self):
        time.sleep(1)
        logging.info(f"Click on Picker vehicle btn")
        self.element("add_vehicle_btn").wait_clickable().click()

    def click_on_vehicle_type_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        # logging.info(f"waiting for vehicle country checkbox icons")
        # self.element("vehicle_country_checkbox_icons").wait_visible()
        logging.info(f"Click on Vehicle dropdown")
        dropdown = self.element("vehicle_type_dropdown").wait_clickable()
        dropdown.click()
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
        year = self.select_index_list_element(index)
        return year

    def click_on_make_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.3)
        # logging.info(f"Click on make dropdown")
        # dropdown = self.element("make_dropdown").wait_visible()
        # dropdown.click()
        logging.info(f"Select Make from list")
        make = self.select_index_list_element(index)
        return make

    def click_on_model_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.2)
        # logging.info(f"Click on model dropdown")
        # dropdown = self.element("model_dropdown").wait_visible()
        # dropdown.click()
        # time.sleep(.2)
        # # dropdown.click()
        # # dropdown.click()
        logging.info(f"Select Model from list")
        self.select_index_list_element(index)

    def click_on_submodel_and_select(self, index=0):
        """
        Input is '0' by default and it will return the first element of the list
        input any other character and it will return a random element in the list
        :param index:
        :return:
        """
        time.sleep(.2)
        # logging.info(f"Click on submodel dropdown")
        # dropdown = self.element("submodel_dropdown").wait_clickable()
        # dropdown.click()
        logging.info(f"Select submodel from list")
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
        # logging.info(f"Click on engine dropdown")
        # dropdown = self.element("engine_dropdown").wait_clickable()
        # dropdown.click()
        logging.info(f"Select Engine from list")
        engine = self.select_index_list_element(index)
        return engine

    def click_on_add_vehicle_submit_btn(self):
        logging.info(f"Click on Add vehicle submit button")
        self.element("add_vehicle_button_submit").wait_clickable().click()

    def get_vehicle_selected(self):
        # era 1.5
        time.sleep(1.5)
        logging.info(f"Get vehicle selected text")
        return self.element("vehicle_selected").wait_visible().text