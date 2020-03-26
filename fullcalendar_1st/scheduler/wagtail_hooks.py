from scheduler.models import Service, Event, Appointment
from myusers.models import User, Doctor, Patient

from django.db import models
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from wagtail.contrib.modeladmin.views import IndexView

class UserIndexView(ModelAdmin):
    model = User
    list_display = ['username', 'is_doctor']

class PatientIndexView(ModelAdmin):
    model = Patient
    list_filter = ['is_confirmed']

class ServiceIndexView(ModelAdmin):
    model = Service

class UnconfirmedAppointmentIndexView(ModelAdmin):
    model = Appointment
    menu_label = 'Unconfirmed'
    list_filter = ['service', 'doctor']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(doctor__isnull=True)


modeladmin_register(UserIndexView)
modeladmin_register(PatientIndexView)
modeladmin_register(ServiceIndexView)
modeladmin_register(UnconfirmedAppointmentIndexView)