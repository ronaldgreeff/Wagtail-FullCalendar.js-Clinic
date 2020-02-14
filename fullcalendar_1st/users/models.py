from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# https://groups.google.com/forum/#!topic/wagtail/OCdYtdnW5IM

class Enquirer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return '{0} {1} ({2})'.format(self.first_name, self.last_name, self.email)


class User(AbstractUser):
    is_owner = models.BooleanField(default=False) # is_staff + full authorization
    is_administrator = models.BooleanField(default=False) # is_staff + semi authorization
    is_patient = models.BooleanField(default=False) # no authorization
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)