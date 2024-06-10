from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def logout(request):
    auth_logout(request)
    return redirect('oidc_logout')


def home(request):
    return render(request, 'myapp/home.html')
