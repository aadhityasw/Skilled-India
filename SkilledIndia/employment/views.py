from django.shortcuts import render
from .forms import EmploymentForm
from django.http import HttpResponse
from .models import Employment

def Employment_List(request) :
    return render(request, 'employment/index.html', {'employees' : Employment.objects.all()})

def Employment_Details(request, emp_id) :
    context = {'employee' : Employment.objects.get(id=emp_id)}
    return render(request, 'employment/details.html', context)

def Employment_Apply(request) :
    if request.method == 'POST':  # data sent by user
        form = EmploymentForm(request.POST)
        if form.is_valid():
            form.save()  # this will save details to database
            return HttpResponse('Employee details added to database')
    else:  # display empty form
        form = EmploymentForm()
    return render(request, 'employment/jobportal.html', {'emp_form' : form})