from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    params = {
        'title': 'Hello./index',
        'msg': 'サンプルページっす',
        'goto': 'next'
    }
    return render(request, 'hello/index.html', params)


def next(request):
    params = {
        'title': 'Hello./next',
        'msg': 'nextページっす',
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)
