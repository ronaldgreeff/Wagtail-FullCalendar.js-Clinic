from myusers.models import User, Doctor, Patient

# from django.db import models
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
# from wagtail.contrib.modeladmin.views import IndexView

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from django.urls import re_path, include
from django.urls import reverse

class UserIndexView(ModelAdmin):
    model = User
    list_display = ['username', 'is_doctor']

class PatientIndexView(ModelAdmin):
    model = Patient
    list_filter = ['is_confirmed']

modeladmin_register(UserIndexView)
modeladmin_register(PatientIndexView)