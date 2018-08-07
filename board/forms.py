from django.contrib.auth import get_user_model
from django import forms

from board.models import Service

User = get_user_model()


class NewServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['user']
