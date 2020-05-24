from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import EventSerializer, AppointmentSerializer
from scheduler.models import Event, Appointment

from itertools import chain
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# TODO: cleanup imports ^

class EventsViewSet(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        events = EventSerializer(Event.objects.all(), many=True)
        appointments = AppointmentSerializer(Appointment.objects.all(), many=True)
        return Response(list(chain(events.data, appointments.data)))


def admin_schedule(request):
    """ Render the html which contains FullCalendar JS code.
    FullCalendar calls a url to EventsViewSet """
    
    return render(request, 'scheduler/admin_schedule.html')