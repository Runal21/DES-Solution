"""
URL configuration for DESSoln project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from article.views import *
from feedback.views import *
from desagent.views import *
from forumpost.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name="home"), #Home page
    path('about/',about,name="about"), #about page
    path('contact/',contact,name="contact"), #contact page


    path('login/',loginpage,name="login"), #login page
    path('register/',registerpage,name="register"), #register page
    path('logout/',logoutpage,name="logout"), #login page

    path('article/',articlepage,name="articlepage"),#Article Page
    path('addarticle/',addarticlepage,name="addarticlepage"),#Article Page


    path('forumpost/',forumpost,name="forumpost"),
    path('post/create/',create_post, name='create_post'),
    path('post/detail/<int:pk>/',post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),

    path('pdfpowerbi/',open_powerbi,name="open_powerbi"),
    path('desagent-chatbot', chatbot, name='chatbot'),



    path('feedback/',feedbackview,name="feedbackview"), #Feedback view to specs user
    path('feedbackform/',feedbackform,name="feedbackform"), #Feedback form
    path('feedback_confirmation/',feedback_confirmation,name="feedback_confirmation"), #Feedback feedback_confirmation
    path('submit_admin_reply/',submit_admin_reply,name="submit_admin_reply"), #Feedback feedback_confirmation




    path('admin/', admin.site.urls),
]
