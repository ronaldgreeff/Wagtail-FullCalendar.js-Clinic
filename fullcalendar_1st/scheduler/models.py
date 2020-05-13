from __future__ import unicode_literals

from django.db import models
# from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from django.utils import timezone

# comment for first migration (circular depencies) - see Appointment below too
from myusers.models import Doctor, Patient


class Service(models.Model):
    name = models.CharField(default='Appointment', max_length=50)
    duration = models.IntegerField(default=60,)

    def __str__(self):
        return '{0} ({1}mins)'.format(self.name, self.duration)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Appointment(TimeStampedModel):
    service = models.ForeignKey(Service, on_delete='CASCADE', null=True)
    # comment for first migration -->
    doctor = models.OneToOneField(Doctor, on_delete='CASCADE', null=True, blank=True)
    patient = models.OneToOneField(Patient, on_delete='CASCADE', null=False)
    # <-- comment for first migration
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '{0} | {1} | {2} - {3}'.format(
            (self.doctor if self.doctor else 'Unconfirmed'),
            self.service,
            self.start.strftime('%d/%m@%H:%M'),
            self.end.strftime('%d/%m@%H:%M'))


class Event(TimeStampedModel):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    users = models.ManyToManyField('myusers.User')

    def __str__(self):
        return '{0} {1} - {2}'.format(
            self.title, self.start, self.end)



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