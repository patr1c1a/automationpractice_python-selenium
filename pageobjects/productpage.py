from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from resources.constants import *


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_input = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, PRODUCT_DESCRIPTION)))

    def add_to_cart(self):
        add_btn = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, ADD_TO_CART)))
        add_btn.click()
        WebDriverWait(self.driver.instance, 10).until(ec.visibility_of_element_located((
            By.CSS_SELECTOR, PRODUCT_ADDED_CONFIRMATION_DIALOG)))
