from django.shortcuts import render


def login(request):
    return render(request, 'Auth/login.html')


def signup(request):
    return render(request, 'Auth/signup.html')
