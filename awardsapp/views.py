# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    projects = Projects.objects.all()
    context = {
    "projects":projects,
    }
    return render(request, 'index.html', locals())

ef registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)
