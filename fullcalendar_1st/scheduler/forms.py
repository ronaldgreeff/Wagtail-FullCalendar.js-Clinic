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

    form_type = forms.CharField(
        initial='event',
        widget=forms.HiddenInput())

    start = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(
            attrs={'class': "schedule_start_field"}))
    end = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(
            attrs={'class': "schedule_end_field"}))

    class Meta:
        model = Event
        fields = ['form_type',
            'title', 'start', 'end', 'users']


class AppointmentForm(forms.ModelForm):

    form_type = forms.CharField(
        initial='appointment',
        widget=forms.HiddenInput())

    start = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(
            attrs={'class': "schedule_start_field"}))
    end = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(
            attrs={'class': "schedule_end_field"}))

    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=False)

    patient_id = forms.CharField(
        initial='',
        widget=forms.HiddenInput())

    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField()
    phone_number = forms.RegexField(
        regex = r'^\+?1?\d{9,15}$', 
        # message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        )

    class Meta:
        model = Appointment
        fields = ['form_type',
            'start', 'end',
            'service', 'doctor', 'patient_id',
            'first_name', 'last_name',
            'email_address', 'phone_number']