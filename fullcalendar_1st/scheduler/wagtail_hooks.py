from scheduler.models import Service, Event#, Appointment
from users.models import User#, Doctor, Patient

from scheduler.forms import EnquirerForm, AppointmentForm
from django.forms import formset_factory

from django.db import models
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from wagtail.contrib.modeladmin.views import IndexView


class ServiceAdmin(ModelAdmin):
    model = Service

class EventAdmin(ModelAdmin):
    model = Event


# class AppointmentIndexView(IndexView):
#     AppointmentFormSet = formset_factory(AppointmentForm, extra=1)
#     appointment_formset = AppointmentFormSet(initial=Appointment.objects.values())

# class AppointmentAdmin(ModelAdmin):
#     model = Appointment
#     list_display = ['service', 'start', 'end']
#     list_per_page = 10
#     index_view_class = AppointmentIndexView

# class DoctorAdmin(ModelAdmin):
#     model = Doctor

# class PatientAdmin(ModelAdmin):
#     model = Patient


# modeladmin_register(AppointmentAdmin)
# modeladmin_register(EventAdmin)
# modeladmin_register(ServiceAdmin)
# modeladmin_register(DoctorAdmin)
# modeladmin_register(PatientAdmin)