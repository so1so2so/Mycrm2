from django.conf.urls import include, url
from django.contrib import admin
from king_admin import views
urlpatterns = [
    url(r'^(\w+)/(\w+)/$', views.index_name,name='admin_obj'),
    url(r'^index/$', views.index,name='admin'),
]
