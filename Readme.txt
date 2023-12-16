[Installation]
  # using pipenv (easier than pip and contains all dependencies)
  # you might need yo change python version in Pipfile python_version = "your-installed-python-version"
  CMD> pipenv shell
  CMD> pipenv install

[Database]
  # Modify database config in project/settings.py file
    'NAME': 'database',
    'USER': 'user',
    'PASSWORD': 'password',

[Initialization]
  CMD> python manage.py migrate
  CMD> python manage.py createsuperuser

[Routes]
  # booking
  URL> /restaurant/booking/tables/

  # menu-item
  URL> /api/menu-items/

  # auth (Djoser)
  URL> /auth/token/login/

  # auth (DRF)
  URL> /api/api-token-auth

[Testing]
  CMD> python manage.py test
