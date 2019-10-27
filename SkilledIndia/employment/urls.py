from django.urls import path
from . import views

urlpatterns = [
    path('', views.Employment_List, name='employment-index'),

    path('<int:emp_id>/', views.Employment_Details, name='employment-details'),

    path('apply/', views.Employment_Apply, name='emp_application'),
]
