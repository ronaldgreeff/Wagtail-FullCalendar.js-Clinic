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
# class PatientSerializer(serializers.ModelSerializer):
#     patient_id = serializers.IntegerField(read_only=True, source='id')

#     class Meta:
#         model = Patient
#         fields = ['patient_id', 'first_name', 'last_name',
#         'email_address', 'phone_number']

# class AppointmentSerializer(serializers.ModelSerializer):
#     # title = ServiceField(queryset=Service.objects.all(),
#     #     source='service')
#     # service = ServiceField(queryset=Service.objects.all())
#     # doctor = DoctorField(queryset=Doctor.objects.all())
#     # patient = PatientField(queryset=Patient.objects.all())
#     # patient = PatientSerializer()

#     class Meta:
#         model = Appointment
#         fields = ['start', 'end',
#         # 'doctor', 'patient', 
#         'service']


# class PatientIdField(serializers.RelatedField):
#     def to_internal_value(self, value):
#         # return int(value)
#         return value
#     def to_representation(self, value):
#         # return str(value)
#         return value

##### THIS IS FOR SERIALIZING THE PATIENT LIST (FOR NOW - TODO: USE NESTED IN APPT)
class PatientSerializer(serializers.ModelSerializer):
    # patient_id = PatientIdField(queryset=Patient.objects.all(), source='id')
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source='id')

    class Meta:
        model = Patient
        fields = ['patient_id', 'first_name', 'last_name',
        'email_address', 'phone_number']


# class DoctorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ['pk']

#     def create(self, validated_data):
#         return Doctor.objects.get(**validated_data)

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
        # YOU ARE HERE
        # validated_data {'start': datetime.datetime(2020, 4, 30, 23, 0, tzinfo=<UTC>),
        # 'end': datetime.datetime(2020, 5, 1, 0, 0, tzinfo=<UTC>), 'doctor': <Doctor: ron>,
        # 'patient': <Patient: q, t >, 'service': <Service: Appointment (60mins)>}

        patient = validated_data.pop('patient')
        doctor = validated_data.pop('doctor')

        # appointment = Appointment.objects.create(**validated_data)

        patient.appointments.add(appointment)
        doctor.appointment_set.add(appointment)

        return appointment