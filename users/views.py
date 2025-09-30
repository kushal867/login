from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import LoginForm, RegisterForm

<<<<<<< HEAD
=======
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.authenticate import login
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegisterForm

# Create your views here.
>>>>>>> b1b5901570fae3cee25865860f352f6d277edb70

def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
<<<<<<< HEAD
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('/admin')
    return render(request, 'login.html', {"form": form})
=======
            print("this is form validation")
            if form.get_user():
                login(request,form.get_user())
                return redirect('/admin')
    context = {
        "form":form
    }
    return render(request,'user/login.html',context)
>>>>>>> b1b5901570fae3cee25865860f352f6d277edb70


def user_defined_login(request):
    if request.user.is_authenticated:
        return redirect('/admin')
<<<<<<< HEAD

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/admin')

    return render(request, 'user_login.html', {"form": form})
=======
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
>>>>>>> b1b5901570fae3cee25865860f352f6d277edb70


def register(request):
    form = RegisterForm()
<<<<<<< HEAD
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/userlogin')
    return render(request, 'register.html', {"form": form})
=======
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
>>>>>>> b1b5901570fae3cee25865860f352f6d277edb70
