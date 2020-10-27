from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from resources.constants import *


class ContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.form_subject_dropdown = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, FORM_SUBJECT_DROPDOWN)))
        self.form_email_input = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, FORM_EMAIL)))
        self.form_order_input = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, FORM_ORDER_REFERENCE)))
        self.form_attachment_input = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, FORM_ATTACHMENT)))
        self.form_message_input = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, FORM_MESSAGE)))
        self.form_submit_btn = WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, FORM_SUBMIT_MESSAGE_BTN)))

    def verify_form_is_present(self):
        WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, FORM)))

    def verify_subject_required(self):
        self.verify_form_is_present()
        self.form_email_input.send_keys(VALID_EMAIL)
        self.form_message_input.send_keys(TEST)
        self.form_submit_btn.click()
        WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, ERROR_ALERT)))

    def verify_email_required(self):
        self.verify_form_is_present()
        Select(self.form_subject_dropdown).select_by_value("1")
        self.form_message_input.send_keys(TEST)
        self.form_submit_btn.click()
        WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, ERROR_ALERT)))

    def verify_message_required(self):
        self.verify_form_is_present()
        Select(self.form_subject_dropdown).select_by_value("2")
        self.form_email_input.send_keys(VALID_EMAIL)
        self.form_submit_btn.click()
        WebDriverWait(self.driver.instance, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, ERROR_ALERT)))
