from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
# Create your views here.
def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # fetch the post by primary key
    return render(request, 'blog/post_detail.html', {'post': post})

#Create Post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("blog:blog_list")
            
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form" : form})

@login_required
def post_update(request, id):
    
    post = get_object_or_404(Post, id=id)
    
    #security check
    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to edit this post")
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post updated successfully!")
            return redirect("blog:blog_list")
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})   

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.user != post.author:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("blog:blog_list")

    return render(request, "blog/post_confirm_delete.html", {"post": post})
<<<<<<< HEAD
=======

>>>>>>> f0764ea (final commit)
