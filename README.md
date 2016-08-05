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

### Chapter 10
* functional tests as separate application
* 1 functional test = 1 user story
* base test with helpers (it is a good rule of a thumb to refactor a helper function when code is duplicated for the third time)
* SQLlite - model dosn't do full validation on save (e.g. doesn't validate blank=False), to enforce validation call model_object.full_clean() --> ValidationError
* urls in templates: {% url url_name arg %}
* useful to implement in model: get_absolute_url (return reverse(url_name, args))

### Chapter 11
* forms
  * process and validate user input
  * can be used in template for input and errors
  * save things into database
* models, views, forms - separate test files for each 
* customising form save method
* django.forms, inside fields definition e.g. fild_name = forms.CharField()
* django.forms.models.ModelForm (inside class Meta which can define model, fields, widgets, error_messages itp) 
* form.errors, form.field.erorrs
* form.is_valid()
* form(data=request.POST)
* customized save method: do thing and return super().save()

### Chapter 12
* class Meta in models: unique_together, ordering
* super
* overwriting form constructor to let the form know another view
* method validate_unique in form and model
* how to test views

### Chapter 13
* js testing fremwork e.g. qunit

### Session 14: 05.08.2016
* http://testing-goat-staging.mrother.com
* http://testing-goat.mrother.com
