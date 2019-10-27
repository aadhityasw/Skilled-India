"""SkilledIndia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('employment/', include('employment.urls')),

    path('contractor/', include('contractor.urls')),

    path('project/', include('project.urls')),

    path('prediction/', include('prediction.urls')),

    path('', views.Home_Page),

    path('contact/', views.Contact_Us), 
]

admin.site.site_header = "Skilled India"
admin.site.site_title = "Skilled India Admin Portal"
admin.site.index_title = "Welcome to Skilled India Portal"