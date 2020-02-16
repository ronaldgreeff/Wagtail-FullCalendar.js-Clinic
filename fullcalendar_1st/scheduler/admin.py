from django.contrib import admin
from scheduler.models import Service, Enquiry, Appointment, Event
from users.models import Enquirer, User

admin.site.register(Service)
admin.site.register(Enquiry)
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(Enquirer)
admin.site.register(User)