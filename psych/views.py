from .models import PsychDiagnosis, MedicalDiagnosis, Medication, Subject, _createId
from .forms import SubjectForm, MedicationForm, MedicalDiagnosisForm, PsychDiagnosisForm, GetTestForm

from nvmt import models as NvmtModels
from tmt import models as TmtModels

from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext, Context, loader
from django.utils.six import BytesIO

import json
import pdb
import random
import string
import math

TEST_TYPES = ['NVMT', 'TMT']
NVMT_GOALS = [{'x':25, 'y': 20}, {'x': 40, 'y': 15}, {'x': 21, 'y': 29}, {'x': 19, 'y': 5}, {'x': 14, 'y': 21}, {'x': 40, 'y': 9}, {'x': 16, 'y': 14}, {'x': 39, 'y': 26}, {'x': 18, 'y': 9}]

@login_required
def dashboard(request):
    context = {}
    if request.method == 'POST':
        print("in post")
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            cleaned_data = subject_form.clean()
            cleaned_data['user'] = request.user
            cleaned_data['id'] = _createId()
            subject_form.save(cleaned_data)
            return redirect('/psych/dashboard')
        else:
            return redirect('/psych/dashboard')
    else:
        template = 'psych/dashboard.html'
        context['user'] = request.user
        subjects = list(Subject.objects.filter(user=request.user))
        subjects_taking_tests = list()
        for subj in subjects:
            test_list = list(NvmtModels.NvmtTest.objects.filter(subject=subj).values())
            if len(test_list) != 0:
                for test in test_list:
                    subjects_taking_tests.append(test)
                
        context['subjects_taking_tests'] = subjects_taking_tests
        context['subjects'] = subjects
        context['subject_form'] = SubjectForm
        context['test_types'] = TEST_TYPES
        context['selected_test_type'] = ''
        return render(request, template, context)

def code_generator(size, chars):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_test(subject, test_type):
    code = code_generator(8, string.ascii_uppercase + string.digits)
    if test_type == 'NVMT':
        tests_being_taken = NvmtModels.NvmtTest.objects.filter(subject=subject)
        if len(list(tests_being_taken)) == 0:
            return NvmtModels.NvmtTest(test_code=code, subject=subject, status="Created")
        else:
            tests = list(tests_being_taken)
            for test in tests:
                if not test.completed:
                    return test
            return NvmtModels.NvmtTest(test_code=code, subject=subject, status="Created")
    elif test_type == 'TMT':
        tests_being_taken = TmtModels.TmtTest.objects.filter(subject=subject)
        if len(list(tests_being_taken)) == 0:
            return TmtModels.TmtTest(test_code=code, subject=subject, status="Created")
        else:
            tests = list(tests_being_taken)
            for test in tests:
                if not test.completed:
                    return test
            return TmtModels.TmtTest(test_code=code, subject=subject, status="Created")
    else:
        return None

@login_required
def generate_test_code(request, subject):
    test_type = request.GET.get('test_type', '')
    test = generate_test(subject=Subject.objects.get(id=subject), test_type=test_type)
    if test is not None:
        test.save()
        context = {'test': test}
        template = "psych/generated_code.html"
        return render(request, template, context)
    else:
        raise ValueError('Test has already been distributed')

@login_required
def add_medication(request):
    if request.is_ajax():
        if request.method == 'POST':
            # pdb.set_trace()
            print("in add_medication")
            print(request.body)
            med_obj = Medication(name=request.POST.get('name'), dosage=request.POST.get('dosage'))
            med_obj.save()
            return redirect('/psych/dashboard')
        else:
            return JsonResponse("Something went wrong")
    else:
        return JsonResponse("Should have never gotten here")
    return JsonResponse("wtf")

@login_required
def add_medical_diagnosis(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.body)
            print("in add_medical_diagnosis")
            med_diag_obj = MedicalDiagnosis(name=request.POST.get('name'))
            med_diag_obj.save()
            return redirect('/psych/dashboard')
        else:
            return JsonResponse("Something went wrong")
    else:
        return JsonResponse("Should have never gotten here")
    return JsonResponse("wtf")

@login_required
def add_psychological_diagnosis(request):
    if request.is_ajax():
        if request.method == 'POST':
            print("in add_psych_diagnosis")
            psy_diag_obj = PsychDiagnosis(name=request.POST.get('name'))
            psy_diag_obj.save()
            return redirect('/psych/dashboard')
        else:
            return JsonResponse("Something went wrong")
    else:
        return JsonResponse("Should have never gotten here")
    return JsonResponse("wtf")

