from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def index(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("topics:index")
    else:
        form = QuestionForm()
    question_list = Question.objects.order_by("-pub_date")
    return render(request, "topics/index.html", {
        "question_list": question_list,
        "form": form,
    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('topics:detail', question_id=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'topics/detail.html', {'question': question, 'form': form})


def results( question_id):
    response = "You're viewing all answers for discussion %s."
    return HttpResponse(response % question_id)

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics:index')
    else:
        form = QuestionForm()
    return render(request, 'topics/add_question.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('topics:index')
    else:
        form = UserCreationForm()
    return render(request, 'topics/sign_up.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('topics:index')

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('topics:index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

