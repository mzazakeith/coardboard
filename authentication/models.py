from django.contrib.auth.models import AbstractUser
from django.db import models

Gender_Choices = (
    ('F', 'female'),
    ('M', 'male'),
)


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class TeacherProfile(models.Model):
    # profile_pic = ImageField()
    bio = models.TextField()
    gender = models.CharField(max_length=30, choices=Gender_Choices, default='None', blank=True)
    phone_number = models.PositiveIntegerField()
    github_username = models.CharField(max_length=30)
    user = models.OneToOneField(User)


class StudentProfile(models.Model):
    # profile_pic = ImageField()
    gender = models.CharField(max_length=30, choices=Gender_Choices, default='None', blank=True)
    phone_number = models.PositiveIntegerField()
    user = models.OneToOneField(User)
