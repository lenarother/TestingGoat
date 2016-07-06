# Tutuorial on TDD with Django based on:

[Test-Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754/)

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
