=====
django-tawkto
=====

django-tawkto is a simple Django app to it integrates with https://www.tawk.to/ chat.


Quick start
-----------

1. Add "tawkto" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'tawkto',
    ]

2. Add `TAWKTO_ID_SITE` in settings.py::

    TAWKTO_ID_SITE='<tawkto id site>'

3. (Optional) Add `TAWKTO_API_KEY`::

    TAWKTO_API_KEY='<tawkto api key>'

4. (Optional) For secure site (requires `TAWKTO_API_KEY`)::

    TAWKTO_IS_SECURE=True

5. In HTML::

    {% load tawkto_tags %}

    <!DOCTYPE html>
    <html lang="en">
    <head>
    ...
    </head>
    <body>
        {% block content %}

        {% endblock %}

        {% tawkto_script %}
    </body>
    </html>

6. Add visitor `name` and `email`::

    {% tawkto_script user_name=request.user.get_full_name user_email=request.user.email %}
