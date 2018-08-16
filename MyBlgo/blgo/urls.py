from django.conf.urls import url, include
from blgo import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^logout/$', views.logout),
    url(r'^captcha/', include('captcha.urls'))
]
