from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import EventSerializer
from scheduler.models import Event, Appointment
from itertools import chain

from django.http import HttpResponse
import datetime
import json


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def admin_schedule(request):
    
    #     # events = Event.objects.filter(
    #     #               user=request.user, start__gte=start, end__lte=end
    #     #          ).values('id', 'title', 'start', 'end')
    #     # data = json.dumps(list(events), cls=DjangoJSONEncoder)

    #     return HttpResponse(json.dumps(data))

    return render(request, 'scheduler/admin_schedule.html')