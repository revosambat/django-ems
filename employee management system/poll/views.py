from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from poll.models import *
# Create your views here.

@login_required(login_url="/login/")
def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html', context)

@login_required(login_url="/login/")
def details(request, id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request, 'polls/details.html', context)

@login_required(login_url="/login/")
def poll(request, id=None):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['question'] = question
        return render(request, 'polls/poll.html', context)
    if request.method == "POST":
        user_id = 1
        data = request.POST
        ret = Answer.objects.create(user_id = user_id, choice_id = data['choice'])
        if ret:
            return HttpResponse("Your vote is added succesfully ")
        else:
            return HttpResponse("Your vote is not added successfully ") 