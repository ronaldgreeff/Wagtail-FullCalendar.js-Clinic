from rest_framework import serializers
from scheduler.models import TimeStampedModel, Event, Appointment, Service
from myusers.models import Doctor, Patient, User


class PatientSerializer(serializers.ModelSerializer):

    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source='id')

    class Meta:
        model = Patient
        fields = ['patient_id', 'first_name', 'last_name',
        'email_address', 'phone_number']


class AppointmentSerializer(serializers.ModelSerializer):

    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), allow_null=True)

    class Meta:
        model = Appointment
        fields = ['start', 'end',
        'doctor', 'patient', 
        'service']

    def create(self, validated_data):

        appointment = Appointment.objects.create(**validated_data)

        return appointment


class EventSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ['title', 'start', 'end', 'users']

    def create(self, validated_data):

        users = validated_data.pop('users')
        event = Event.objects.create(**validated_data)
        [event.users.add(user) for user in users]

        return event