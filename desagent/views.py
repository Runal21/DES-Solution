from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone


convet={
    'hello':'hello nice to meet you again!!',
    'hi':'hi nice to meet you again!!',
    'how are you?':'i am fine',
    'what is your name?':'my name is DES Agent',
    'what is DES Soln?':'DES is a software that helps you to understand IWM and SWM processes',
    'what is IWM?':'IWM is a process that helps you to understand your business towards India Waste Management',
    'what is SWM?':'SWM is a process that helps you to understand your business towards Singapore Waste Management',
    'tell me about website?':'this is DES Soln where IWM and SWM processes explained deeply',
}

# def chatbot(request):
#     if request.method == 'POST':
#         cm_message = request.POST.get("message")
#         cm_response = convet.get(cm_message,"convet")
#         return JsonResponse({'cm_message':cm_message,'cm_response':cm_response})
#     return render(request, 'desagent/desagent.html')

def chatbot(request):
    if request.method == 'POST':
        cm_message = request.POST.get("cm_message")
        for key, value in convet.items():
            if cm_message == key:
                cm_response = value
                break
        else:
            cm_response = "I'm sorry, I don't understand that message."
        return JsonResponse({'cm_message':cm_message,'cm_response':cm_response})
    return render(request, 'desagent/desagent.html')