from django.shortcuts import render,HttpResponse

# Create your views here.
def feedback(request):
    return HttpResponse('this is a feedback page')