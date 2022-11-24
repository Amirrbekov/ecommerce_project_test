from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupuser_view(request):

    context = {}
    register = RegisterCustomForm()
    context['register']=register
    if request.method == "GET":
        return render(request, "signupuser.html", context)
    else:
        if request.POST["password"] == request.POST['confirm']:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST['password'])
                user.save()
                login(request, user)
                return redirect('shop:homepage')
            except IntegrityError:
                context['error']="That username has already been taken. Please choose a new username"
                return render(request, 'signupuser.html', context)
        else:
            context['error']="Passwords did not match"
            return render(request, 'signupuser.html', context)

def signinuser_view(request):

    context={}
    logform = LoginCustomerForm()
    context['logform']=logform
    if request.method == "GET":
        return render(request, "signinuser.html", context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context['error']="Username or password did not match"
            return render(request, "signinuser.html", context)
        else:
            login(request, user)
            return redirect("shop:homepage")

@login_required
def logoutuser_view(request):
    logout(request)
    return redirect("account:signinuser")

def about_view(request):

    return render(request, "about.html")