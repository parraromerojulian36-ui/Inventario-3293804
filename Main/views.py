from django.shortcuts import render


def login_view(request):
    return render(request, 'login/Login.html')


def home(request):
    return render(request, 'login/home.html')
