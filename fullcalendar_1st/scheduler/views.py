from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import CalendarEventSerializer
from scheduler.models import CalendarEvent


class LoadEventsView(viewsets.ModelViewSet): # ApiView
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer

# class InsertEventView(ApiView):
# 	pass

# class UpdateEventView(ApiView):
# 	pass

# class DeleteEventView(ApiView):
# 	pass