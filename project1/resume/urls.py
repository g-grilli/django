from django.conf.urls import url

from . import views

app_name = 'resume'

urlpatterns = [
    url(r'^$', views.resume, name='resume'),
]