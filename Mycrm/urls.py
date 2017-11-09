from django.conf.urls import include, url
from django.contrib import admin
from crm import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crm/', include("crm.urls")),
    url(r'^students/', include("students.urls")),
    url(r'^king/', include("king_admin.urls")),
]
