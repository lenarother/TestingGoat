"""Testing feature: create and fill in an individual list."""


# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from .base import FunctionalTest


class InputValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty imput box.
        self.browser.get(self.server_url)
        # self.browser.find_element_by_id('id_new_item').send_keys('\n')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # The hompe page refreshes, and there is an error massage saying
        # the list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_table_list('1: Buy milk')

        # Perversly, she now decides to submit a second blank item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.check_for_row_in_table_list('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "id_list_table"), 'Make tea')
        )
        self.check_for_row_in_table_list('1: Buy milk')
        self.check_for_row_in_table_list('2: Make tea')
