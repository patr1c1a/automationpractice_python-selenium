import unittest
from webdriver import Driver
from resources.constants import *
from pageobjects.homepage import HomePage
from pageobjects.searchresultspage import SearchResults


class TestsSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver()

    def setUp(self):
        self.driver.navigate(BASE_URL)

    def test_search_results_consistent(self):
        """
        Verify every search result includes the search term used.
        """
        home_page = HomePage(self.driver)
        home_page.perform_search(SEARCH_TERM)
        search_page = SearchResults(self.driver)
        results = search_page.get_search_results()
        search_page.verify_results_contain_term(results, SEARCH_TERM)

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
