from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

# DRF
from rest_framework import routers
from . api import api_router
from scheduler import views

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),

    url(r'^api/', views.GetSchedule.as_view(), name='get_schedule'),
    url(r'^ajax/event_service_duration/$', views.event_service_duration, name='event_service_duration'),
    url(r'^ajax/patient_lookup/$', views.patient_lookup, name='patient_lookup'),
    # url(r'^api/insert/', views.InsertEventView.as_view(), name='schedule_insert'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Wagtail's API
    url(r'^api/v2/', api_router.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),

    url(r'^django-admin/', admin.site.urls),

    # Wagtail's def. page serving mechanism - last pattern in list:
    url(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
