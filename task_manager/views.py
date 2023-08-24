from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django import forms
from django.utils.translation import gettext as _


def main_page(request):
    return render(request, "index.html")