from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from resources.constants import *


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_input = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, SEARCH_INPUT_FIELD)))
        self.contactus_button = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, CONTACTUS_BTN)))
        self.tshirts_category = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, TSHIRTS_CATEGORY)))

    def perform_search(self, term):
        self.search_input.send_keys(term)
        self.search_input.send_keys(Keys.ENTER)

    def navigate_to_contact(self):
        self.contactus_button.click()

    def navigate_to_tshirts_category(self):
        self.tshirts_category.click()
