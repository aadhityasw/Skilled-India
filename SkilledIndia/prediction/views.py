from django.shortcuts import render
from django.http import HttpResponse
from .apps import PredictionConfig
from rest_framework.views import APIView


def Prediction_List(request) :
    return HttpResponse("A list of all the predictions that can be made.")

def Prediction_Time(request) :
    if request.method == 'GET' :
        sector_data = request.GET['sector']
        budget_data = request.GET['budget']
        skworkforce_data = request.GET['skilled_workers']
        uskworkforce_data = request.GET['unskilled_workers']
        duration = PredictionConfig.duration_predictor.predict([[sector_data, budget_data, skworkforce_data, uskworkforce_data]])[0]
        context = {
            'result_render' : True,
            'budget_data' : budget_data,
            'sector_data' : sector_data,
            'skworkforce_data' : skworkforce_data,
            'uskworkforce_data' : uskworkforce_data,
            'duration_data' : duration,
        }
        print('Duration : ', duration)
        return render(request, 'prediction/time.html', context)
    else :
        return render(request, 'prediction/time.html', {'result_render' : False})

def Prediction_Workforce(request) :
    if request.method == 'GET' :
        budget_data = request.GET['budget']
        sector_data = request.GET['sector']
        duration_data = request.GET['duration']
        skworkforce = PredictionConfig.skilled_workforce_predictor.predict([[sector_data, budget_data, duration_data]])[0]
        uskworkforce = PredictionConfig.unskilled_workforce_predictor.predict([[sector_data, budget_data, duration_data]])[0]
        context = {
            'result_render' : True,
            'budget_data' : budget_data,
            'sector_data' : sector_data,
            'skworkforce_data' : skworkforce,
            'uskworkforce_data' : uskworkforce,
            'duration_data' : duration_data,
        }
        print('Skilled : ', skworkforce)
        print('Unskilled : ', uskworkforce)
        return render(request, 'prediction/workforce.html', context)
    else :
        return render(request, 'prediction/workforce.html') 

def Prediction_Budget(request) :
    if request.method == 'GET' :
        duration_data = request.GET['duration']
        sector_data = request.GET['sector']
        skworkforce_data = request.GET['skilled_workers']
        uskworkforce_data = request.GET['unskilled_workers']
        budget = PredictionConfig.budget_predictor.predict([[sector_data, skworkforce_data, uskworkforce_data, duration_data]])[0]
        context = {
            'result_render' : True,
            'budget_data' : budget,
            'sector_data' : sector_data,
            'skworkforce_data' : skworkforce_data,
            'uskworkforce_data' : uskworkforce_data,
            'duration_data' : duration_data,
        }
        print('Budget : ', budget)
        return render(request, 'prediction/budget.html', context)
    else :
        return render(request, 'prediction/budget.html')
