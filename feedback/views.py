from django.shortcuts import render, HttpResponse , redirect
from .models import Feedback,FeedbackReply
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login')

def feedbackview(request):
    feedbacks = Feedback.objects.all()
    feedback_with_replies = []
    for feedback in feedbacks:
        # Get all replies for the current feedback
        replies = FeedbackReply.objects.filter(feedback=feedback)
        feedback_with_replies.append((feedback, replies))
    return render(request, 'feedback/feedbackview.html', {'feedback_with_replies': feedback_with_replies})

    # fbreplys = FeedbackReply.objects.filter()
    # return render(request, 'feedback/feedbackview.html', {'fbreplys': fbreplys})

@login_required(login_url='/login')
def feedbackform(request):
    if request.method == 'POST':
        fb_uname = request.POST.get('fb_uname')
        fb_email = request.POST.get('fb_email')
        fb_content = request.POST.get('fb_content')

        # Check if the username and email match the authenticated user
        if fb_uname == request.user.username and fb_email == request.user.email:
            # Form validation
            if fb_uname.strip() and fb_email.strip() and fb_content.strip():
                feedbackform = Feedback.objects.create(fb_uname=fb_uname, fb_email=fb_email, fb_content=fb_content)
                feedbackform.save()
                return redirect('feedback_confirmation')
            else:
                messages.error(request, "Please fill in all fields")
        else:
            messages.error(request, "Invalid username or email")
    return render(request, 'feedback/feedbackform.html')

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
