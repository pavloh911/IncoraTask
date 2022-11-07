from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=20, validators=[
        RegexValidator(regex=r'^[A-Za-z]*$', message='The first name can contain only latin letters.')
    ])
    last_name = models.CharField(max_length=20, blank=True, validators=[
        RegexValidator(regex=r'^[A-Za-z]*$', message='The last name can contain only latin letters.')
    ])
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, validators=[
        RegexValidator(regex=r'^\+?(38)?\(?0[1-9]{2}\)?[0-9]{2}-?[0-9]{3}-?[0-9]{2}$',
                       message='Invalid phone number format.')
    ])
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return str(self.email)

    USERNAME_FIELD = 'email'
    last_login = ...
    objects = UserManager()



