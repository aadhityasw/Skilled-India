from django.urls import path
from . import views

urlpatterns = [
    path('', views.Prediction_List),

    path('time/', views.Prediction_Time, name='time-predict'),

    path('workforce/', views.Prediction_Workforce, name='workforce-predict'),

    path('budget/', views.Prediction_Budget, name='budget-predict'),
]
