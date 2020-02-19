from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# https://groups.google.com/forum/#!topic/wagtail/OCdYtdnW5IM

class User(AbstractUser):
    is_owner = models.BooleanField(default=False) # is_staff + full authorization
    is_doctor = models.BooleanField(default=False) # is_staff + some authorization
    is_administrator = models.BooleanField(default=False) # is_staff + some authorization
    is_patient = models.BooleanField(default=False) # no authorization
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE', null=True)
    services = models.ManyToManyField(User)


class Patient(models.Model):
    user =  models.OneToOneField(User, on_delete='CASCADE', null=True)
    is_confirmed = models.BooleanField(default=False)
    documents = wagtail.docs # ! review security considerations ! #