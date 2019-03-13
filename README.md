# django-tawkto

django-tawkto is a simple Django app to it integrates with https://www.tawk.to/ chat.

### Quick start

Install the stable release from pypi (using pip):
```bash
pip install django-tawkto
```

Add `tawkto` to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    ...
    'tawkto',
]
```

Add `TAWKTO_ID_SITE` in settings.py:

```python
TAWKTO_ID_SITE='<tawkto id site>'
```

(Optional) Add `TAWKTO_API_KEY`:

```python
TAWKTO_API_KEY='<tawkto api key>'
```

(Optional) For secure site (requires `TAWKTO_API_KEY`):

```python
TAWKTO_IS_SECURE=True
```

In HTML:

```djangotemplate
{% load tawkto_tags %}

<!DOCTYPE html>
<html lang="en">
<head>
    ...
</head>
<body>
    ...
    {% tawkto_script %}
</body>
</html>
```

6. Add visitor `name` and `email`:

```djangotemplate
{% tawkto_script user_name=request.user.get_full_name user_email=request.user.email %}
```    

7. Use a different widget for a given property:

```djangotemplate
{% tawkto_script widget_id='somewidgetid' %}
```

