import logging
import random
import time
import mysql.connector
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
        general_category_list = self.element("general_category_list").find_elements()
        # logging.info(f"El tamaño de la lista general:{len(general_category_list)}")
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
        logging.info(f"Select a random element of the list")
        index = random.randint(0, len(lista))
        element_selected = lista[index]
        element_text = element_selected.text
        element_text = element_text.upper()
        logging.info(f"Element selected: {element_text}")
        element_selected.click()
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
            index = random.randint(0, n_elementos)
            time.sleep(.2)
            element_selected = lista[index].text
            logging.info(f"select element on the list with index: {index}: {element_selected}")
            lista[index].click()
        else:
            index = 0
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

    def validate_parent_category_list_page(self):
        logging.info(f"Validate parent category list page")
        return self.element("element_buttons_grid_category").wait_clickable()

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

