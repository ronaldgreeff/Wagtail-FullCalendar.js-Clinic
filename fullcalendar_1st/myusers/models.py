from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

from scheduler.models import Appointment, Event


class User(AbstractUser):
    is_owner = models.BooleanField(default=False) # is_staff + full authorization
    is_doctor = models.BooleanField(default=False) # is_staff + some authorization
    is_administrator = models.BooleanField(default=False) # is_staff + some authorization
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE', primary_key=True)

    appointments = models.ForeignKey(Appointment, on_delete='CASCADE', null=True, blank=True)
    events = models.ForeignKey(Event, on_delete='CASCADE', null=True, blank=True)
    # services = models.ManyToManyField('scheduler.Service')

    def __str__(self):
        return '{0}'.format(self.user.username)


class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email_address = models.EmailField(max_length=100, null=False, blank=False)
    is_confirmed = models.BooleanField(default=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    appointments = models.ForeignKey(Appointment, on_delete='CASCADE', null=True, blank=True)

    # documents = wagtail.docs # ! review security considerations ! #

    def __str__(self):
        return '{0}, {1} {2}'.format(
            self.last_name, 
            self.first_name,
            ('(unconfirmed)' if not self.is_confirmed else ''))


# create doctor instance automatically
@receiver(post_save, sender=User)
def create_user_type(sender, instance, created, **kwargs):
    if created:
        if instance.is_doctor:
            Doctor.objects.create(user=instance,)
            #TODO: add in services (and same in edit)

@receiver(post_save, sender=User)
def edit_user_type(sender, instance, created, **kwargs):
    try:
        doctor = Doctor.objects.get(user=instance)
        if not instance.is_doctor:
            doctor.delete()
    except Doctor.DoesNotExist:
        if instance.is_doctor:
            Doctor.objects.create(user=instance)