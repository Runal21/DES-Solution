from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required(login_url='/login')
def addarticlepage(request):
    if request.method == 'POST':
        art_title = request.POST.get('art_title')
        art_content = request.POST.get('art_content')
        art_image = request.FILES.get('art_image')
        art_author = request.POST.get('art_author')

        article = Article(art_title=art_title,art_content=art_content,art_author=art_author,art_image=art_image )
        article.save()

        messages.success(request, 'Article created successfully.')  
    return render(request, 'article/createarticle.html')


@login_required(login_url='/login')
def articlepage(request):
    articles = Article.objects.all()
    return render(request, 'article/articlepage.html', {'articles': articles})
