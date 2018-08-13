from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, Context, loader
import pdb

from psych.models import PsychDiagnosis, MedicalDiagnosis, Medication, Subject
from psych.forms import LoginForm, RegistrationForm
# Create your views here.

def homepage(request): 
    context = {}
    if request.user.is_authenticated:
        return redirect('/psych/dashboard')
    template = 'home/home.html'
    return render(request, template, context)

def login_page(request):
    request_context = RequestContext(request)
    context = {}    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/psych/dashboard')
        else:
            context = {'login': 'failed'}
            return HttpResponse("Invalid login details supplied.")
    else:
        if request.user.is_authenticated:
            return redirect('/psych/dashboard')
        template = 'home/login.html'
        form = LoginForm()
        context = {'form': form}
        return render(request, template, context)

def register_page(request):
    request_context = RequestContext(request)
    context = Context()
    if request.is_ajax():
        username = request.GET.get('username', None)
        email = request.GET.get('email', None)
        phone_number = request.GET.get('phone_num', None)
        data = {
            'username_is_taken': User.objects.filter(username__iexact=username).exists(),
            'email_is_taken': User.objects.filter(email__iexact=email).exists(),
            'phone_num_is_taken': Musician.objects.filter(phone_num__iexact=phone_number).exists()
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        #user['phone_num'] = '2162223333'
        if registration_form.is_valid():
            #need to send email
            cleaned_data = registration_form.clean()
            registration_form.save(cleaned_data)
            context = {}
            return redirect('/')
    else:
        template = 'home/register.html'
        musicianForm = RegistrationForm ()
        context = {'form': musicianForm}
        return render(request, template, context)      
      
def bulma_temp(request):
    context = {}
    template = 'home/bulma_template.html'
    return render(request, template, context)
  
@login_required
def logout_request(request):
    logout(request)
    return redirect('/')