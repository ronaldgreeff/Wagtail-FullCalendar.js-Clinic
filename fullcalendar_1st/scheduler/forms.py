from django import forms

from scheduler.models import Service, Appointment, Event
from myusers.models import User, Doctor, Patient

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
    phone_number = forms.RegexField(
        regex = r'^\+?1?\d{9,15}$', 
        # message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        )

    def save(self, commit=True):

        data = self.cleaned_data

        patient = Patient.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email_address=data['email'],
            phone_number=data['phone_number'], )

        requested_service_name = getattr(
            data['service'], 'name')
        requested_service_duration = getattr(
            data['service'], 'duration')

        requested_service = Service.objects.get(
            name=requested_service_name)

        unconfirmed_appointment = Appointment.objects.create(
            service = requested_service,
            # doctor assigned upon confirmation
            patient = patient,
            start = data['datetime'],
            end = data['datetime'] + timedelta(
                minutes=requested_service_duration) )

        unconfirmed_appointment.save()

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

# class BaseEventForm(forms.Form):
#     title = forms.CharField()
#     start = forms.DateField()
#     end = forms.DateField()
#     recurring = forms.BooleanField()
#     recurrance= forms.IntegerField()


# class AppointmentForm(BaseEventForm):
#     service = forms.ModelChoiceField(queryset=Service.objects.all())
#     doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
#     patient = forms.ModelChoiceField(queryset=Patient.objects.all())


# class EventForm(BaseEventForm):
#     users = forms.MultipleChoiceField(choices=[])