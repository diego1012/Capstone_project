# Littlelemon

## Installation

using pipenv (easier than pip and contains all dependencies)

you might need yo change python version in Pipfile python_version = "your-installed-python-version"

```Shell
# CMD / PowerShell
pipenv shell
pipenv install
```

## Setup

Modify database config in project/settings.py file

```Shell
# CMD / PowerShell
'NAME': 'database',
'USER': 'user',
'PASSWORD': 'password',
```

## Initialization

Run migrations

```Shell
# CMD / PowerShell
python manage.py migrate
```

Create super user

```Shell
# CMD / PowerShell
python manage.py createsuperuser
```

## Routes

booking

```
/restaurant/booking/tables/
```

menu-item

```
/api/menu-items/
```

auth (Djoser)

```
/auth/token/login/
```

auth (DRF)

```
/api/api-token-auth
```

## Testing

```Shell
# CMD / PowerShell
python manage.py test
```
