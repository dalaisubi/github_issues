from django.urls import path
    
from . import views

app_name='issues'

urlpatterns = [

    path('', views.issuesView , name='issues'),
    
]
