from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^new-service$', views.new_service, name='new-service'),
    url(r'^userprofile/(?P<user_id>\d+)', views.userprofile, name='profile'),
    url(r'^forum$', views.forum, name='forum'),
    url(r'^comment/(?P<topic_id>\d+)', views.comment, name='comment'),
    url(r'^read/(?P<msg_id>\d+)', views.read, name='read')
]



