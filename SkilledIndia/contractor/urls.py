from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contractor_List, name='contractor-list'),

    path('<int:con_id>/', views.Contractor_Details, name='contractor-details'),

    path('apply/', views.Contractor_Apply, name='contractor-estimate'),
]
