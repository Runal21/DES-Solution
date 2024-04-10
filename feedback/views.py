from django.shortcuts import render, HttpResponse , redirect
from .models import Feedback,FeedbackReply
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')

def feedbackview(request):
    fbreplys = FeedbackReply.objects.all()       
    return render(request,'feedback/feedbackview.html',{'fbreplys':fbreplys})

@login_required(login_url='/login')
def feedbackform(request):
    if request.method == 'POST':
        fb_uname = request.POST.get('fb_uname')
        fb_email = request.POST.get('fb_email')
        fb_content= request.POST.get('fb_content')
        feedbackform = Feedback.objects.create(fb_uname=fb_uname,fb_email=fb_email, fb_content= fb_content)
        feedbackform.save()
        return redirect('feedback_confirmation')
    return render(request,'feedback/feedbackform.html')

def feedback_confirmation(request):
    return render(request, 'feedback/feedback_confirmation.html')

#    feedback, fbr_admin, fbr_reply_content 
def submit_admin_reply(request,fb_uname):
    feedback = Feedback.objects.get(fb_uname=fb_uname)
    if request.method == 'POST':
        fbr_reply_content = request.POST.get('fbr_reply_content')
        # Get the logged-in admin user
        admin_user = request.user
        # Create the feedback reply
        feedback_reply = FeedbackReply.objects.create(feedback=feedback,fbr_admin=admin_user,fbr_reply_content= fbr_reply_content)
        feedback_reply.save()
        return redirect('feedbackview', fb_uname=fb_uname)
    return render(request, 'feedback/admin_reply_form.html')


