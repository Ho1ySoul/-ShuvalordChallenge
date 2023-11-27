from django import forms
from django.core.mail.backends import console
from django.shortcuts import render, redirect
from django.views.generic import ListView

from heros.forms import HeroUpdate
from heros.models import HeroModel


# Create your views here.
def index(request):
    heros = HeroModel.objects.all()
    context = {
        'heros': heros
    }
    return render(request, 'index.html', context)

def get_ordering(request):
    if request.method=='GET':
        heros = HeroModel.objects.all().order_by('-name')
    console.log(heros)
    print(heros)
    context = {
        'heros': heros
    }
    return render(request, 'index.html', context)


def hero_detail(request, pk):
    hero = HeroModel.objects.get(id=pk)
    if request.method == 'POST':
        form = HeroUpdate(request.POST, instance=hero)
        if form.is_valid():
            form.save()
            return redirect('index-page')
    else:
        form = HeroUpdate(instance=hero)

    context = {
        'form': form,
        'hero': hero
    }
    return render(request, 'hero_detail.html', context)


