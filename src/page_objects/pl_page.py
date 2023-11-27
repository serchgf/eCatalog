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


class PLPage(BasePage):

    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(PLPage, self).__init__(driver, wait_driver)


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
            element_selected = lista[index - 1]
            element_text = element_selected.text

            try:
                element_selected.click()
            except ElementClickInterceptedException:
                self.javascript_clic(element_text)

            element_text = element_text.upper()
            return element_text
        except IndexError:
            index = random.randint(0, len(lista))
            element_selected = lista[index - 1]
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

    def select_index_list_element(self, index=0):
        logging.info(f"Get element list")
        time.sleep(0.5)
        lista = self.element("list_box").find_elements()
        element_selected = lista[index].text
        logging.info(f"Element selected: {element_selected}")
        lista[index].click()
        return element_selected

    def select_first_subcategory(self):
        logging.info(f"Select the first subcategory in the CLP")
        lista = self.element("category_landing_elements_img").find_elements()
        element_selected = lista[0].text
        logging.info(f"select first element of the list: {element_selected}")
        lista[0].click()
        return element_selected

    def get_link_product_list(self):
        logging.info(f"Get Products list")
        lista = self.element("link_products_list").find_elements()
        return lista

    def get_popular_category_list(self):
        logging.info(f"Get popular category list")
        lista = self.element("popular_categories_list_btn").find_elements()
        return lista

    def click_homepage_button(self):
        logging.info(f"Click home page button")
        self.element("homePage_button").wait_clickable().click()

    def validate_product_list_page_vehicle(self, subcategory_selected, vehicle):

        year, make, model, submodel, engine = vehicle
        make = make.split('\n')[0]
        model = model.split('\n')[0]
        submodel = submodel.split('\n')[0]
        logging.info("Validate product list page")
        try:
            self.element("span_filter_by").wait_visible()
            self.element("sort_by_dropdown").wait_visible()
        except TimeoutError:
            self.element("span_filter_by").wait_visible()
            self.element("sort_by_dropdown").wait_visible()

        assert self.element("plp_title").find_element().text == subcategory_selected, "The subcategory is not match"
        assert self.element("fits_element").find_element().text == f"Fits {make} {model} {year}", "The vehicle don't match"



    def validate_no_products_found(self):
        try:
            if self.element("plp_error").find_element():
                return True
        except NoSuchElementException:
            return False

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


    def click_on_Picker_vehicle_btn(self):
        time.sleep(1)
        logging.info(f"Click on Picker vehicle btn")
        self.element("add_vehicle_btn").wait_clickable().click()


    def click_on_add_vehicle_submit_btn(self):
        logging.info(f"Click on Add vehicle submit button")
        self.element("add_vehicle_button_submit").wait_clickable().click()

    def get_vehicle_selected(self):
        # era 1.5
        time.sleep(1.5)
        logging.info(f"Get vehicle selected text")
        return self.element("vehicle_selected").wait_visible().text

    def select_vehicle_specific(self):

        self.click_on_Picker_vehicle_btn()
        time.sleep(0.5)
        self.element("year_input").find_element().send_keys("2021")
        self.element("autocomplet_panel").wait_visible()
        year = self.select_index_list_element()

        self.element("make_input").find_element().send_keys("Toyota")
        self.element("autocomplet_panel").wait_visible()
        make = self.select_index_list_element()

        self.element("model_input").find_element().send_keys("Rav4")
        self.element("autocomplet_panel").wait_visible()
        model = self.select_index_list_element()

        self.element("submodel_input").find_element().send_keys("XLE")
        self.element("autocomplet_panel").wait_visible()
        submodel = self.select_index_list_element()

        self.element("autocomplet_panel").wait_visible()
        engine = self.select_index_list_element()

        self.click_on_add_vehicle_submit_btn()

        return year, make, model, submodel, engine

    def validate_product_list_page(self, subcategory_selected):

        logging.info("Validate product list page")
        try:
            self.element("span_filter_by").wait_visible()
            self.element("sort_by_dropdown").wait_visible()
        except TimeoutError:
            self.element("span_filter_by").wait_visible()
            self.element("sort_by_dropdown").wait_visible()

        assert self.element("plp_title").find_element().text == subcategory_selected, "The subcategory is not match"

    def validate_pagination(self):

        logging.info("Validate the pagination")
        products_number = self.get_search_results_number()

        if products_number > 20:
            elements_in_page = self.element("part_number").find_elements()
            assert len(elements_in_page) == 20, "The number of elements in page is minor than 20"
            logging.info(f"Elements per page: {len(elements_in_page)}")

