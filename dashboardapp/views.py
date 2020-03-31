from django.shortcuts import render

# Create your views here.

from .models import *


def index(request):
    try:
        msg = Category.objects.all()
    except Category.DoesNotExist:
        msg = None
    context = {'messages': msg}
    return render(request, 'home.html', context)


def item(request, category):
    context = {'id': category}
    return render(request, 'index.html', context)


def watch(request, cat):
    try:
        var = Image.objects.filter(categories=cat)
    except Image.DoesNotExist:
        var = None
    context = {'variables': var,
               'id_no':cat}
    return render(request, 'watch.html', context)

