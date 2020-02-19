from django.contrib import admin
from scheduler.models import Service, Appointment, Event
from users.models import User, Doctor, Patient

admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)