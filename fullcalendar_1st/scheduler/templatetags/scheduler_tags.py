from django import template
from scheduler.forms import EnquirerForm, EventForm, AppointmentForm
from scheduler.serializers import EventSerializer, AppointmentSerializer
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
    """ Loads modal containing forms (Event and Appointment) to allow the user to easily
    switch between the two. form_type passed in via data-* attribute """

    ## old form save method
    # request = context['request']
    # get_form = {'event': EventForm, 'appointment': AppointmentForm}

    # if request.method == 'POST':
    #     form_type = request.POST.get('form_type')
    #     form = get_form[form_type](request.POST)

    #     if form.is_valid():
    #         forms = form.save()

    #         return {
    #             'saved_form': saved_form,
    #         }

    # print(request.POST)
    # <QueryDict: {'csrfmiddlewaretoken': ['DMe2zSZNjRZNTkkSycuXYWFGgPDMWEPoeIo5vlXYNa7LWURkUT62OW1RYBYvm2JM'],
    # 'start': ['08-05-2020 00:00'], 'end': ['08-05-2020 01:00'], 'service': ['1'], 'doctor': [''], 'first_name': ['asd'], 'last_name': ['asd'],
    # 'email_address': ['sdfsd@sadfa.com'], 'phone_number': ['asdas@asd.com'], 'form_type': ['appointment']}>

    request = context['request']
    ser = {'event': EventSerializer, 'appointment': AppointmentSerializer}

    if request.method == 'POST':

        form_type = request.POST.pop('form_type')
        # todo - put data in a dict
        ser_form = ser[form_type](data=request.POST)

        if ser_form.is_valid():
            return Response(ser_form.data)
        else:
            return Response(ser_form.errors)

    else:
        # form = get_form[form_type](request.POST)
        forms = {'event': EventForm(),
        'appointment': AppointmentForm()}

    return {
        'forms': forms,
    }

    ## from views / serializer
    # def post(self, request, format=None):
    #     """
    #     POST should just check if the start date is valid
    #     and return the "end time" based on service selected
    #     """
    #     # AppointmentValidSerializer, EventValidSerializer
    #     form_type = request.data.pop('form_type')
    #     if form_type == 'appointment':
    #         serializer = AppointmentSerializer(request.data)
    #     elif form_type == 'event':
    #         serializer = EventSerializer(request.data)

    #     print(request.data)
    #     if serializer.is_valid():
    #         print('post serializer valid\n{}\n'.format(request.data))
    #         return Response(serializer.data)
 
    #     print('post serializer invalid\n{}\n---\n{}'.format(request.data, serializer.errors))

    #     return Response(serializer.errors)