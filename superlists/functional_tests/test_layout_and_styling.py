"""Tests for feature: to-do list is pretty - css is loaded."""

from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512, delta=5
        )

        # She starts a new list and sees the imput is nicly centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_item_in_table('testing')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512, delta=5
        )