# from django.db import models
# # Create your models here.

from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class Service(models.Model):
    name = models.CharField(default='appointment', max_length=50)
    duration = models.IntegerField(default=60,)

    def __str__(self):
        return '{0} ({1}mins)'.format(self.name, self.duration)

class Enquirer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)


class CalendarEvent(models.Model):
    enquirer = models.ForeignKey(Enquirer, on_delete='CASCADE', null=True)
    service = models.ForeignKey(Service, on_delete='CASCADE', null=True)
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    # is timestamp useful?

    class Meta:
        verbose_name = 'CalendarEvent'
        verbose_name_plural = 'CalendarEvents'

    def __str__(self):
        return self.title


class PickDateTimePage(Page):
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
        from scheduler.forms import DatePickerForm

        if request.method == 'POST':
            form = DatePickerForm(request.POST)
            if form.is_valid():
                saved_form = form.save()
                return render(request, 'scheduler/pickdatetime.html', {
                    'page': self,
                    'saved_form': saved_form,
                })
        else:
            form = DatePickerForm()

        return render(request, 'scheduler/pickdatetime.html', {
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
    # def serve(self, request):

    #     return render(request, 'scheduler/doctor_schedule.html', {
    #                 'calendar_config_options': 0,
    #             })