from django.contrib.auth import get_user_model
from django import forms

from board.models import Service, Topic, Comments, Ratings
from authentication.models import Messages

User = get_user_model()


class Dmform(forms.ModelForm):
    class Meta:
        model = Messages
        exclude = ['sender', 'reciever', 'time_sent', 'read']


class NewServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['user']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ['user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['commenter','topic_id']


class RateForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['rated']