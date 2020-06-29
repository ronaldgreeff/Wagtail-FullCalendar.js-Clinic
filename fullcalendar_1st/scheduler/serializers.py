from rest_framework import serializers
from scheduler.models import TimeStampedModel, Event, Appointment, Service
from myusers.models import Doctor, Patient, User


class EventSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ['title', 'start', 'end', 'users']

    def create(self, validated_data):
        print('\n*****\nvalidated_data', validated_data)

        return


##### THIS IS FOR SERIALIZING THE PATIENT LIST (FOR NOW - TODO: USE NESTED IN APPT)
class PatientSerializer(serializers.ModelSerializer):
    # patient_id = PatientIdField(queryset=Patient.objects.all(), source='id')
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source='id')

    class Meta:
        model = Patient
        fields = ['patient_id', 'first_name', 'last_name',
        'email_address', 'phone_number']


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = ['start', 'end',
        'doctor', 'patient', 
        'service']

    def create(self, validated_data):
        print('\n*****\nvalidated_data', validated_data)

        appointment = Appointment.objects.create(**validated_data)

        return appointment