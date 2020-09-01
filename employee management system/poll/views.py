from django.shortcuts import render
from django.http import HttpResponse, Http404
from poll.models import *
# Create your views here.

def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html', context)

def details(request, id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request, 'polls/details.html', context)