from .views import admin_schedule
from django.urls import path

urlpatterns = [
    path('', admin_schedule, name='admin_schedule'),
]