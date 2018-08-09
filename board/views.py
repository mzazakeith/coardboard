from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from board.forms import NewServiceForm, TopicForm, CommentForm, Dmform, RateForm
from django.contrib.auth import get_user_model
from authentication.models import TeacherProfile, StudentProfile
from board.models import Topic, Comments, Ratings

User = get_user_model()


def index(request):
    return render(request, "index/index.html")

@login_required
def home(request):
    user = request.user
    if user.is_teacher:
        profile = TeacherProfile.objects.get(user=user)
    elif user.is_student:
        profile = StudentProfile.objects.get(user=user)
    messages = request.user.outbox.all()
    inbox = request.user.inbox.filter(read=False)
    return render(request, "home.html", locals())

@login_required
def read(request, msg_id):
    request.user.inbox.filter(pk=msg_id, read=False).update(read=True)
    return redirect('home')

@login_required
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

@login_required
def userprofile(request, user_id):
    online = request.user
    dmform = Dmform()
    form = RateForm()
    users = User.objects.get(id=user_id)
    ratesum = Ratings.objects.filter(rated=users).aggregate(Sum('rate'))
    count = Ratings.objects.filter(rated=users).count()
    if count == 0 :
        rate = 0
    else:
        rate = ratesum['rate__sum']/count
    if request.method == 'POST':
        dmform = Dmform(request.POST)
        if dmform.is_valid():
            dm = dmform.save(commit=False)
            dm.sender = request.user
            dm.reciever = users
            dm.save()
    if users.is_teacher:
        profile = TeacherProfile.objects.get(user=users)
    elif users.is_student:
        profile = StudentProfile.objects.get(user=users)
    return render(request, 'userprofile.html', {"user": users, "profile": profile, "dm": dmform, "form": form, "rate":rate, "online":online})


def forum(request):
    comments = Comments.objects.all()
    comment_form = CommentForm()
    current_user = request.user
    topics = Topic.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = current_user
            topic.save()
            return redirect('/forum')
    else:
        form = TopicForm()
    return render(request, "forum.html",
                  {"form": form, "topics": topics, 'comment': comment_form, "comments": comments})

@login_required
def comment(request, topic_id):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, pk=topic_id)
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.topic_id = topic
            comment.save()
            return redirect(forum)
    else:
        comment_form = CommentForm()
    return render(request, 'forum.html', {'comment': comment_form})


def rate(request, user_id):
    form = RateForm()
    users = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = RateForm(request.POST, request.FILES)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.rated = users
            rate.save()
            return redirect('/userprofile/'+user_id)
    else:
        form = RateForm()
    return redirect('/userprofile/' + user_id)

