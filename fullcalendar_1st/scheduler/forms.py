from django import forms
from django.forms import formset_factory

from scheduler.models import Service, Enquiry, Appointment, Event
from users.models import Enquirer, User

from datetime import timedelta
from .widgets import XDSoftDateTimePickerInput



class EnquirerForm(forms.Form):
    service = forms.ModelChoiceField(queryset=Service.objects.all())
    datetime = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email =  forms.EmailField()

    def save(self, commit=True):

        data = self.cleaned_data

        enquirer = Enquirer.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'])

        requested_service_name = getattr(
            data['service'], 'name')
        requested_service_duration = getattr(
            data['service'], 'duration')

        requested_service = Service.objects.get(
            name=requested_service_name)

        new_event = CalendarEvent.objects.create(
            enquirer = enquirer,
            service = requested_service,
            title = requested_service_name,
            start = data['datetime'],
            end = data['datetime'] + timedelta(
                minutes=requested_service_duration))

        new_event.save()


class AppointmentForm(forms.Form):
    title = forms.CharField()
    start = forms.DateField()
    end = forms.DateField()
    recurring = forms.BooleanField()
    recurrance= forms.IntegerField()
    service = forms.ModelChoiceField(queryset=Service.objects.all())
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(is_doctor=True))
    patient = forms.ModelChoiceField(queryset=User.objects.filter(is_patient=True))

# TODO move formset factory
# https://docs.djangoproject.com/en/2.2/topics/forms/formsets/
# TO wagtail admin view
# https://docs.wagtail.io/en/v2.7.1/reference/contrib/modeladmin/primer.html#changing-what-appears-in-the-listing
# https://docs.wagtail.io/en/v2.7.1/reference/contrib/modeladmin/index.html

AppointmentFormSet = formset_factory(AppointmentForm, extra=1)
appointment_formset = AppointmentFormSet(initial=Enquiry.objects.values())


class EventForm(forms.Form):
    title = forms.CharField()
    start = forms.DateField()
    end = forms.DateField()
    event_type = forms.ChoiceField()
    recurring = forms.BooleanField()
    recurrance= forms.IntegerField()