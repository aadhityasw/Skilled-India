from django.shortcuts import render
from django.http import HttpResponse
from .apps import PredictionConfig
from rest_framework.views import APIView


def Prediction_List(request) :
    return HttpResponse("A list of all the predictions that can be made.")

def Prediction_Time(request) :
    if request.method == 'POST' :
        budget_data = request.GET['budget_data']
        return HttpResponse('Data Recieved')
    else :
        return render(request, 'prediction/time.html')

def Prediction_Workforce(request) :
    return render(request, 'prediction/workforce.html')

def Prediction_Budget(request) :
    return render(request, 'prediction/budget.html')
