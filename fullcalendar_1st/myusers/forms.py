from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from myusers.models import User


class CustomUserEditForm(UserEditForm):
    is_owner = forms.BooleanField(required=False)
    is_doctor = forms.BooleanField(required=False)
    is_administrator = forms.BooleanField(required=False)
    # is_patient = forms.BooleanField(required=False)
    phone_number = forms.CharField(required=False)

    def clean(self):
        if not any(self.is_owner, self.is_doctor, self.is_administrator, self.is_patient):
            raise ValidationError("User must have at least one role.")

class CustomUserCreationForm(UserCreationForm):
    is_owner = forms.BooleanField(required=False)
    is_doctor = forms.BooleanField(required=False)
    is_administrator = forms.BooleanField(required=False)
    # is_patient = forms.BooleanField(required=False)
    phone_number = forms.CharField(required=False)

    def clean(self):
        if not any(self.is_owner, self.is_doctor, self.is_administrator, self.is_patient):
            raise ValidationError("User must have at least one role.")


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