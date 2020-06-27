from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import PatientSerializer, EventSerializer, AppointmentSerializer
from scheduler.models import Event, Appointment, Service

from itertools import chain
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse, HttpResponse

from myusers.models import Patient
from django.template.loader import render_to_string
import json
# TODO: cleanup imports ^

class GetSchedule(APIView):
    """
    Get a list of events and appointments

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated] #[permissions.IsAdminUser]

    def collect_schedule(self):
        events = EventSerializer(Event.objects.all(), many=True)
        appointments = AppointmentSerializer(Appointment.objects.all(), many=True)
        return list(chain(events.data, appointments.data))

    def get(self, request, format=None):
        schedule = self.collect_schedule()
        return Response(schedule)


def event_service_duration(request):

    if request.is_ajax and request.method == 'GET':

        service_id = request.GET.get('service_id', None)
        service = Service.objects.get(id=service_id)
        data = {'duration': service.duration}
        return JsonResponse(data)


def patient_lookup(request):

    if request.is_ajax and request.method == 'GET':

        query_basis = request.GET.get('query_basis')
        query_value = request.GET.get('query_value')

        p = Patient.objects
        
        if query_value:

            if query_basis == 'first_name':
                patients = p.filter(first_name__icontains=query_value)
            elif query_basis == 'last_name':
                patients = p.filter(last_name__icontains=query_value)
            elif query_basis == 'email':
                patients = p.filter(email_address__icontains=query_value)
            elif query_basis == 'phone':
                patients = p.filter(phone_number__icontains=query_value)

        else:
            patients = p.all()

        l = []
        for patient in patients:
            pd = PatientSerializer(patient).data;
            l.append({
                'pd': pd,
                'pds': json.dumps(pd)
                })

        html = render_to_string(
            template_name = 'scheduler/patient_list_partial.html',
            context = {'patients': l},
            )

        return JsonResponse(html, safe=False)


def admin_schedule(request):
    """ Render the html which contains FullCalendar JS code.
    FullCalendar calls EventsViewSet """

    ser = {'event': EventSerializer, 'appointment': AppointmentSerializer}

    if request.method == 'POST':

        form_type = request.POST.get('form_type')
        ser_form = ser[form_type](data=request.POST)

        print('\nform_type: {}\ndata: {}\n'.format(form_type, request.POST))
        print('ser_form: {}\n'.format(ser_form))

        # response_data = {'test': 'test'}

        # # return JsonResponse(response_data)

        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type='application/json'
        #     )

        if ser_form.is_valid():
            # TODO: Create
            return JsonResponse({'created': ser_form.data})
            # return HttpResponse(
            #     json.dumps(ser_form.data),
            #     content_type='application/json'
            #     )
        else:
            return JsonResponse({'errors': ser_form.errors})
            # return HttpResponse(
            #     json.dumps(ser_form.errors),
            #     content_type='application/json'
            #     )

        # return JsonResponse(response_data)

    return render(request, 'scheduler/admin_schedule.html')