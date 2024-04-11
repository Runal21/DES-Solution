from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone



def ask_openai(cm_message):
    cm_response = openai.Completion.create(
        model= 'gpt-3.5-turbo-1106',
        prompt= cm_message,
        max_tokens =150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer=cm_response.choice[0].text.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        cm_message = request.POST.get("message")
        cm_response = ask_openai(cm_message)
        return JsonResponse({'cm_message':cm_message,'cm_response':cm_response})
    return render(request, 'desagent/desagent.html')