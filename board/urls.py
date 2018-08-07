from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^new-service$', views.new_service, name='new-service'),
    url(r'^userprofile/(?P<user_id>\d+)', views.userprofile, name='profile')
]



