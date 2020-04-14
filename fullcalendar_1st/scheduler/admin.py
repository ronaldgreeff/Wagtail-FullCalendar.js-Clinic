from django.contrib import admin
from scheduler.models import Service, Event, Appointment
from myusers.models import User, Doctor, Patient

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)

admin.site.register(Service)

admin.site.register(Appointment)
admin.site.register(Event)