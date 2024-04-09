from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def articlepage(request):
    return render(request, 'article/articlepage.html')

def addarticlepage(request):
    return HttpResponse("admin will add article")
    # return render(request, 'article/addarticlepage.html')