from rest_framework import serializers
from scheduler.models import TimeStampedModel, Event, Appointment, Service
from myusers.models import Doctor, Patient, User


# TODO: need to prefix or suffix the ids for events and appointments

class UserField(serializers.RelatedField):
    def to_representation(self, value):
        return '{}'.format(value.first_name)

class EventSerializer(serializers.ModelSerializer):
    users = UserField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = '__all__'


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
    # adding title, which doesn't exist in model, to be consistent with events
    doctor = DoctorField(queryset=Doctor.objects.all())
    patient = PatientField(queryset=Patient.objects.all())
    title = ServiceField(queryset=Service.objects.all(), source='service')

    class Meta:
        model = Appointment
        fields = '__all__'

# for a in appointments:
#     ad = {}
#     ad['title'] = a.service.name
#     ad['doctor'] = a.doctor.user.first_name
#     ad['patient'] = a.patient.first_name
#     ad['start'] = datetime.datetime.strptime(str(a.start.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#     ad['end'] = datetime.datetime.strptime(str(a.end.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#     data.append(ad)

# for e in events:
#     ed = {}
#     ed['title'] = e.title
#     ed['start'] = datetime.datetime.strptime(str(e.start.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#     ed['end'] = datetime.datetime.strptime(str(e.end.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#     ed['all_day'] = e.all_day
#     # TODO - users, models.ManyToManyField('myusers.User')