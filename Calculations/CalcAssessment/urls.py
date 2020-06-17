from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/$', views.login_request, name='login_request'),
    url(r'^logout/$', views.logout_request, name='logout_request'),
]
