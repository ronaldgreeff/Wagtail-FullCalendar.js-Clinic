from scheduler.models import Service, Event, Appointment
from myusers.models import User, Doctor, Patient

from scheduler.forms import EnquirerForm, AppointmentForm
from django.forms import formset_factory

from django.db import models
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from wagtail.contrib.modeladmin.views import IndexView

class UserIndexView(ModelAdmin):
    model = User
    list_display = ['username', 'is_doctor']



modeladmin_register(UserIndexView)