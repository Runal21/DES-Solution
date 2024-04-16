from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone

convet = {
    'hello': 'Hello! Nice to meet you again!!',
    'hi': 'Hi! Nice to meet you again!!',
    'hey': 'Hey! Nice to meet you again!!',
    'how are you?': 'I am fine, thank you for asking!',
    'what is your name?': 'My name is DES Agent.',
    'what is DES Soln?': 'DES Soln is a software platform designed to facilitate waste management processes, providing insights and solutions for both India Waste Management (IWM) and Singapore Waste Management (SWM).',
    'what is IWM?': 'IWM stands for India Waste Management, which refers to the process of managing and handling waste generated within India. DES Soln offers tools and resources to optimize waste management practices in the Indian context.',
    'what is SWM?': 'SWM stands for Singapore Waste Management, which involves the management and disposal of waste in Singapore. DES Soln provides insights and strategies for efficient waste management in Singapore.',
    'tell me about the website?': 'DES Soln is a comprehensive platform that offers detailed information and resources related to waste management processes. It covers topics such as waste generation, collection, recycling, and disposal, providing valuable insights for businesses and individuals looking to improve their waste management practices.',
    'what are the key features of DES Soln?': 'DES Soln offers a range of features, including data analytics tools, educational resources, interactive forums, and real-time monitoring capabilities. Users can access information on waste generation trends, recycling rates, regulatory requirements, and best practices for sustainable waste management.',
    'how can DES Soln benefit businesses?': 'Businesses can leverage DES Soln to gain insights into their waste management processes, identify areas for improvement, and implement strategies to reduce waste generation, enhance recycling efforts, and minimize environmental impact. By adopting sustainable waste management practices, businesses can optimize resource utilization, reduce operational costs, and enhance their corporate social responsibility (CSR) initiatives.',
    'how can individuals contribute to waste management efforts through DES Soln?': 'Individuals can use DES Soln to learn about waste management practices, access tips for reducing waste at home and in their communities, and participate in recycling programs and initiatives. By adopting eco-friendly habits and promoting sustainable behaviors, individuals can contribute to the overall goal of minimizing waste and preserving the environment for future generations.',
}


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

# def chatbot(request):
#     if request.method == 'POST':
#         cm_message = request.POST.get("cm_message")
#         cm_response = convet.get(cm_message.lower(), "I'm sorry, I don't understand that message.")
#         return JsonResponse({'cm_message': cm_message, 'cm_response': cm_response})
#     return render(request, 'desagent/desagent.html')

