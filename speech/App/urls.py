from django.urls import path
from . import views

#app_name = "polls"

urlpatterns = [
    path('', views.home, name='home'),
    path('starting_page/', views.starting_page, name='starting_page'),
    path('speech_recognition/', views.speech_recognition, name='speech_recognition'),
    
]
