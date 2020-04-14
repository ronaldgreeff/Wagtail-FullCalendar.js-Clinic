# in wagtail, defined in models
# from django import template
# from scheduler.forms import EnquirerForm

# register = template.Library()

# @register.inclusion_tag('enquiry_form.html', takes_context=True)
# def load_enquiry_form(context):
#     request = context['request']

#     if request.method == 'POST':
#         form = EnquirerForm(request.POST)
#         if form.is_valid():
#             saved_form = form.save()
#             return render(request, 'scheduler/appointment_confirmation.html', {
#                 'page': self,
#                 'saved_form': saved_form,
#             })
#     else:
#         form = EnquirerForm()

#     return render(request, 'scheduler/enquire_page.html', {
#         'page': self,
#         'form': form,
#     })

from django import template
from scheduler.forms import EnquirerForm
from django.shortcuts import render

register = template.Library()

@register.inclusion_tag('scheduler/enquiry_form.html', takes_context=True)
def load_enquiry_form(context):
    request = context['request']

    if request.method == 'POST':
        form = EnquirerForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return {
            	'saved_form': saved_form,
            }
            # return render(request, 'scheduler/appointment_confirmation.html', {
            #     'page': self,
            #     'saved_form': saved_form,
            # })
    else:
        form = EnquirerForm()

    return {
    	'form': form,
    }

    # return render(request, 'scheduler/enquire_page.html', {
    #     'page': self,
    #     'form': form,
    # })