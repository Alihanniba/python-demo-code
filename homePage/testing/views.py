# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
#限制视图只能服务规定的http方法
from django.views.decorators.http import require_http_methods
# Create your views here.

def hello(request):
    return HttpResponse("hello,world");

# @require_http_methods(["GET", "POST"])
def test(request):
    return render(request,'templates/index.html')


