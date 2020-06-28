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
    """ """
    # TODO: add button to so that user can
    # update patient details then and there

    if request.method == 'POST':

        form_type = request.POST.get('form_type')
        print('\nform_type: {}\ndata: {}\n'.format(form_type, request.POST))

        if form_type == 'appointment':

            patient = request.POST.get('patient[first_name]')

            patient_id = request.POST.get('patient[patient_id]')
            first_name = request.POST.get('patient[first_name]')
            last_name = request.POST.get('patient[last_name]')
            email_address = request.POST.get('patient[email_address]')
            phone_number = request.POST.get('patient[phone_number]')

            if patient_id:
                patient = Patient.objects.get(id=patient_id)
                patient.is_confirmed = True
                patient.save()

            else:
                patient = Patient.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    email_address = email_address,
                    is_confirmed = True,
                    phone_number = phone_number,
                    )

            ser_form = AppointmentSerializer(
                data={
                    'start':request.POST.get('start'),
                    'end':request.POST.get('end'),
                    'doctor':request.POST.get('doctor'),
                    'service':request.POST.get('service'),
                    'patient':patient.id,
                })

        elif form_type == 'event':
            ser_form = EventSerializer(data=request.POST)

        print('ser_form: {}\n'.format(ser_form))

        if ser_form.is_valid():
            ser_form.save()
            data = {'created': ser_form.data}

        else:
            data = {'errors': ser_form.errors}

        return JsonResponse(data)

    if request.method == 'GET':
        return render(request, 'scheduler/admin_schedule.html')