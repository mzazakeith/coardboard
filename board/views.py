from django.shortcuts import render, redirect
from board.forms import NewServiceForm
from django.contrib.auth import get_user_model
from authentication.models import TeacherProfile, StudentProfile

User = get_user_model()


def index(request):
    return render(request, "index/index.html")


def home(request):
    return render(request, "home.html")


def new_service(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = current_user
            service.save()
            return redirect('/home')
    else:
        form = NewServiceForm()
    return render(request, 'new_service.html', {"form": form})


def userprofile(request, user_id):
    users = User.objects.get(id=user_id)
    if users.is_teacher:
        profile = TeacherProfile.objects.get(user=users)
    elif users.is_student:
        profile = StudentProfile.objects.get(user=users)
    return render(request, 'userprofile.html', {"user": users, "profile": profile})
