from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello,world.You're at the polls index.")
def detail(request,question_id):
    return HttpResponse("you are looking at question %s." % question_id)

def results(request,question_id):
    return HttpResponse("you are results at question %s." % question_id)

def vote(request,question_id):
    return HttpResponse("you are voting on question %s." % question_id)