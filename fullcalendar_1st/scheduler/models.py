# from django.db import models
# # Create your models here.

from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


# class Account():
# doctor, secretary, patient
# once an enquirer's appointment is confirmed, they become a patient
# a patient should be assigned to either a service, doctor or both - depending on the clinic


class Service(models.Model):
    name = models.CharField(default='appointment', max_length=50)
    duration = models.IntegerField(default=60,)

    def __str__(self):
        return '{0} ({1}mins)'.format(self.name, self.duration)

class Enquirer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return '{0} {1} ({2})'.format(self.first_name, self.last_name, self.email)

class CalendarEvent(models.Model):
    # account (patient, doctor, ...)
    enquirer = models.ForeignKey(Enquirer, on_delete='CASCADE', null=True)
    service = models.ForeignKey(Service, on_delete='CASCADE', null=True)
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'CalendarEvent'
        verbose_name_plural = 'CalendarEvents'

    def __str__(self):
        return self.title


# TODO
# Should be Enquiry (currently CalendarEvent), Appointment, Event


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
