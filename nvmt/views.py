from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
    test = get_object_or_404(Test, test_code=test_code)
    if test.completed:
        return JsonResponse("Test has already been completed!!! Do Note overwrite!!!!")
    else:
        context['test'] = test
    return render(request, 'nvmt/index.html', context)

def send_test_data(request, test_code):
    if request.is_ajax():
        if request.method == 'POST':
            test_json = json.loads(request.body)
            test = get_object_or_404(Test, test_code=test_code)
            if test.completed:
                return JsonResponse("Test has already been completed!!! Do Note overwrite!!!!")
            # for now, parse data and save the test assuming the took the whole test.
            for trial in test_json['trials']:
                current_trial = Trial(trial_num=trial['trial_num'], test=test)
                current_trial.save()
                cards = list()
                for card in trial['finishedCards']:
                    current_card = Card(trial=current_trial, card_num = card['card_num'])
                    current_card.save()
                    targets = list()
                    for target_dict in card['clicked_targets']:
                        target = target_dict['target']
                        time = target['clicked'].split(':')
                        current_target = Target(card=current_card, x=target['x'], y=target['y'], is_goal=target['is_target'], click_time=datetime.timedelta(hours=int(time[0]), minutes=int(time[1]), seconds=int(time[2]), milliseconds=int(time[3])))
                        current_target.save()
            test.completed = True
            test.save(['completed'])
            return JsonResponse("Success Saving Test!")
    else:
        context = {}
        return render(request, 'nvmt/finished.html', context)
