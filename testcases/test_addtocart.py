import unittest
from webdriver import Driver
from resources.constants import *
from pageobjects.homepage import HomePage
from pageobjects.tshirstcategorypage import TShirtsCategoryPage
from pageobjects.productpage import ProductPage
from pageobjects.searchresultspage import SearchResults


class TestsContact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver()

    def setUp(self):
        self.driver.navigate(BASE_URL)

    def test_cart_add_product_from_category_page(self):
        """
        Verify a product can be added to cart from a product category page.
        """
        home_page = HomePage(self.driver)
        home_page.navigate_to_tshirts_category()
        tshirts_page = TShirtsCategoryPage(self.driver)
        tshirts_page.select_first_product()
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()

    def test_cart_add_product_from_search_results(self):
        """
        Verify a product can be added to cart by selecting it from search results listing.
        """
        home_page = HomePage(self.driver)
        home_page.perform_search(SEARCH_TERM)
        search_page = SearchResults(self.driver)
        search_page.select_product(PRODUCT_FROM_FIRST_COLUMN)
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
