"""Testing feature: create and fill in an individual list."""


from unittest import skip
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions

from .base import FunctionalTest


class InputValidationTest(FunctionalTest):

    @skip("for later")
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty imput box.

        # The hompe page refreshes, and there is an error massage saying
        # the list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversly, she now decides to submit a second blank item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
