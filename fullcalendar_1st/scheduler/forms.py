from django import forms

from scheduler.models import Service, Event#, Appointment
from myusers.models import User#, Doctor, Patient

from datetime import timedelta
from .widgets import XDSoftDateTimePickerInput


# TODO for customer user models, need to implement custom forms
# i.e. to create associated user when creating doctors
# https://docs.wagtail.io/en/v2.7.1/advanced_topics/customisation/custom_user_models.html


# MODEL
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     country = models.CharField(verbose_name='country', max_length=255)
#     status = models.ForeignKey(MembershipStatus, on_delete=models.SET_NULL, null=True, default=1)


# FORM (create and edit)
# from django import forms
# from django.utils.translation import ugettext_lazy as _

# from wagtail.users.forms import UserEditForm, UserCreationForm

# from users.models import MembershipStatus

# class CustomUserEditForm(UserEditForm):
#     country = forms.CharField(required=True, label=_("Country"))
#     status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))


# class CustomUserCreationForm(UserCreationForm):
#     country = forms.CharField(required=True, label=_("Country"))
#     status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))


# TEMPLATES
# Template create.html:

# {% extends "wagtailusers/users/create.html" %}

# {% block extra_fields %}
#     {% include "wagtailadmin/shared/field_as_li.html" with field=form.country %}
#     {% include "wagtailadmin/shared/field_as_li.html" with field=form.status %}
# {% endblock extra_fields %}

# Template edit.html:

# {% extends "wagtailusers/users/edit.html" %}

# {% block extra_fields %}
#     {% include "wagtailadmin/shared/field_as_li.html" with field=form.country %}
#     {% include "wagtailadmin/shared/field_as_li.html" with field=form.status %}
# {% endblock extra_fields %}



# The extra_fields block allows fields to be inserted below the last_name field in the default templates. Other block overriding options exist to allow appending fields to the end or beginning of the existing fields, or to allow all the fields to be redefined.

# Add the wagtail settings to your project to reference the user form additions:

# WAGTAIL_USER_EDIT_FORM = 'users.forms.CustomUserEditForm'
# WAGTAIL_USER_CREATION_FORM = 'users.forms.CustomUserCreationForm'
# WAGTAIL_USER_CUSTOM_FIELDS = ['country', 'status']
#=================================================================================================
# FOR REFERENCE
# MODELS
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
#     interests = models.ManyToManyField(Subject, related_name='interested_students')

# VIEWS
# from django.contrib.auth import login
# from django.shortcuts import redirect
# from django.views.generic import CreateView

# from ..forms import StudentSignUpForm
# from ..models import User

# class StudentSignUpView(CreateView):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'registration/signup_form.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('students:quiz_list')

# FORMS
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction

# from classroom.models import Student, Subject, User

# class StudentSignUpForm(UserCreationForm):
#     interests = forms.ModelMultipleChoiceField(
#         queryset=Subject.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         student = Student.objects.create(user=user)
#         student.interests.add(*self.cleaned_data.get('interests'))
#         return user








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


class BaseEventForm(forms.Form):
    title = forms.CharField()
    start = forms.DateField()
    end = forms.DateField()
    recurring = forms.BooleanField()
    recurrance= forms.IntegerField()


class AppointmentForm(BaseEventForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all())
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(is_doctor=True))
    patient = forms.ModelChoiceField(queryset=User.objects.filter(is_patient=True))


class EventForm(BaseEventForm):
    users = forms.MultipleChoiceField(choices=[])