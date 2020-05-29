from django import template
from scheduler.forms import EnquirerForm, EventForm, AppointmentForm
# from django.shortcuts import render

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
    else:
        form = EnquirerForm()

    return {
    	'form': form,
    }

@register.inclusion_tag('scheduler/event_form.html', takes_context=True)
def load_event_form(context):
    request = context['request']

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return {
                'saved_form': saved_form,
            }
    else:
        form = EventForm()

    return {
        'form': form,
    }

@register.inclusion_tag('scheduler/appointment_form.html', takes_context=True)
def load_appointment_form(context):
    request = context['request']

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return {
                'saved_form': saved_form,
            }
    else:
        form = AppointmentForm()

    return {
        'form': form,
    }