# Tutuorial on TDD with Django based on:

[Test-Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754/)

# Part I

### Session 1: 03.06.2016
* functional test with plain assert

### Session 2: 05.06.2016
* functional test with user story
* functional test uses now unittest
* use **implicitly_wait** from selenium

### Session 3: 10.06.2016
* starting app: manage.py startapp name
* using both functional and unit tests
* Django unit test runner
* **Django.core.urlresolver.resolve**, and urls
* view function, **Django.http.HttpRequest**, **Django.http.HttpResponse**

### Session 4: 11.06.2016
* django.template.loader.render_to_string
* testing whether right template is rendered: resonse.content.decode(), **render_to_string()**
* selenium: **find_element_by_id**, **find_element[s]_by_tag_name**, **send_keys**, **Keys.ENTER**

### Session 5: 04.06.2016
* html form: <fomr method="POST"></form>
* Cross site request forgery {% csrf_token %}
* redirect after POST
* models.Model, makemigrations, migrate, testing model
* {{ forloop.counter }}
* Marionette web driver for selenium

### Session 6: 13.07.2016
* django.test.LiveServerTestCase: self.live_server_url
* REST-based design
* assertRegex (unittest)
* django.test.TestCase: response = self.client.get(url)
* django.test.TestCase: self.assertRedirects(response, url)
* django.test.TestCase: self.assertTemplateUsed(response, template)
* self.client.post(url, data)
* 302 - redirect
* 404 - not found
* 444 - connection closed without response
* html form: <fomr method="POST" action="url"></form>
* models.ForeignHey(ModelClassName, default)
* Model.objects.create
* capture grupes in urls e.g. "^/(\d+)/$" - argument in view
* selenium.webdriver.common.by.By
* selenium.webdriver.support.ui.WebDriverWait
* selenium.webdriver.support.expected_conditions
* expected_conditions.text_to_be_present_in_element


# Part II

### Session 7: 14.07.2016
* don't test layout, test some basics to check whether static files are loaded
* browser.set_window_size
* template inharitance: {% block name %}{% endblock %}, {% extends 'template.html' %}
* STATIC_URL for static files included in meta head
* STATIC_ROOT for collecting static
* django.contrib.staticfiles.testing.StaticLiveServerTestCase
* bootstrap jumbotron

### Session 8: 02.08.2016
* make notes and templates
* assure user account with home folder
* provision: see provisioning_notes.md in deploy_tools
* deploy: create directory sutructure, pull source code form git, activate venv, install reuiremnets, migrate, collectstatic, update settings (DEBUG, ALLOWED_HOSTS), restart gunicorn job, run functional tools
