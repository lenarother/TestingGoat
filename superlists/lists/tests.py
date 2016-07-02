from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTests(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        find = resolve('/')
        self.assertEqual(find.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # passing request to render_to_string makes
        # this function work with crsf_token
        expected_html = render_to_string(
            'home.html',
            {'item_text': 'A new list item'},
            request=request)

        self.assertEqual(expected_html, response.content.decode())

    def test_home_page_can_save_a_POST_requet(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
