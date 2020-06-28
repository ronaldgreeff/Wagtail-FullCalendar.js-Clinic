from rest_framework import serializers
from scheduler.models import TimeStampedModel, Event, Appointment, Service
from myusers.models import Doctor, Patient, User


# class UserField(serializers.RelatedField):
#     def to_representation(self, instance):
#         # return '{}'.format(instance.first_name)
#         return {
#             'first_name': instance.first_name,
#             'last_name': instance.last_name
#         }

class EventSerializer(serializers.ModelSerializer):
    # users = UserField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ['title', 'start', 'end', 'users']


# class ServiceField(serializers.RelatedField):
#     # def to_internal_value(self, value):
#     #     print(value)
#     def to_representation(self, value):
#         return '{}'.format(value.name)

# class DoctorField(serializers.RelatedField):
#     def to_representation(self, value):
#         return '{}'.format(value.user.first_name)

# class PatientField(serializers.RelatedField):
    # def to_internal_value(self, value):
    #     print(value, 'value')
    # def to_representation(self, value):
    #     return '{}'.format(value.first_name)
# class PatientField(serializers.RelatedField):
#     def to_internal_value(self, value):
#         print(value, 'value')


# TODO: should be under myuser.serializers
# class PatientIdField(serializers.RelatedField):
#     def to_internal_value(self, value):
#         return int(value)

#     def to_representation(self, value):
#         return str(value)
class PatientSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(read_only=True, source='id')

    class Meta:
        model = Patient
        fields = ['patient_id', 'first_name', 'last_name',
        'email_address', 'phone_number']

class AppointmentSerializer(serializers.ModelSerializer):
    # title = ServiceField(queryset=Service.objects.all(),
    #     source='service')
    # service = ServiceField(queryset=Service.objects.all())
    # doctor = DoctorField(queryset=Doctor.objects.all())
    # patient = PatientField(queryset=Patient.objects.all())
    # patient = PatientSerializer()

    class Meta:
        model = Appointment
        fields = ['start', 'end',
        'doctor', 'patient', 'service']