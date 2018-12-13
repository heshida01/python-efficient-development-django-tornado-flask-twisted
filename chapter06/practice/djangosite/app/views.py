# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")


def moments_input(request):
    data ={'content':'请填写内容', 'user_name': '匿名'}
    if request.method == 'POST':  
        form = MomentForm(request.POST, initial = data)  
        if form.is_valid():  
            moment = form.save()  
            moment.save()  
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:  
        form = MomentForm()  
    import os
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print PROJECT_ROOT
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'), {'form': form})  
