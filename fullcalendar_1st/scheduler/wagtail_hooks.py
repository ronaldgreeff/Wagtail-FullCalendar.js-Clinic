from scheduler.models import Service, Enquiry, Appointment, Event
from users.models import Enquirer, User

from scheduler.forms import EnquirerForm, AppointmentForm
from django.forms import formset_factory

from django.db import models
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from wagtail.contrib.modeladmin.views import IndexView


# TODO this code probably doesn't belong in wagtail_hooks anymore - move after working


class AppointmentIndexView(IndexView):
    AppointmentFormSet = formset_factory(AppointmentForm, extra=1)
    appointment_formset = AppointmentFormSet(initial=Enquiry.objects.values())

class AppointmentAdmin(ModelAdmin):
    model = Appointment
    list_display = ('service', 'doctor', 'start', 'end')
    list_per_page = 10
    index_view_class = AppointmentIndexView

modeladmin_register(AppointmentAdmin)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# formset factory
# https://docs.djangoproject.com/en/2.2/topics/forms/formsets/
# wagtail admin view
# https://docs.wagtail.io/en/v2.7.1/reference/contrib/modeladmin/index.html
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~