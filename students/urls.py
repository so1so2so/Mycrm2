from django.conf.urls import include, url
from students import views

urlpatterns = [
    url(r'^$', views.student_index, name='student_index'),
]
