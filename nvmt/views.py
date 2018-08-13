from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
# rest_framework imports
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# model imports
from .models import *
# from .serializers import *
# Create your views here.

def home(request):
    context = {}
    return render(request, 'nvmt/homepage.html', context)

def test_start(request):
    context = {
        user: '',
        subject: '',
        test: '',
        trial: '',
        cards: [],
        points: []
    }
    return render(request, 'nvmt/index.html', context)

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    else:
        return redirect('home')

@login_required
def logout_view(request):
    logout(request)

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['signup_email']
        password1 = request.POST['signup_password']
        password2 = request.POST['repeate_signup_password']
        if password1 == password2:
            new_user = User.objects.create_user(first_name, last_name, email, password1)
    else:
        return redirect('home')

def register_subject(request):
    context = {}
    return render(request, 'nvmt/registration.html', context)

def test_finished(request):
    context = {}
    return render(request, 'nvmt/finished.html', context)
