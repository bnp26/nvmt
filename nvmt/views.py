from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
# rest_framework imports
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# model imports
from .models import *
from psych.forms import GetTestForm

import json
# from .serializers import *
# Create your views here.

STORED_TEST = {}

def test_home(request):
    context = {}
    if request.method == 'POST':
        get_test_form = GetTestForm(request.POST)
        if get_test_form.is_valid():
            print(get_test_form)
            potential_test_code = get_test_form.clean()
            test_code = potential_test_code['test_code']
            test_exists = get_object_or_404(Test, test_code=test_code)
            context['test'] = test_exists
            return redirect('/nvmt/test-start/{0}'.format(test_code))
        else:
            return redirect('/nvmt')
    else:
        context['get_test_form'] = GetTestForm
        template = "nvmt/test_home.html"
        return render(request, template, context)

def test_start(request, test_code):
    '''
    if request.method == 'POST':
        test_data = request.POST.get('test_data')
        for trial in test_data['trials']:
    '''
    context = {
        'test': '',
        'trial': '',
        'cards': [],
        'points': []
    }
    context['test'] = get_object_or_404(Test, test_code=test_code)
    return render(request, 'nvmt/index.html', context)

def send_test_data(request, test_code):
    if request.is_ajax():
        if request.method == 'POST':
            test = json.loads(request.body)
            if test['trials'].length <= 6:
                STORED_TEST = test
    context = {}
    return render(request, 'nvmt/finished.html', context)
