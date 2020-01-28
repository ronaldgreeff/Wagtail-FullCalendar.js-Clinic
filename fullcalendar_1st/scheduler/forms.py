from django import forms

class DateForm(forms.modelForm):

    datetime = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    def save(self):

        data = self.cleaned_data