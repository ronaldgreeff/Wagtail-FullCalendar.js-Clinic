from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import EventSerializer, AppointmentSerializer, AppointmentValidSerializer, EventValidSerializer
from scheduler.models import Event, Appointment

from itertools import chain
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
# TODO: cleanup imports ^


# class InsertEventView(APIView):
#     pass

# TODO - better name for EventsViewSet
class GetCreateSchedule(APIView):
    """
    Get a list of events and appointments

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated] #[permissions.IsAdminUser]

    def CollectSchedule(self):
        events = EventSerializer(Event.objects.all(), many=True)
        appointments = AppointmentSerializer(Appointment.objects.all(), many=True)
        return list(chain(events.data, appointments.data))

    def get(self, request, format=None):
        schedule = self.CollectSchedule()
        return Response(schedule)

    def post(self, request, format=None):
        """
        POST should just check if the start date is valid
        and return the "end time" based on service selected
        """
        # AppointmentValidSerializer, EventValidSerializer
        form_type = request.data.pop('form_type')
        if form_type == 'appointment':
            serializer = AppointmentSerializer(request.data)
        elif form_type == 'event':
            serializer = EventSerializer(request.data)

        print(request.data)
        if serializer.is_valid():
            print('post serializer valid\n{}\n'.format(request.data))
            return Response(serializer.data)
 
        print('post serializer invalid\n{}\n---\n{}'.format(request.data, serializer.errors))

        return Response(serializer.errors)


def event_service_duration(request):
    service_id = request.GET.get('service_id', None)
    service = Service.objects.get(id=service_id)
    data = {'duration': service.duration}
    return JsonResponse(data)


def admin_schedule(request):
    """ Render the html which contains FullCalendar JS code.
    FullCalendar calls EventsViewSet """
    return render(request, 'scheduler/admin_schedule.html')