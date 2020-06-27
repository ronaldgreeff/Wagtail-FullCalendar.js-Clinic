from django import template
from scheduler.forms import EnquirerForm, EventForm, AppointmentForm

register = template.Library()

@register.inclusion_tag('scheduler/enquiry_form.html', takes_context=True)
def load_enquiry_form(context):
    request = context['request']

    if request.method == 'POST':
        form = EnquirerForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return { 'saved_form': saved_form }

    else:
        form = EnquirerForm()

    return {
    	'form': form,
    }


@register.inclusion_tag('scheduler/schedule_modal.html', takes_context=True)
def load_schedule_modal(context):
    return {
        'forms': {
            'event': EventForm(),
            'appointment': AppointmentForm() },
    }