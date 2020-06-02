from rest_framework import serializers
from scheduler.models import TimeStampedModel, Event, Appointment, Service
from myusers.models import Doctor, Patient, User


# class UserField(serializers.RelatedField):
#     def to_representation(self, value):
#         return '{}'.format(value.first_name)


class EventSerializer(serializers.ModelSerializer):
    # users = UserField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ['start']



# class ServiceField(serializers.RelatedField):
#     def to_representation(self, value):
#         return '{}'.format(value.name)

# class DoctorField(serializers.RelatedField):
#     def to_representation(self, value):
#         return '{}'.format(value.user.first_name)

# class PatientField(serializers.RelatedField):
#     def to_representation(self, value):
#         return '{}'.format(value.first_name)


class AppointmentSerializer(serializers.ModelSerializer):
    # adding title, which doesn't exist in model, to be consistent with events
    # doctor = DoctorField(queryset=Doctor.objects.all())
    # patient = PatientField(queryset=Patient.objects.all())
    # title = ServiceField(queryset=Service.objects.all(), source='service')

    class Meta:
        model = Appointment
        fields = ['start']