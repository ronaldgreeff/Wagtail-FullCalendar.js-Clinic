from django import forms
from scheduler.models import Service

class DateForm(forms.Form):

    service = forms.ModelChoiceField(queryset=Service.objects.all())
    datetime = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    first_name = forms.CharField()
    last_name = forms.CharField()
    email =  forms.EmailField()

    def save(self):

        data = self.cleaned_data