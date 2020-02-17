from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from users.models import Enquirer
from django.utils import timezone

from users.models import User


class Service(models.Model):
    name = models.CharField(default='appointment', max_length=50)
    duration = models.IntegerField(default=60,)

    # for modeladmin - see .wagtail_hooks
    panels = [
        FieldPanel('name'),
        FieldPanel('duration'),
    ]

    def __str__(self):
        return '{0} ({1}mins)'.format(self.name, self.duration)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Enquiry(TimeStampedModel):
    enquirer = models.OneToOneField(Enquirer, on_delete='CASCADE', null=True)
    service = models.ForeignKey(Service, on_delete='CASCADE', null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return '{0} {1} - {2}'.format(self.service, self.start, self.end)

# an enquiry turns to an appointment once confirmed by an administrator

class Appointment(TimeStampedModel):
    service = models.ForeignKey(Service, on_delete='CASCADE', null=True)
    # doctor = models.OneToOneField(Doctor, on_delete='CASCADE', null=False)
    doctor = models.OneToOneField(User, on_delete='CASCADE', null=False)
    # patient = models.OneToOneField(Patient, on_delete='CASCADE', null=False)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '({0}) {1} {2} - {3}'.format(self.doctor, self.service, self.start, self.end)


class Event(TimeStampedModel):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    users = models.ManyToManyField(User)

    def __str__(self):
        return '{0} {1} - {2}'.format(self.title, self.start, self.end)



class EnquirePage(Page):
    intro = RichTextField(blank=True)
    guidance = RichTextField(blank=True)
    thankyou_page_title = models.CharField(
        max_length=255, help_text="Title text to use for the 'thank you' page")

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="intro_text"),
        FieldPanel('guidance', classname="guidance_text"),
        FieldPanel('thankyou_page_title'),
    ]

    def serve(self, request):
        from scheduler.forms import EnquirerForm

        if request.method == 'POST':
            form = EnquirerForm(request.POST)
            if form.is_valid():
                saved_form = form.save()
                return render(request, 'scheduler/appointment_confirmation.html', {
                    'page': self,
                    'saved_form': saved_form,
                })
        else:
            form = EnquirerForm()

        return render(request, 'scheduler/enquire_page.html', {
            'page': self,
            'form': form,
        })


class SecretarySchedulePage(Page):

    def serve(self, request):

        return render(request, 'scheduler/secretary_schedule.html', {
                    'calendar_config_options': 0,
                })


class DoctorSchedulePage(Page):
    pass
