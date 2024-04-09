from django.shortcuts import render,HttpResponse

# Create your views here.
def forumpost(request):
    return HttpResponse("this is a forumpost")