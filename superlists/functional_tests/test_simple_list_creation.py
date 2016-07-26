"""Tests for feature: create and fill in an individual list."""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invinted to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        expected_text = 'Enter a to-do item'
        self.assertEqual(inputbox.get_attribute('placeholder'), expected_text)

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tring fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, she is taken to a new URL,
        # and now the page lists "1: Buy peacocks feathers" as an item in a
        # to-do list table
        inputbox.send_keys(Keys.ENTER)
        # Wait until ENTER is sent and Buy... appears in the table
        self.wait_for_item_in_table('Buy peacock feathers')
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_table_list('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        # Wait until ENTER is sent and Use... appears in the table
        self.wait_for_item_in_table('Use peacock feathers to make a fly')
        self.check_for_row_in_table_list('1: Buy peacock feathers')
        self.check_for_row_in_table_list(
            '2: Use peacock feathers to make a fly'
        )
        # Now a new user, Francis, comes along to the site.

        # We use a new browser session to make sure that no information
        # of Edith's is coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox(
            capabilities=self.firefox_capabilities
        )

        # Francis visits the home page. There is no sign of Edith's
        # list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Wait until ENTER is sent and Buy milk appears in the table
        self.wait_for_item_in_table('Buy milk')
        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Make a fly', page_text)

        # Satisfied, they both go back to sleep
