from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, RegisterForm


# Login using Django's built-in AuthenticationForm
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/admin')

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/admin')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})


# Login using custom LoginForm
def user_defined_login(request):
    if request.user.is_authenticated:
        return redirect('/admin')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/admin')
    else:
        form = LoginForm()

    return render(request, 'user_login.html', {"form": form})


# User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/userlogin')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {"form": form})
