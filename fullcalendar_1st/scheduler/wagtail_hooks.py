from scheduler.models import Service, Event, Appointment

# from django.db import models
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
# from wagtail.contrib.modeladmin.views import IndexView

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from django.urls import re_path#, include
from django.urls import reverse
from .views import admin_schedule


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^schedule/', admin_schedule, name='admin_schedule'),
    ]

@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        ('Schedule'),
        reverse('admin_schedule'),
        classnames='icon icon-snippet',
        order=1000
    )


class ServiceIndexView(ModelAdmin):
    model = Service

class UnconfirmedAppointmentIndexView(ModelAdmin):
    model = Appointment
    menu_label = 'Unconfirmed'
    list_filter = ['service', 'doctor']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(doctor__isnull=True)

modeladmin_register(ServiceIndexView)
modeladmin_register(UnconfirmedAppointmentIndexView)