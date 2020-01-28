from django.contrib import admin
from scheduler.models import Service, CalendarEvent

# Register your models here.
admin.site.register(Service)
admin.site.register(CalendarEvent)