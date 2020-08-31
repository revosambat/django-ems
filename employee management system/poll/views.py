from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {}
    context['title'] = 'polls'
    return render(request, 'polls/index.html', context)