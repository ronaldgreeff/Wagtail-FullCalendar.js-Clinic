# from django.db import models
# # Create your models here.

from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class IceCreamFlavour(models.Model):
    flavour_name = models.CharField(max_length=255)
    your_name = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)


class FlavourSuggestionPage(Page):
    intro = RichTextField(blank=True)
    thankyou_page_title = models.CharField(
        max_length=255, help_text="Title text to use for the 'thank you' page")

    # Note that there's nothing here for specifying the actual form fields -
    # those are still defined in forms.py. There's no benefit to making these
    # editable within the Wagtail admin, since you'd need to make changes to
    # the code to make them work anyway.

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('thankyou_page_title'),
    ]

    def serve(self, request):
        from scheduler.forms import FlavourSuggestionForm

        if request.method == 'POST':
            form = FlavourSuggestionForm(request.POST)
            if form.is_valid():
                flavour = form.save()
                return render(request, 'scheduler/pickdatetime.html', {
                    'page': self,
                    'flavour': flavour,
                })
        else:
            form = FlavourSuggestionForm()

        return render(request, 'scheduler/pickdatetime.html', {
            'page': self,
            'form': form,
        })