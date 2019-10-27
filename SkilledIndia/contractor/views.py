from django.shortcuts import render
from .forms import ContractorForm
from django.http import HttpResponse
from .models import Contractor

def Contractor_List(request) :
    return render(request, 'contractor/contractor_index.html', {'contractors' : Contractor.objects.all()})

def Contractor_Details(request, con_id) :
    context = {'contractor' : Contractor.objects.get(id=con_id)}
    return render(request, 'contractor/details.html', context)

def Contractor_Apply(request) :
    if request.method == 'POST':  # data sent by user
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()  # this will save details to database
            return HttpResponse('Contractor estimation added to database')
    else:  # display empty form
        form = ContractorForm()
    return render(request, 'contractor/estimate.html', {'contractor_estimate_form' : form})