from django.urls import path
from . import views

urlpatterns = [
    path('', views.Project_Search, name='project-index'),

    path('<int:proj_id>/', views.Project_Individual, name='project-details'),

    path('add/', views.Project_Add, name='add-proj'),
]
