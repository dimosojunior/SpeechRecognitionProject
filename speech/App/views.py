from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from .models import *
from .forms import *
from django.http import HttpResponse
from datetime import datetime, timedelta
import pyotp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#C:\Users\DIMOSO JR\Desktop\ProjectWork\SmartInvigilation\SmartInvigilationProject\SmartInvigilationApp
print(BASE_DIR)


#@login_required(login_url='login')
def home(request):

    return render(request,'App/home.html')


@login_required(login_url='home')
def starting_page(request):


    return render(request, 'App/starting_page.html')


@login_required(login_url='home')
def speech_recognition(request):
    error_message =None
    

    if request.method == 'POST':

        random.seed()
        random_number = random.randint(1,100)
        print(f"RandomNumber {random_number}")

        username = request.user.username
        email = request.user.email
        microphone_no = request.POST.get('microphone_no')

        save_speech = SpeechRecognitionHistory.objects.create(username=username, microphone_no=microphone_no, email=email)
        save_speech.save()

        microphone_no_integer = int(microphone_no)



        print(f"MICROPHONE NUMBER {microphone_no_integer}")


        #START SPEECH RECOGNITION
        import speech_recognition as sr

        r = sr.Recognizer()

        mic = sr.Microphone(device_index=microphone_no_integer)

        print("Start Speaking")
        #error_message = "Start Speaking!!"
        #messages.info(request, f'Hey {username} Start Speaking')


        with mic as source:
            audio = r.listen(source)


        try:
            result = r.recognize_google(audio)
        except sr.RequestError:
            #exit("API is unreachable")
            #error_message = "API is unreachable"
            messages.info(request, f'Hey {username}, Requested API is unreachable')
            return redirect("starting_page")


        except sr.UnknownValueError:
            #exit("Unable to recognize speech! ")
            #error_message = "Unable to recognize speech!"
            messages.info(request, f'Hey {username}, Unable to recognize speech!')
            return redirect("starting_page")


        with open(BASE_DIR+f'/SpeechHistory/{random_number}.txt',mode='w') as file:
            file.write(result)

        print("It has stored speech into text in my file")
        #error_message = "It has stored speech into text in my file"
        messages.info(request, f'Hey {username}, It has stored speech into text in my file')
        return redirect("starting_page")


            

    # context = {
    #     "error_message":error_message,
    # }

    # return render(request,'App/starting_page.html',context)