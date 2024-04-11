from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone


openai_api_key = 'your key'
openai.api_key = openai_api_key

def ask_openai(cm_message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": cm_message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer



def chatbot(request):
    chats = Chat.objects.filter(cm_user=request.user)

    if request.method == 'POST':
        cm_message = request.POST.get('cm_message')
        cm_response = ask_openai(cm_message)

        chat = Chat(cm_user=request.user, cm_message=cm_message, cm_response=cm_response, cm_created_at=timezone.now())
        chat.save()
        return JsonResponse({'cm_message': cm_message, 'cm_response': cm_response})
    return render(request, 'desagent/desagent.html', {'chats': chats})
