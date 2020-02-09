from django import forms
from scheduler.models import Service, Enquirer, CalendarEvent
from datetime import timedelta

class DatePickerForm(forms.Form): #DatePickerForm

    service = forms.ModelChoiceField(queryset=Service.objects.all())
    datetime = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    first_name = forms.CharField()
    last_name = forms.CharField()
    email =  forms.EmailField()

    # def __init__():
    # TODO block out existing events on the front-end

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

# # DatePickerForm as a widget instead
# from .widgets import XDSoftDateTimePickerInput
# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'], 
#         widget=XDSoftDateTimePickerInput()
#     )