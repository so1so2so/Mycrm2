from django.conf.urls import include, url
from django.contrib import admin
from king_admin import views
urlpatterns = [
    url(r'^index/$', views.index,name='admin'),
    url(r'^(\w+)/(\w+)/$', views.index_name,name='admin_obj'),
    url(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_obj_change,name='table_obj_change'),
]