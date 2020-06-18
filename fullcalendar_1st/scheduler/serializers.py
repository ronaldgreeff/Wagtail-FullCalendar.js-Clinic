from rest_framework import serializers
from scheduler.models import TimeStampedModel, Event, Appointment, Service
from myusers.models import Doctor, Patient, User


class UserField(serializers.RelatedField):
    def to_representation(self, value):
        return '{}'.format(value.first_name)


class EventSerializer(serializers.ModelSerializer):
    users = UserField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ['start',  'users']



class ServiceField(serializers.RelatedField):
    def to_representation(self, value):
        return '{}'.format(value.name)

class DoctorField(serializers.RelatedField):
    def to_representation(self, value):
        return '{}'.format(value.user.first_name)

class PatientField(serializers.RelatedField):
    def to_representation(self, value):
        return '{}'.format(value.first_name)


class AppointmentSerializer(serializers.ModelSerializer):
    title = ServiceField(queryset=Service.objects.all(),
        source='service')
    service = ServiceField(queryset=Service.objects.all())
    doctor = DoctorField(queryset=Doctor.objects.all())
    patient = PatientField(queryset=Patient.objects.all())

    class Meta:
        model = Appointment
        fields = ['title', 'start', 'end',
        'doctor', 'patient', 'service']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name',
        'email_address', 'phone_number']

# class AppointmentValidSerializer(serializers.Serializer):
#     start = serializers.DateTimeField(
#         format="%Y-%m-%d %H:%M:%S",
#         required=False, read_only=True)


# class EventValidSerializer(serializers.Serializer):
#     start = serializers.DateTimeField(
#         format="%Y-%m-%d %H:%M:%S",
#         required=False, read_only=True)