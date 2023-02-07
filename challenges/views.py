from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('My index page view.')


def january(request):
    return HttpResponse('January view.')


def february(request):
    return HttpResponse('February view.')


def march(request):
    return HttpResponse('March view.')


def april(request):
    return HttpResponse('April view.')


def may(request):
    return HttpResponse('May view.')


def june(request):
    return HttpResponse('June view.')


def july(request):
    return HttpResponse('July view.')


def august(request):
    return HttpResponse('August view.')


def september(request):
    return HttpResponse('September view.')


def october(request):
    return HttpResponse('October view.')


def november(request):
    return HttpResponse('November view.')


def december(request):
    return HttpResponse('December view.')
