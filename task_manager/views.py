from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

def main_page(request):
    return HttpResponse("hello world")