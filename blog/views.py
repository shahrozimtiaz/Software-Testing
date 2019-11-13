from django.shortcuts import get_object_or_404, render, redirect,reverse
from django.contrib.auth.models import User
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
    return render(request, 'blog/posts.html')

def signout(request):
    logout(request)
    return redirect(reverse('blog:loginPage'))
