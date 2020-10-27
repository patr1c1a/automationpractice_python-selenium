from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from resources.constants import *


class TShirtsCategoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_input = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, PRODUCT_LIST)))

    def select_first_product(self):
        first_product = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, PRODUCT_FROM_FIRST_COLUMN)))
        first_product.click()
