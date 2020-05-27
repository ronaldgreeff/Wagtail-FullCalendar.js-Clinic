from django.shortcuts import render

# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from scheduler.serializers import EventSerializer, AppointmentSerializer
from scheduler.models import Event, Appointment

from itertools import chain
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.permissions import IsAuthenticated
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
        if Event elif Appointment
        """
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            print('post serializer valid')
            serializer.save()
            return Response(serializer.data)
 
        print('post serializer invalid\n{}\n---\n{}'.format(request.data, serializer.errors))

        # post serializer invalid
        # <QueryDict: {
        # 'csrftoken': ['EV2SgggyZWWFRD0sFV4ddeSy5W57MNYC6mLVgECrDQekuPIKpOCtPUpOxe9mIpYH'],
        # 'title': ['sdf'],
        # 'start': ['5/6/2020'],
        # 'end': ['5/7/2020'],
        # 'all_day': ['true'],
        # 'success': [''],
        # 'error': ['']}>
        # ---
        # {'start': [ErrorDetail(
        #     string='Datetime has wrong format. Use one of these formats instead:
        #     YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z].', code='invalid')],
        # 'end': [ErrorDetail(
        #     string='Datetime has wrong format. Use one of these formats instead:
        #     YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z].', code='invalid')]}

        return Response(serializer.errors)



def admin_schedule(request):
    """ Render the html which contains FullCalendar JS code.
    FullCalendar calls a url to EventsViewSet """
    return render(request, 'scheduler/admin_schedule.html')