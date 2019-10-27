from django.shortcuts import render
from .forms import ProjectForm
from django.http import HttpResponse
from .models import Project

def Project_Search(request) :
    return render(request, 'project/index.html', {'projects' : Project.objects.all()})

def Project_Individual(request, proj_id) :
    context = {'project' : Project.objects.get(id=proj_id)}
    return render(request, 'project/details.html', context)

def Project_Add(request) :
    if request.method == 'POST':  # data sent by user
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()  # this will save the details to database
            return HttpResponse('Project details added to database')
    else:  # display empty form
        form = ProjectForm()
    return render(request, 'project/addproj.html', {'add_proj_form' : form})
