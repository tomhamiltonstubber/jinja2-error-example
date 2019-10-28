# Example of Jinja Error with Django Debug

This error seems to happen if there's an error in the template and when the user is authenticated.

The error was caused between versions 2.10.1 and 2.10.2.

## How to replicate

- Download repo
- `pip install -r requirements.txt`
- `python manage.py migrate`
- Create a user in shell:
```
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
```
- Login with your username and password fro above.
- There will be a message `A server error occurred.  Please contact the administrator.` shown in the browser.
- The stacktrace in the console will be long, with most of the errors being:

```
  File "/home/tom/repos/jinja-error-replication/env/lib/python3.7/site-packages/django/views/debug.py", line 383, in _get_lines_from_file
    context_line = source[lineno]
IndexError: list index out of range
```

The code causing the error is in the `index.jinja` template:

```jinja2
  {% for x, y in foo %}
    {{ x }}
  {% endfor %}
```

where `foo = 'bar'`

Hope this helps.