@login_required
def databoard(request):
    context = {}

    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            cleaned_data = subject_form.clean()
            cleaned_data['user'] = request.user
            subject_form.save(cleaned_data)
            return redirect('/psych/databoard')
        else:
            return redirect('/psych/subject_register')
    else:
        template = 'psych/databoard.html'
        context['user'] = request.user
        subjects = list(Subject.objects.filter(user=request.user))
        '''
        subjects_taking_tests = list()
        for subj in subjects:
            test_list = list(Test.objects.filter(user=request.user, subject=subj).values())
            if len(test_list) != 0:
                subjects_taking_tests.append(test_list[0])
        context['subjects_taking_tests'] = subjects_taking_tests 
        '''
        context['subjects'] = subjects
        context['subject_form'] = SubjectForm 
        return render(request, template, context)

@login_required
def testing_center(request):
    context = {}
    context['errors'] = {}
    if request.method == 'POST':
        test_form = GetTestForm(request.POST)
        if test_form.is_valid():
            test_form = test_form.clean()
            potential_test_code = test_form['test_code'] 
            test_exists = get_object_or_404(NvmtModels.NvmtTest, test_code=potential_test_code)
            context['test'] = test_exists
            return redirect('psych/nvmt_test_report/{0}'.format(test_exists))
        else:
            context['errors'].push('test_code')
            return redirect('/psych/testing_center')
    else:
        test_form = GetTestForm()
        context['test_form'] = test_form
        template = 'psych/testing_center.html'
        return render(request, template, context)

def __getClickTime__(target):
    return target.click_time

@login_required
def nvmt_test_report(request, test_code):
    test_data = {}
    test = get_object_or_404(NvmtModels.NvmtTest, test_code=test_code)
    subj = get_object_or_404(Subject, id=test.subject.id)
    norms = test.get_normative_data(subj.age)
    complex_norms = test.get_complex_data(subj.age)
    simple_norms = test.get_simple_data(subj.age)
    test_data['test_code'] = test.test_code
    test_data['subject'] = test.subject.id
    test_data['completed'] = test.completed
    test_data['created'] = str(test.created)
    test_data['biased_norms'] = test.get_biased_data()
    test_data['trials'] = list()
    trials = list(NvmtModels.Trial.objects.filter(test=test))
    trial_counter = 0

    # setting up json along with making calculations for the report
    for trial in trials:
        json_trials = test_data['trials']
        # appending to a given trial a new trial with a list of cards
        json_trials.append({'trial_num': trial.trial_num, 'cards': list()})
        cards = list(NvmtModels.Card.objects.filter(trial=trial))
        card_counter = 0
        for card in cards:
            # initialize a JSON card object with its card number, a list of its targets, and how many times it was clicked
            json_trials[trial_counter]['cards'].append({'card_num': card.card_num, 'targets': list(), 'num_clicks': 0, 'target_distances': list() })
            json_cards = json_trials[trial_counter]['cards']
            targets = list(NvmtModels.Target.objects.filter(card=card))
            # sort by click time
            targets.sort(key=__getClickTime__)
            # only use the first two targets clicked
            target_dist = list()
            if len(targets) < 2:
                target_dist = list(targets)
            else:
                target_dist = list(targets[0:2])
            for target in target_dist:
                width = abs(NVMT_GOALS[card_counter]['x'] - target.x)
                height = abs(NVMT_GOALS[card_counter]['y'] - target.y)
                dist = round(math.sqrt(width**2 + height**2)/4, 4)
                json_cards[card_counter]['target_distances'].append(dist)
            json_cards[card_counter]['num_clicks'] = len(targets)
            for target in list(targets):
                json_targets = json_cards[card_counter]['targets']
                json_targets.append({'x': target.x, 'y': target.y, 'is_goal': target.is_goal, 'clicked': str(target.click_time)[0:10]})
            card_counter += 1
        original = norms[trial_counter]
        simple = simple_norms[trial_counter]
        complicated = complex_norms[trial_counter]
        json_trials[trial_counter]['originalValues'] = original
        json_trials[trial_counter]['simpleValues'] = simple
        json_trials[trial_counter]['complexValues'] = complicated
        trial_counter += 1
    # sending the json
    context = {'test': json.dumps(test_data)}
    template = 'psych/nvmt_test_report.html'
    return render(request, template, context)   

@login_required
def scales(request):
    context = {}
    if request.method == 'GET':
        '''
        questions = list(Question.objects.order_by('scale'))
        scale_questions = questions
        scales = []
        current = ''
        scales_counter = 0
        counter = 0
        for question in questions:
            if question.scale != current:
                if len(scales) < 1:
                    scales.append({'name': question.scale, 'questions': []})
                    current = question.scale
                    continue
                else:
                    scales.append({'name': question.scale, 'questions': []})
                    current = question.scale
                    scales[scales_counter]['questions'] = scale_questions[0:counter]
                    scale_questions = scale_questions[counter:]
                    scales_counter = scales_counter + 1
                    counter = 0
                    continue
            counter = counter + 1
        for scale in scales:
            print(scale['name'])
            print(scale['questions'])
        context['scales'] = scales
        '''
        template = 'psych/scales.html'
        return render(request, template, context)