from django.shortcuts import render

from django.http import HttpResponseRedirect

from .forms import *
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
               'id_no': cat}
    return render(request, 'watch.html', context)


def insert(request):
    if request.method == 'POST':
        form = image_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/print')
    else:
        form = image_form()
    return render(request, 'form.html', {'form': form})


def print(request):
    a = Image.objects.all()
    return render(request, 'print.html', {'print': a})

def insert_cat(request):
    if request.method == 'POST':
        form = category_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = category_form()
    return render(request, 'cat_form.html', {'form': form})