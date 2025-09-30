from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.authenticate import login
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegisterForm

# Create your views here.

def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("this is form validation")
            if form.get_user():
                login(request,form.get_user())
                return redirect('/admin')
    context = {
        "form":form
    }
    return render(request,'user/login.html',context)


def user_defined_login(request):
    if request.user.is_authenticated:
        return redirect('/admin')
    form = LoginForm()
    context = {
        "form":form
    }
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username =request.POST['username'], password = request.POST['password'])
            if user is not None:
                login(request,user )
                return redirect('/admin')

    return render(request, 'user/user_login.html',context)


def register(request):
    form = RegisterForm()
    context = {
        "form":form
    }
    if request.method =="POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            return redirect('/user/userlogin')
    return render(request, 'user/register.html', context)
