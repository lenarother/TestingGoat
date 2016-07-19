"""Teasting feature: to-do list is pretty - css is loaded."""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512, delta=5
        )

        # She starts a new list and sees the imput is nicly centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "id_list_table"), 'testing')
        )
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512, delta=5
        )
