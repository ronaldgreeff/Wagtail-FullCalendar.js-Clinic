# for direct usage
# from django import forms
# class DateForm(forms.Form):
#     date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

from django import forms
from .widgets import XDSoftDateTimePickerInput

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=XDSoftDateTimePickerInput()
    )