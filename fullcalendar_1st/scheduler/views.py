from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from scheduler.serializers import EnquirySerializer
# from scheduler.models import Enquiry

#####################################
#
# It's wagtail - views are in models
#
#####################################

class LoadEventsView(viewsets.ModelViewSet): # ApiView
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    # jsonencode serializer.data
    # HttpResonse(JSON)

# class InsertEventView(ApiView):
#	if request.POST.data isvalid
# 	calendar_event = CalendarEvent()
#	title, start, end, allday

# class UpdateEventView(ApiView):
# 	CalendarEvent.objects.get(id=id)
#	for i in request.POST.data
#		event[i] = data[i]
#	event.save()

# class DeleteEventView(ApiView):
# 	Calendar.objects.delete(id=id)