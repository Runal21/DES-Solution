from django.shortcuts import render,HttpResponse

# Create your views here.
def forumpost(request):
    return render(request, 'forumpost/forumpost.html')