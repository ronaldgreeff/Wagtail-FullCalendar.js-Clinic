from django import template
from scheduler.forms import EnquirerForm, EventForm, AppointmentForm
# from scheduler.serializers import EventSerializer, AppointmentSerializer
# from rest_framework.response import Response
# from django.http import JsonResponse #HttpResponse
# import json
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

    # request = context['request']
    # ser = {'event': EventSerializer, 'appointment': AppointmentSerializer}

    # if request.method == 'POST':
    #     form_type = request.POST.get('form_type')
    #     ser_form = ser[form_type](data=request.POST)
    #     print('\nform_type: {}\ndata: {}\n'.format(form_type, request.POST))
    #     print('ser_form: {}\n'.format(ser_form))

    #     response_data = {'test': 'test'}

    #     return JsonResponse(response_data)

    #     # return HttpResponse(
    #     #     json.dumps(response_data),
    #     #     content_type='application/json'
    #     #     )

    #     # if ser_form.is_valid():
    #     #     print('*valid:\n', ser_form.data)
    #     #     return HttpResponse(
    #     #         json.dumps(ser_form.data),
    #     #         content_type='application/json'
    #     #         )
    #     # else:
    #     #     print('*invalid:\n', json.dumps(ser_form.errors))
    #     #     return HttpResponse(
    #     #         json.dumps(ser_form.errors),
    #     #         content_type='application/json'
    #     #         )

    # else:

    # if request.method == 'GET':
    #     # form = get_form[form_type](request.POST)
    #     forms = {'event': EventForm(),
    #     'appointment': AppointmentForm()}

    return {
        'forms': {'event': EventForm(),
            'appointment': AppointmentForm()},
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