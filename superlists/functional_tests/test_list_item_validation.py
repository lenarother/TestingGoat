"""Tests for feature: user sees warning on sending invalid input ."""


# from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class InputValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty imput box.
        self.browser.get(self.server_url)
        # self.browser.find_element_by_id('id_new_item').send_keys('\n')
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        # The hompe page refreshes, and there is an error massage saying
        # the list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_table_list('1: Buy milk')

        # Perversly, she now decides to submit a second blank item
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.check_for_row_in_table_list('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_item_in_table('Make tea')
        self.check_for_row_in_table_list('1: Buy milk')
        self.check_for_row_in_table_list('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy wellies')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_item_in_table('Buy wellies')
        self.check_for_row_in_table_list('1: Buy wellies')

        # She accidentally tries to enter a duplicated item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy wellies')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_item_in_table('Buy wellies')

        # She sees a helpful error message
        self.check_for_row_in_table_list('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got it in your list")

    def test_error_messages_are_cleared_on_input(self):
        # Edith starts a new list in a way taht causes a validation error
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts writing in the input box to clear the error
        inputbox = self.get_item_input_box()
        inputbox.send_keys('a')

        # She is pleased to see that the error message dissapears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
