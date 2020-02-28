from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from myusers.models import User


class CustomUserEditForm(UserEditForm):
    is_owner = forms.BooleanField(required=False)
    is_doctor = forms.BooleanField(required=False)
    is_administrator = forms.BooleanField(required=False)
    phone_number = forms.CharField(required=False)

    def clean(self):
        if not any(self.is_owner, self.is_doctor, self.is_administrator, self.is_patient):
            raise ValidationError("User must have at least one role.")

class CustomUserCreationForm(UserCreationForm):
    is_owner = forms.BooleanField(required=False)
    is_doctor = forms.BooleanField(required=False)
    is_administrator = forms.BooleanField(required=False)
    phone_number = forms.CharField(required=False)

    def clean(self):
        if not any(self.is_owner, self.is_doctor, self.is_administrator, self.is_patient):
            raise ValidationError("User must have at least one role.")