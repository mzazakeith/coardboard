from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from authentication.forms import TeacherSignupForm, StudentSignupForm, CreateTeacherProfileForm, \
    CreateStudentProfileForm
from authentication.models import TeacherProfile

User = get_user_model()


def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_student = False
            user.is_teacher = True
            user.save()
            return redirect(create_teacher_profile)
    else:
        form = TeacherSignupForm()
    return render(request, 'registration/teacher_signup.html', {'form': form})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_student = True
            user.is_teacher = False
            user.save()
            return redirect(create_student_profile)
    else:
        form = StudentSignupForm()
    return render(request, 'registration/student_signup.html', {'form': form})


@login_required
def create_teacher_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateTeacherProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('/')
    else:
        form = CreateTeacherProfileForm()
    return render(request, 'profile/teacher_profile.html', {"form": form, "user": current_user})


@login_required
def create_student_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateStudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('/')
    else:
        form = CreateStudentProfileForm()
    return render(request, 'profile/student_profile.html', {"form": form, "user": current_user})
