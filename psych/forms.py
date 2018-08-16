from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import os
from binascii import hexlify, unhexlify
import pdb

from .models import Subject, PsychDiagnosis, MedicalDiagnosis, Medication

class LoginForm(forms.Form):
    username = forms.CharField(max_length=18, required=True, help_text='username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
        
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'validate'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'validate'}))
    username = forms.CharField(min_length=4, max_length=18, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'validate'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'validate'}))
    password1 = forms.CharField(min_length=6, max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'validate'}))
    password2 = forms.CharField(min_length=6, max_length=18, required=True, help_text='confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password' , 'class':'validate'}))
    
    def clean(self):
        data = super(RegistrationForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
    
    def save(self, data):
        user =  User.objects.create_user(first_name = data.get('first_name'), last_name = data.get('last_name'), email = data.get('email'), username = data.get('username'), password = data.get('password1'))
        user.save()
        
class GetTestForm(forms.Form):
    test_code = forms.CharField(max_length=11, required=True, help_text='enter code for test', widget=forms.TextInput(attrs={'placeholder':'QPPI CODE', 'name':'test_code', 'class':'col s6 offset-s3 center', 'style': 'font-size: 25pt'}))

    def clean(self):
        super().clean()
        return self.cleaned_data

class MedicationForm(forms.Form):
    name = forms.CharField(max_length=80, required=True, widget=forms.TextInput(attrs={'placeholder': 'medication name', 'class':'col s8'}))
    dosage = forms.CharField(max_length=5, required=True, widget=forms.TextInput(attrs={'placeholder':'dosage', 'class':'col s4'}))
    
    def save(self, data):
        med = Medication(name=data.get('name'), dosage=data.get('dosage'))
        med.save()

class MedicalDiagnosisForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={'placeholder': 'new medical diagnosis', 'class':'col s12'}))
    
    def save(self, data):
        med_diag = MedicalDiagnosis(name=data.get('name'))
        med_diag.save()

class PsychDiagnosisForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={'placeholder': 'new psychological diagnosis', 'class':'col s12'}))
    
    def save(self, data):
        psych_diag = PsychDiagnosis(name=data.get('name'))
        psych_diag.save()

class SubjectForm(forms.Form):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    ETHNIC_CHOICES = (
        ('AfA', 'African American'),
        ('CA', 'Caucasian American'),
        ('AsA', 'Asian American'),
        ('HA', 'Hispanic American'),
        ('ArA', 'Arab American'),
        ('NA', 'Native American'),
    )

    EDU_CHOICES = (
        ('HS_WO/D', 'Some High School (No Diploma)'),
        ('HS_W/D', 'High School Diploma'),
        ('C_WO/D', 'Some College Experience (No Diploma)'),
        ('C_BA', 'Bachelor of Arts'),
        ('C_BS', 'Bachelor of Science'),
        ('C_MS', 'Master\'s Degree'),
        ('C_DO', 'Doctorate Degree'),
    )
    
    MED_CHOICES = ()
    MED_ISSUE_CHOICES = ()
    MENTAL_ISSUE_CHOICES = ()
    
    meds = list(Medication.objects.all())
    med_issues = list(MedicalDiagnosis.objects.all())
    mental_issues = list(PsychDiagnosis.objects.all())

    for choice in meds:
        id = choice.id
        shown = '{0} {1}'.format(choice.name, choice.dosage)
        MED_CHOICES = MED_CHOICES + ((id, shown), )
    
    for choice in med_issues:
        id = choice.id
        val = '{0}'.format(choice.name)
        MED_ISSUE_CHOICES = MED_ISSUE_CHOICES + ((id, val), )
    
    for choice in mental_issues:
        id = choice.id
        val = '{0}'.format(choice.name)
        MENTAL_ISSUE_CHOICES = MENTAL_ISSUE_CHOICES + ((id, val), )
    
    age = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Age', 'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    ethnicity = forms.ChoiceField(choices=ETHNIC_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    education = forms.ChoiceField(choices=EDU_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    chronic_desc = forms.CharField(max_length=255, required=False, help_text='chronic description in less than 255 characters', 
                                   widget=forms.Textarea(attrs={'placeholder':'chronic description', 'class':'materialize-textarea txtarea'}))
    meds = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'meds-choices'}), choices=MED_CHOICES, required=False)
    med_issues = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'med-issues-choices'}), choices=MED_ISSUE_CHOICES, required=False)
    mental_issues = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'mental-issues-choices'}), choices=MENTAL_ISSUE_CHOICES, required=False)
    
    def save(self, data):
        print("saving")
        user = data.get('user')
        new_user = User.objects.get(username=user.get_username())
        subject = Subject(user=new_user, age=data.get('age'), gender=data.get('gender'), ethnicity=data.get('ethnicity'), edu_lvl=data.get('education'), chronic_desc = data.get('chronic_desc'))
        subject.save()
        
        for med in data.get('meds'):
            med_obj = Medication.objects.get(id=med)
            subject.meds.add(med_obj)
        
        for med_issue in data.get('med_issues'):
            med_issue_obj = MedicalDiagnosis.objects.get(id=med_issue)
            subject.med_issues.add(med_issue_obj)
        
        for mental_issue in data.get('mental_issues'):
            mental_issue_obj = PsychDiagnosis.objects.get(id=mental_issue)
            subject.mental_issues.add(mental_issue)