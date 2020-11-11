import unittest
from webdriver import Driver
from resources.constants import *
from pageobjects.homepage import HomePage
from pageobjects.contactpage import ContactPage


class TestsContact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver()

    def setUp(self):
        self.driver.navigate(BASE_URL)

    def test_contactus_subject_required(self):
        """
        Verify subject is required when sending a message using "contact us" form.
        """
        home_page = HomePage(self.driver)
        home_page.navigate_to_contact()
        contact_page = ContactPage(self.driver)
        contact_page.verify_subject_required()

    def test_contactus_email_required(self):
        """
        Verify email is required when sending a message using "contact us" form.
        """
        home_page = HomePage(self.driver)
        home_page.navigate_to_contact()
        contact_page = ContactPage(self.driver)
        contact_page.verify_email_required()

    def test_contactus_message_required(self):
        """
        Verify message is required when sending a message using "contact us" form.
        """
        home_page = HomePage(self.driver)
        home_page.navigate_to_contact()
        contact_page = ContactPage(self.driver)
        contact_page.verify_message_required()

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
