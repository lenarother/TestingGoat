"""
Base case for testing the to-do-list application from user point of view.

(Base for Functional test / black box test / acceptance test)
"""

import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        # setup firefox_capabilities since Firefox driver isnot working
        # since Firefox 47.0 and will be disabled in the future
        self.firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.firefox_capabilities['marionette'] = True
        self.browser = webdriver.Firefox(
            capabilities=self.firefox_capabilities
        )
        self.browser.implicitly_wait(15)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table_list(self, row_text):
        texts = [
            el.text for el in self.browser.find_elements_by_tag_name('tr')
        ]
        self.assertIn(row_text, texts)

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def wait_for_item_in_table(self, item):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "id_list_table"), item)
        )
        return
