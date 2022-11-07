# Python + PostgreSQL Task
## Task
### Create RESTful API:
1. /users POST - create user with the next fields: first_name (required, only letters),
last_name (only letters), email (required, unique, correct format), phone (correct format),
password (hash)
2. /login POST - create API for user login by email and password. Use JWT authentication
3. /users/:id GET - get 1 user by id.
4. /users/:id PUT - update user, add validation. Connect Socket.IO for sending push
notifications after user update.
   
## Setup
### install requirements
```bach
pip install -r requirements.txt
```
### connect PostgreSQL db
Update in IncoraTask > settings.py
```bach
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Incora',  # db name
        'USER': 'pavlo',  # user name
        'PASSWORD': '1234',  # password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
make migrations and migrate
```bach
python manage.py makemigrations
```
```bach
python manage.py migrate
```
## Run server
```bach
python manage.py runserver
```
## Take messages from Socket.IO
- Connect to server by host name
- Create listener with name "update"

