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

# # class AppointmentIndexView(IndexView):
# #     AppointmentFormSet = formset_factory(AppointmentForm, extra=1)
# #     appointment_formset = AppointmentFormSet(initial=Appointment.objects.values())
# #
# # TODO Appointment confirmation
# class AppointmentAdmin(ModelAdmin):
#     model = Appointment
#     list_display = ['service', 'start', 'end']
#     list_per_page = 10
#     # index_view_class = AppointmentIndexView

# # TODO Doctor should be registered using a form
# class DoctorAdmin(ModelAdmin):
#     model = Doctor
#     list_display = ['user']

# # Patient will be created via enquiry form - no need to
# # manage them via admin. Just here for convenience
# class PatientAdmin(ModelAdmin):
#     model = Patient
#     list_display = ['user', 'is_confirmed']

# # Here for convenience
# class ServiceAdmin(ModelAdmin):
#     model = Service

# # Here for convenience
# class EventAdmin(ModelAdmin):
#     model = Event

# modeladmin_register(ServiceAdmin)
# modeladmin_register(EventAdmin)
# modeladmin_register(AppointmentAdmin)
# modeladmin_register(DoctorAdmin)
# modeladmin_register(PatientAdmin)