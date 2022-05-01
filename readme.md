# ECommerce Project

<strong>Getting Started</strong><br>
Simple eCommerce app. The project has backend <strong>(Django + Django Rest Framework</strong>, <strong>MySQL</strong> database, frontend <strong>(Next JS)</strong> & android app <strong>(Flutter)</strong>.

## Backend (Django + Django Rest Framework)
- Configure virtual environment 
- Install Django
> pip install Django
- Install Django Rest Framework
> pip install djangorestframework

## Database (MySQL)
- Create a mysql database
> pip install mysqlclient

- Install "<em>mysqlclient</em>" package using pip & configure into settings.py file 
```py
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database-name>',
        'USER': 'root', 
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Create superuser
> python manage.py createsuperuser
- Make migrations 
> python manage.py makemigrations
> python manage.py migrate


## Frontend (Next JS)

## Android app (Flutter)
