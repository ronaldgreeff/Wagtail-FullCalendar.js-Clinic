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


@register.inclusion_tag('scheduler/schedule_modal.html', takes_context=True)
def load_schedule_modal(context):
    """ Loads two forms (Event and Appointment) to allow the user to easily
    switch between the two. form_type passed in via data-* attribute """

    get_form = {'event': EventForm,
        'appointment': AppointmentForm}

    request = context['request']

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form = get_form[form_type](request.POST)

        if form.is_valid():
            saved_form = form.save()

            return {
                'saved_form': saved_form,
            }
    else:
        # form = get_form[form_type](request.POST)
        forms = {'event': EventForm(),
        'appointment': AppointmentForm()}

    return {
        'forms': forms,
    }