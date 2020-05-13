from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import EventSerializer
from scheduler.models import Event, Appointment


def admin_schedule(request):
	events = Event.objects.all()
	return render(request, 'scheduler/admin_schedule.html', {'data': events})
