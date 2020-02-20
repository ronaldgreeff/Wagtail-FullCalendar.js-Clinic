from rest_framework import serializers
from scheduler.models import TimeStampedModel, Appointment, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
