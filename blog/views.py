from django.shortcuts import get_object_or_404, render, redirect,reverse
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages



def loginPage(request):
    if request.method == "POST":
        request.POST.get('username')
        if User.objects.filter(username=request.POST.get('username')).exists():
            print('found user')
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                print('valid creds')
                login(request, user)
                return redirect(reverse('blog:posts'))
            else:
                print('auth failed')
                messages.error(request, 'Username is either already taken or password is not correct')
                return redirect(reverse('blog:loginPage'))
        else:
            print('creating')
            user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'))
            login(request, user)
            return render(request, 'blog/welcome.html')

    return render(request, 'blog/login.html')

def posts(request):
    posts = list(Post.objects.all().order_by('-timeStamp'))
    return render(request, 'blog/posts.html',{'posts':posts})

def makePost(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('post'):
            user = User.objects.get(username=request.user.username)
            Post(user=user,title=request.POST.get('title'),post=request.POST.get('post')).save()
            return redirect(reverse('blog:posts'))

    return render(request, 'blog/makePost.html')

def signout(request):
    logout(request)
    return redirect(reverse('blog:loginPage'))
