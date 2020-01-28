from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import CalendarEventSerializer
from scheduler.models import CalendarEvent


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer