"""
Testing the to-do-list application from user point of view.
(Functional test / black box test / acceptance test)
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # setup firefox_capabilities since Firefox driver isnot working
        # since Firefox 47.0 and will be disabled in the future
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        self.browser = webdriver.Firefox(capabilities=firefox_capabilities)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table_list(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invinted to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        expected_text = 'Enter a to-do item'
        self.assertEqual(inputbox.get_attribute('placeholder'), expected_text)

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tring fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy peacock feathers" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_table_list('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her lists
        self.check_for_row_in_table_list('1: Buy peacock feathers')
        self.check_for_row_in_table_list(
            '2: Use peackok feathers to make a fly'
        )

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explenatory text to that effect.
        self.fail('Finish the test!')

        # She visits the URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main(warnings='ignore')
