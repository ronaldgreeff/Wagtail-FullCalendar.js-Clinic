# for django direct usage
# from django import forms
# class DateForm(forms.Form):
#     date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

# for django widget
from django import forms
from .widgets import XDSoftDateTimePickerInput

class FlavourSuggestionForm(forms.Form): # DateForm
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        # widget=XDSoftDateTimePickerInput()
    )

# from django import forms
# from scheduler.models import IceCreamFlavour
# class FlavourSuggestionForm(forms.ModelForm):
#     """
#     A form for suggesting an ice cream flavour. Here we're using a Django ModelForm, but this could
#     be as simple or as complex as you like -
#     see https://docs.djangoproject.com/en/1.9/topics/forms/
#     """
#     class Meta:
#         model = IceCreamFlavour
#         fields = ['flavour_name', 'your_name', 'datetime']