from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from appAccount.forms import CostumeUserCreationForm
from appAccount.backends import EmailBackend
from django.contrib.auth.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect('appBlog:home')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            user = EmailBackend.authenticate(request, request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('appBlog:home')
        else:
            messages.error(request, 'Wrong Information')
            return redirect('appAccount:login')

    return render(request, 'appAccount/login.html')


def logout_view(request):
    try:
        logout(request)
        messages.success(request, 'Logout Successfully')
        return redirect('appAccount:login')
    except:
        messages.error(request, 'Logout Failed')
        return redirect('appBlog:home')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('appBlog:home')
    if request.method == 'POST':
        form = CostumeUserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email'])
            if user:
                messages.error(request, 'Account exists,Try Again')
                return redirect('appAccount:signup')
            form.save()
            messages.success(request, 'Sign Up Successfully')
            return redirect('appAccount:login')
        else:
            messages.error(request, 'Wrong Information,Try Again')
            return redirect('appAccount:signup')

    return render(request, 'appAccount/signup.html', {'form': CostumeUserCreationForm()})

