from django.contrib import admin
from scheduler.models import Service, CalendarEvent, Enquirer, PickDateTimePage
# Register your models here.
admin.site.register(Service)
admin.site.register(CalendarEvent)
admin.site.register(Enquirer)
admin.site.register(PickDateTimePage)