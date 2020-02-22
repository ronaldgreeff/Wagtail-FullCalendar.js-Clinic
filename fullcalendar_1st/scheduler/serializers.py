from rest_framework import serializers
from scheduler.models import TimeStampedModel, Event#, Appointment

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
