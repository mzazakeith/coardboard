from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^signup/teacher/$', views.teacher_signup, name='signup-teacher'),
    url(r'^signup/student/$', views.student_signup, name='signup-student'),
    url(r'^setup/profile-teacher$', views.create_teacher_profile, name='new-teacher-profile'),
    url(r'^setup/profile-student$', views.create_student_profile, name='new-student-profile'),
]


