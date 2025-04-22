from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
from .forms import QuestionForm, AnswerForm

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
    # question_list = Question.objects.order_by("-pub_date")
    # return render(request, "topics/index.html", {"question_list": question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("topics:detail", question_id=question.id)
    else:
        form = AnswerForm()

    return render(request, "topics/detail.html", {
        "question": question,
        "form": form
    })

def results(request, question_id):
    response = "You're viewing all answers for discussion %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're submitting an answer to discussion %s." % question_id)

def add_question(request, question_id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics:index')
    else:
        form = QuestionForm()
    return render(request, 'topics/add_question.html', {'form': form})

def add_answer(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('topics:detail',
                            question_id=question.id)
    else:
        form = AnswerForm()

    return render(request, 'topics/add_answer.html', {'form': form, 'question': question})

