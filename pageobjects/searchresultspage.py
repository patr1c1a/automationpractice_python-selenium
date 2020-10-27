from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from resources.constants import *


class SearchResults:

    def __init__(self, driver):
        self.driver = driver
        self.search_results_heading = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, SEARCH_HEADING)))

    def get_search_results(self):
        search_results_array = self.driver.instance.find_elements_by_css_selector(SEARCH_RESULTS_ARRAY)
        return search_results_array

    def verify_results_contain_term(self, results, term):
        for result in results:
            assert term in result.get_attribute("title").lower(), "Search term not included in search result."

    def select_product(self, selector):
        product = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, selector)))
        product.click()
