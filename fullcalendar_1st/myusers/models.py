from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_owner = models.BooleanField(default=False) # is_staff + full authorization
    is_doctor = models.BooleanField(default=False) # is_staff + some authorization
    is_administrator = models.BooleanField(default=False) # is_staff + some authorization
    # is_patient = models.BooleanField(default=False) # no authorization
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE', primary_key=True)
    services = models.ManyToManyField('scheduler.Service')


class Patient(models.Model):
    # user =  models.OneToOneField(User, on_delete='CASCADE', primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email_address = models.EmailField(max_length=100, null=False, blank=False)
    is_confirmed = models.BooleanField(default=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    # documents = wagtail.docs # ! review security considerations ! #


@receiver(post_save, sender=User)
def create_user_type(sender, instance, created, **kwargs):
    if created:
        if instance.is_doctor:
            Doctor.objects.create(user=instance,)
            #TODO: add in services (also in edit)

        # # if not elif: a doctor **could** become a patient
        # if instance.is_patient:
        #     Patient.objects.create(user=instance,)

@receiver(post_save, sender=User)
def edit_user_type(sender, instance, created, **kwargs):
    try:
        doctor = Doctor.objects.get(user=instance)
        if not instance.is_doctor:
            doctor.delete()
    except Doctor.DoesNotExist:
        if instance.is_doctor:
            Doctor.objects.create(user=instance)

    # try:
    #     patient = Patient.objects.get(user=instance)
    #     if not instance.is_doctor:
    #         patient.delete()
    # except Patient.DoesNotExist:
    #     if instance.is_doctor:
    #         Patient.objects.create(user=instance)