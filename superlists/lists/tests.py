from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item


class HomePageTests(TestCase):
    """View tests."""

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


class ItemModelTest(TestCase):
    """Model tests."""

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
