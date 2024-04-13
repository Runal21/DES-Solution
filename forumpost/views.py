from django.shortcuts import render, redirect
from .models import ForumPost, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import ForumPost, Comment



def forumpost(request):
    posts = ForumPost.objects.all()
    return render(request, 'forumpost/forumpost.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        fp_title = request.POST.get('fp_title')
        fp_content = request.POST.get('fp_content')
        if fp_title and fp_content:
            forum_post = ForumPost.objects.create(fp_title=fp_title, fp_content=fp_content, fp_author=request.user)
            forum_post.save()
            # return redirect('post_detail', pk=forum_post.pk)
    return render(request, 'forumpost/create_fp.html')

def post_detail(request,pk):
    post = get_object_or_404(ForumPost,pk=pk)
    comments = post.comment_set.all()
    return render(request, 'forumpost/fp_detail.html', {'post': post, 'comments': comments})

@login_required
def add_comment(request,pk):
    if request.method == 'POST':
        post = get_object_or_404(ForumPost,pk=pk)
        cmfp_content = request.POST.get('cmfp_content')
        comments = Comment.objects.create(cmfp_content=cmfp_content,post=post, cmfp_author=request.user)
        comments.save()
        return redirect('post_detail',pk=pk)
    return render(request, 'forumpost/add_comment.html', {'post': post})