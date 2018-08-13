from django.contrib import admin

from .models import PsychDiagnosis, MedicalDiagnosis, Medication, Subject
from .forms import SubjectForm, MedicationForm, MedicalDiagnosisForm, PsychDiagnosisForm, GetTestForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, Context, loader
from django.utils.six import BytesIO

import json
import pdb

@login_required
def dashboard(request):
    context = {}
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            cleaned_data = subject_form.clean()
            cleaned_data['user'] = request.user
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
            test_list = list(Test.objects.filter(user=request.user, subject=subj).values())
            if len(test_list) != 0:
                subjects_taking_tests.append(test_list[0])
        context['subjects'] = subjects
        context['subjects_taking_tests'] = subjects_taking_tests
        context['subject_form'] = SubjectForm
        return render(request, template, context)

@login_required
def add_medication(request):
    if request.is_ajax():
        if request.method == 'POST':
            new_med = request.POST.get('med')
            json_acceptable_string = new_med.encode('ascii','replace')
            med_dict = json.loads(json_acceptable_string)
            med_obj = Medication(name=med_dict['name'], dosage=med_dict['dosage'])
            med_obj.save()
            return JsonResponse(serialize('json', list(Medication.objects.all())), safe=False)
        else:
            return JsonResponse("was trying to do a ajax get request")
    else:
        return JsonResponse("was trying to do a ajax get request")

@login_required
def add_medical_diagnosis(request):
    if request.is_ajax():
        if request.method == 'POST':
            new_issue = request.POST.get('med_issue')
            json_acceptable_string = new_issue.encode('ascii','replace')
            print(json_acceptable_string)
            issue_dict = json.loads(json_acceptable_string)
            issue_obj = MedicalDiagnosis(name=issue_dict['name'])
            issue_obj.save()
            return JsonResponse(serialize('json', list(MedicalDiagnosis.objects.all())), safe=False)
        else:
            return JsonResponse("was trying to do a ajax get request")
    else:
        return JsonResponse("was trying to do a ajax get request")

@login_required
def add_psychological_diagnosis(request):
    if request.is_ajax():
        if request.method == 'POST':
            new_issue = request.POST.get('psych_issue')
            json_acceptable_string = new_issue.encode('ascii','replace')
            print(json_acceptable_string)
            issue_dict = json.loads(json_acceptable_string)
            issue_obj = PsychDiagnosis(name=issue_dict['name'])
            issue_obj.save()
            return JsonResponse(serialize('json', list(PsychDiagnosis.objects.all())), safe=False)
        else:
            return JsonResponse("was trying to do a ajax get request")
    else:
        return JsonResponse("was trying to do a ajax get request")

@login_required
def databoard(request):
    context = {}

    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            cleaned_data = subject_form.clean()
            cleaned_data['user'] = request.user
            subject_form.save(cleaned_data)
            return redirect('/psych_app/databoard')
        else:
            return redirect('/psych_app/subject_register')
    else:
        template = 'psych_app/databoard.html'
        context['user'] = request.user
        subjects = list(Subject.objects.filter(user=request.user))
        subjects_taking_tests = list()
        for subj in subjects:
            test_list = list(Test.objects.filter(user=request.user, subject=subj).values())
            if len(test_list) != 0:
                subjects_taking_tests.append(test_list[0])
        context['subjects'] = subjects
        context['subjects_taking_tests'] = subjects_taking_tests 
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
            potential_test_code = get_test_form['test_code'] 
            test_exists = get_object_or_404(Test, test_code=potential_test_code)
            context['test'] = test_exists
            return redirect('psych_app/spy/{0}'.format(test_exists))
        else:
            context['errors'].push('test_code');
            return redirect('/psych_app/testing_center')
    else:
        test_form = GetTestForm()
        context['test_form'] = test_form
        template = 'psych_app/testing_center.html'
        return render(request, template, context)

@login_required
def scales(request):
    context = {}
    if request.method == 'GET':
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
        template = 'psych_app/scales.html'
        return render(request, template, context)