from django.conf.urls import include, url
from crm import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^sale_index/', views.sale_index,name='sale_index'),
    url(r'^sole_baobiao/', views.sole_baobiao,name='sole_baobiao'),
]
