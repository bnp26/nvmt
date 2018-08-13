from django.contrib.auth.models import User
from django.db import models
import os
from binascii import hexlify

def _createId():
    return hexlify(os.urandom(16))

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
    ('HS_WO/D', 'Some High School (No Deploma)'),
    ('HS_W/D', 'High School Deploma'),
    ('C_WO/D', 'Some College Experience (No Degree)'),
    ('C_BA', 'Batchelor of Arts'),
    ('C_BS', 'Batchelor of Science'),
    ('C_MS', 'Masters Degree'),
    ('C_DO', 'Doctrate Degree'),
)

class MedicalDiagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 120, blank=False)
    
class PsychDiagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 120, blank=False)

class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 80, blank=False)
    dosage = models.CharField(max_length = 5, blank=False)

class Subject(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=_createId)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
    ethnicity = models.CharField(max_length = 3, choices=ETHNIC_CHOICES) 
    edu_lvl = models.CharField(max_length=9, choices=EDU_CHOICES)
    chronic_desc = models.CharField(max_length=155, blank=True, null=True)
    meds = models.ManyToManyField(Medication, blank=True)
    med_issues = models.ManyToManyField(MedicalDiagnosis, blank=True)
    mental_issues = models.ManyToManyField(PsychDiagnosis, blank=True)
    
    class Meta:
        ordering = ('id', 'created', )