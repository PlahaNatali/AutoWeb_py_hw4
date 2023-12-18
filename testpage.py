import logging

import yaml

from base_page import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operate with {element_name}')
            return False

        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        field = self.find_element(locator, timeout=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None

        logging.debug(f'We find text {text} in field {element_name}')
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click {element_name} button')
            return False

        logging.debug(f'Clicked {element_name} button')
        return True

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description="password form")

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description="login")

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'])

    def get_text_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_LOGIN_RESULT'])

    def click_new_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_NEW_POST_BTN'], description="new post")

    def enter_new_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NEW_POST_TITLE_FIELD'], word, description="new post title")

    def click_save_new_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_NEW_POST_SAVE_BTN'], description="save new post")

    def get_post_title(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_POST_TITLE_FIELD'])

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description="contact")

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_NAME_INPUT'], word, description="contact name")

    def enter_contact_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_EMAIL_INPUT'], word, description="contact email")

    def enter_contact_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_CONTENT_INPUT'], content, description="contact content")

    def click_contact_contact_us_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_CONTACT_US_BTN'], description="contact us")