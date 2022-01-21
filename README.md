# django-tawkto

django-tawkto is a simple Django app to it integrates with https://www.tawk.to/ chat.

### Requirements

Python 3.7 to 3.10 supported.

Django 2.2 to 4.0 supported.

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

(Optional) Add visitor `name` and `email`:

```djangotemplate
{% tawkto_script user_name=request.user.get_full_name user_email=request.user.email %}
```

(Optional) Use a different widget for a given property (`default` is the default value):

```python
TAWKTO_WIDGET_ID = "default"
```

or

```djangotemplate
{% tawkto_script widget_id='somewidgetid' %}
```

(Optional) Use a different tawkto property:

```djangotemplate
{% tawkto_script id_site='tawktosideit' api_key='tawktoapikey'%}
```

(Optional) Set custom metadata regarding this chat/visitor:

- `is_secure` must be `True`.
- You must provide a valid email.
- Metadata is represented by key and value.
- The key is of the string data type and can contain only alphanumeric characters and ‘-‘ (dash).
- More in [https://developer.tawk.to/jsapi/](https://developer.tawk.to/jsapi/) `setAttributes` section.

```python
# view.py
def view(request):
    context = {'metadata': {'attr-1': 'value1', 'attr-2': 'value2'}}
    return render(request, 'template.html', context)
```

In template:

```djangotemplate
{% tawkto_script is_secure=True user_email=example@example.com extra_attributes=metadata %}
```

![metadata-image](https://i.imgur.com/SjLkl2Z.png)
