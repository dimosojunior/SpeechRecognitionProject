from django.urls import path
from . import views

#app_name = "polls"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('all_speeches/', views.all_speeches, name='all_speeches'),
    path('starting_page/', views.starting_page, name='starting_page'),
    path('speech_recognition/', views.speech_recognition, name='speech_recognition'),
    
]
